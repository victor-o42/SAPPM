"""
Staff Authentication Module
Handles staff registration, login verification, and profile management.
"""

from typing import Optional, Dict, Any
from src.db.supabase_client import get_supabase

supabase = get_supabase()

def sign_up_staff(email: str, password: str, full_name: str, staff_id: str, department: str = "Academic Affairs") -> Dict[str, Any]:
    """
    Registers a new staff member with Supabase Auth and saves profile metadata.
    """
    try:
        # Create user in Supabase Auth
        res = supabase.auth.sign_up({
            "email": email.strip(),
            "password": password,
            "options": {
                "data": {
                    "full_name": full_name.strip(),
                    "staff_id": staff_id.strip(),
                    "department": department
                }
            }
        })
        
        user = res.user
        if not user:
            return {"success": False, "message": "Sign up failed. Please check credentials and try again."}

        # Store profile details in staff_profiles table
        profile_data = {
            "id": user.id,
            "full_name": full_name.strip(),
            "staff_id": staff_id.strip(),
            "email": email.strip(),
            "role": "Academic Advisor",
            "department": department
        }
        supabase.table("staff_profiles").upsert(profile_data).execute()

        return {
            "success": True, 
            "user": user, 
            "message": f"Account successfully created for {full_name}."
        }
    except Exception as e:
        return {"success": False, "message": str(e)}


def sign_in_staff(email: str, password: str) -> Dict[str, Any]:
    """
    Authenticates a staff member and loads their profile.
    """
    try:
        res = supabase.auth.sign_in_with_password({
            "email": email.strip(),
            "password": password
        })
        
        user = res.user
        session = res.session
        
        if not user:
            return {"success": False, "message": "Invalid email or password."}
            
        # Fetch profile from staff_profiles table
        profile_res = supabase.table("staff_profiles").select("*").eq("id", user.id).execute()
        profile = profile_res.data[0] if profile_res.data else {
            "id": user.id,
            "email": user.email,
            "full_name": user.user_metadata.get("full_name", "Staff Member"),
            "staff_id": user.user_metadata.get("staff_id", "N/A"),
            "role": "Academic Staff"
        }

        return {
            "success": True, 
            "user": user, 
            "session": session,
            "profile": profile,
            "message": f"Welcome, {profile.get('full_name', 'Staff')}."
        }
    except Exception as e:
        return {"success": False, "message": str(e)}


def sign_out_staff() -> Dict[str, Any]:
    """
    Signs out the current user session.
    """
    try:
        supabase.auth.sign_out()
        return {"success": True, "message": "Successfully signed out."}
    except Exception as e:
        return {"success": False, "message": str(e)}
