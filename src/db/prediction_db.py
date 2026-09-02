"""
Prediction Database Service for S.A.P.P.M
Provides dual-layer persistent storage (Supabase Cloud + Local SQLite Cache)
Ensures student prediction records and audit history are always saved and retrieved reliably.
"""

import os
import sqlite3
from datetime import datetime
from typing import List, Dict, Any, Optional
from src.db.supabase_client import get_supabase

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "sappm_history.db")

def init_sqlite_db():
    """Initializes the local SQLite database table if it does not exist."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS prediction_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                reg_no TEXT NOT NULL,
                study_hours REAL NOT NULL,
                attendance REAL NOT NULL,
                participation REAL NOT NULL,
                predicted_grade TEXT NOT NULL,
                confidence REAL NOT NULL,
                predicted_by TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# Ensure table exists on import
try:
    init_sqlite_db()
except Exception:
    pass


def save_student_prediction(
    student_name: str,
    reg_no: str,
    study_hours: float,
    attendance: float,
    participation: float,
    predicted_grade: str,
    confidence: float,
    predicted_by: Optional[str] = "Staff Member",
    user_id: Optional[str] = None
) -> bool:
    """
    Saves a student prediction record to local SQLite and syncs to Supabase if connected.
    """
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Save to local SQLite (guaranteed persistence)
    try:
        init_sqlite_db()
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO prediction_history 
                (student_name, reg_no, study_hours, attendance, participation, predicted_grade, confidence, predicted_by, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                student_name,
                reg_no,
                float(study_hours),
                float(attendance),
                float(participation),
                predicted_grade,
                float(confidence),
                predicted_by or "Staff Member",
                now_str
            ))
            conn.commit()
    except Exception as e:
        print(f"SQLite save error: {e}")

    # 2. Sync to Supabase Cloud if available
    try:
        supabase = get_supabase()
        student_res = supabase.table("student_data").insert({
            "student_name": student_name,
            "matric_number": reg_no,
            "weekly_self_study_hours": float(study_hours),
            "attendance_percentage": float(attendance),
            "class_participation": float(participation),
            "total_score": 0.0,
            "created_by": user_id
        }).execute()

        student_id = None
        if student_res.data and isinstance(student_res.data[0], dict):
            student_id = student_res.data[0].get("student_id")

        if student_id:
            supabase.table("prediction_output").insert({
                "student_id": student_id,
                "model_id": 1,
                "predicted_grade": predicted_grade,
                "risk_level": "LOW RISK" if predicted_grade in ["A", "B"] else ("MEDIUM RISK" if predicted_grade == "C" else "HIGH RISK"),
                "confidence_score": round(confidence, 2),
                "predicted_by": user_id
            }).execute()
    except Exception as e:
        # Non-blocking warning if Supabase is offline
        print(f"Supabase sync warning: {e}")

    return True


def get_all_prediction_history(
    limit: int = 100, 
    user_id: Optional[str] = None, 
    predicted_by: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Retrieves personal prediction history records for the logged-in staff member.
    """
    records = []

    # Try fetching from Supabase first
    try:
        supabase = get_supabase()
        query = supabase.table("prediction_output").select("*, student_data(*)")
        
        if user_id:
            query = query.eq("predicted_by", user_id)
            
        res = query.order("prediction_date", desc=True).limit(limit).execute()
        if res.data and len(res.data) > 0:
            for item in res.data:
                stu = item.get("student_data") or {}
                date_val = item.get("prediction_date", "")
                if date_val:
                    try:
                        date_val = datetime.fromisoformat(date_val.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
                    except Exception:
                        pass
                records.append({
                    "student_name": stu.get("student_name", "Unknown Student"),
                    "reg_no": stu.get("matric_number", "N/A"),
                    "study_hours": stu.get("weekly_self_study_hours", 0.0),
                    "attendance": stu.get("attendance_percentage", 0.0),
                    "participation": stu.get("class_participation", 0.0),
                    "predicted_grade": item.get("predicted_grade", "N/A"),
                    "confidence": item.get("confidence_score", 0.0),
                    "created_at": date_val or "Recently"
                })
            return records
    except Exception as e:
        print(f"Supabase fetch fallback to SQLite: {e}")

    # Fallback to local SQLite with personal filtering
    try:
        init_sqlite_db()
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if predicted_by:
                cursor.execute("""
                    SELECT student_name, reg_no, study_hours, attendance, participation, predicted_grade, confidence, created_at
                    FROM prediction_history
                    WHERE predicted_by = ?
                    ORDER BY id DESC
                    LIMIT ?
                """, (predicted_by, limit))
            else:
                cursor.execute("""
                    SELECT student_name, reg_no, study_hours, attendance, participation, predicted_grade, confidence, created_at
                    FROM prediction_history
                    ORDER BY id DESC
                    LIMIT ?
                """, (limit,))
            rows = cursor.fetchall()
            for r in rows:
                records.append({
                    "student_name": r["student_name"],
                    "reg_no": r["reg_no"],
                    "study_hours": r["study_hours"],
                    "attendance": r["attendance"],
                    "participation": r["participation"],
                    "predicted_grade": r["predicted_grade"],
                    "confidence": r["confidence"],
                    "created_at": str(r["created_at"])[:16]
                })
    except Exception as e:
        print(f"SQLite fetch error: {e}")

    return records
