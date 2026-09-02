"""
Prediction & Analytics Service for S.A.P.P.M
Loads trained machine learning models, generates real-time predictions,
calculates SHAP explainability values, and logs results to Supabase.
"""

import warnings
warnings.filterwarnings("ignore")
import joblib
import pandas as pd
import numpy as np
import shap
from typing import Dict, Any, List, Optional, cast
from src.db.supabase_client import get_supabase

# Cache model and explainer in memory for instant inference
_MODEL = None
_ENCODER = None
_EXPLAINER = None

def get_model_assets():
    """
    Loads the trained champion model, label encoder, and SHAP TreeExplainer.
    """
    global _MODEL, _ENCODER, _EXPLAINER
    if _MODEL is None:
        _MODEL = joblib.load("models/best_model.pkl")
        _ENCODER = joblib.load("models/best_label_encoder.pkl")
        _EXPLAINER = shap.TreeExplainer(_MODEL)
    return _MODEL, _ENCODER, _EXPLAINER


def predict_student_grade(
    study_hours: float,
    attendance: float,
    participation: float,
    total_score: Optional[float] = 0.0,
    student_name: Optional[str] = "Student",
    matric_number: Optional[str] = None,
    user_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Predicts a student's grade, risk level, confidence score, and logs to Supabase.
    """
    model, encoder, explainer = get_model_assets()

    # Structure feature DataFrame matching training columns (strictly without total_score)
    student_df = pd.DataFrame([{
        "weekly_self_study_hours": float(study_hours),
        "attendance_percentage": float(attendance),
        "class_participation": float(participation)
    }])

    # Run model prediction and probabilities
    pred_encoded = model.predict(student_df)
    probabilities = model.predict_proba(student_df)[0]
    predicted_grade = encoder.inverse_transform(pred_encoded)[0]
    confidence_score = float(probabilities.max() * 100)

    # Determine Academic Risk Category
    if predicted_grade in ["A", "B"]:
        risk_level = "LOW RISK"
        risk_color = "#10B981"
        recommendation = "Student is performing strongly. Encourage consistent study habits."
    elif predicted_grade == "C":
        risk_level = "MEDIUM RISK"
        risk_color = "#F59E0B"
        recommendation = "Student is in the average tier. Increasing attendance and study hours can elevate them to Grade B."
    else:
        risk_level = "HIGH RISK"
        risk_color = "#EF4444"
        recommendation = "Immediate academic intervention recommended. Focus on core continuous assessment and tutoring support."

    # Compute SHAP feature contributions
    shap_values = explainer.shap_values(student_df)
    
    # Format SHAP values cleanly for storage and charting
    if isinstance(shap_values, list):
        # Multiclass list of arrays
        class_idx = int(pred_encoded[0])
        feature_shap = shap_values[class_idx][0].tolist() if len(shap_values) > class_idx else [0,0,0]
    elif hasattr(shap_values, "ndim") and shap_values.ndim == 3:
        class_idx = int(pred_encoded[0])
        feature_shap = shap_values[0, :, class_idx].tolist()
    else:
        feature_shap = shap_values[0].tolist() if len(shap_values) > 0 else [0,0,0]

    shap_breakdown = {
        "weekly_self_study_hours": feature_shap[0] if len(feature_shap) > 0 else 0,
        "attendance_percentage": feature_shap[1] if len(feature_shap) > 1 else 0,
        "class_participation": feature_shap[2] if len(feature_shap) > 2 else 0
    }

    # Grade probability dictionary for charting
    grade_distribution = {
        grade: float(prob * 100)
        for grade, prob in zip(encoder.classes_, probabilities)
    }

    # Log to Supabase Database
    try:
        supabase = get_supabase()
        
        # 1. Insert into student_data
        student_row = {
            "student_name": student_name,
            "matric_number": matric_number or f"STU-{int(np.random.randint(1000, 9999))}",
            "weekly_self_study_hours": float(study_hours),
            "attendance_percentage": float(attendance),
            "class_participation": float(participation),
            "total_score": float(total_score),
            "created_by": user_id
        }
        student_res = supabase.table("student_data").insert(student_row).execute()
        student_id = None
        if student_res.data and isinstance(student_res.data[0], dict):
            student_id = student_res.data[0].get("student_id")

        # 2. Insert into prediction_output
        if student_id:
            prediction_row = {
                "student_id": student_id,
                "model_id": 1,  # 1 = XGBoost Champion
                "predicted_grade": predicted_grade,
                "risk_level": risk_level,
                "confidence_score": round(confidence_score, 2),
                "shap_summary": shap_breakdown,
                "predicted_by": user_id
            }
            supabase.table("prediction_output").insert(prediction_row).execute()
    except Exception as e:
        # Non-blocking log error
        print(f"Supabase logging warning: {e}")

    return {
        "student_name": student_name,
        "matric_number": matric_number,
        "predicted_grade": predicted_grade,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "confidence_score": confidence_score,
        "recommendation": recommendation,
        "grade_distribution": grade_distribution,
        "shap_breakdown": shap_breakdown,
        "features": {
            "weekly_self_study_hours": study_hours,
            "attendance_percentage": attendance,
            "class_participation": participation,
            "total_score": total_score
        }
    }


def fetch_prediction_history(limit: int = 50) -> List[Dict[str, Any]]:
    """
    Fetches recent prediction records joined with student information from Supabase.
    """
    try:
        supabase = get_supabase()
        res = (
            supabase.table("prediction_output")
            .select("*, student_data(*), model_info(model_name)")
            .order("prediction_date", desc=True)
            .limit(limit)
            .execute()
        )
        return cast(List[Dict[str, Any]], res.data or [])
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []


def fetch_model_registry() -> List[Dict[str, Any]]:
    """
    Retrieves the model comparison audit list from Supabase model_info table.
    """
    try:
        supabase = get_supabase()
        res = supabase.table("model_info").select("*").order("accuracy", desc=True).execute()
        return cast(List[Dict[str, Any]], res.data or [])
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []
