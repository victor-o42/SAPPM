"""
Supabase client helper for S.A.P.P.M
Manages database connection for staff auth, student records, and predictions.
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_ANON_KEY")

def get_supabase() -> Client:
    """
    Initializes and returns the Supabase client instance.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "Supabase credentials missing. Ensure SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are in .env."
        )
    return create_client(SUPABASE_URL, SUPABASE_KEY)
