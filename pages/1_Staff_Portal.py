"""
Staff Portal & Authentication Page for S.A.P.P.M
- Pre-auth: Ultra-Premium Double-Bezel Glassmorphic 3D Card with rotating laser border beam, spring typography, and 100% native Streamlit forms (Zero Iframes = Zero Trapping, Zero Cramming, Instant Supabase Sync!)
- Post-auth: The Full Original Student Academic Performance Prediction System (app_3.py architecture with Sliders, Model Inference, Prediction Confidence, Probabilities Distribution Chart, SHAP Attribution, and Feature Importance)
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap
from src.auth import sign_in_staff, sign_up_staff, sign_out_staff

st.set_page_config(
    page_title="Staff Portal - S.A.P.P.M",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Global Scrollbar & Layout Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    /* Clean Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #05070E;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.3);
    }

    [data-testid="stSidebar"] { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { visibility: hidden !important; }

    html, body, [class*="css"], .stApp {
        background-color: #05070E !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #FFFFFF !important;
    }

    /* Double-Bezel Native Back to Home Pill */
    [data-testid="stPageLink"] {
        position: fixed !important;
        top: 24px !important;
        left: 36px !important;
        z-index: 999999 !important;
    }

    [data-testid="stPageLink"] a {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        padding: 10px 22px !important;
        border-radius: 9999px !important;
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.2) !important;
        color: #CBD5E1 !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        cursor: pointer !important;
    }

    [data-testid="stPageLink"] a:hover {
        color: #FFFFFF !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        background: rgba(15, 23, 42, 0.9) !important;
        box-shadow: 0 12px 30px -2px rgba(99, 102, 241, 0.3), inset 0 1px 1px 0 rgba(255, 255, 255, 0.4) !important;
        transform: translateX(-4px) !important;
    }

    [data-testid="stPageLink"] a p {
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        margin: 0 !important;
        color: inherit !important;
    }

    /* Ambient Background Glows */
    .auth-ambient-glow {
        position: fixed;
        top: -10%;
        left: 50%;
        transform: translateX(-50%);
        width: 100vw;
        height: 600px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.18) 0%, rgba(99, 102, 241, 0.08) 45%, transparent 75%);
        filter: blur(90px);
        pointer-events: none;
        z-index: 0;
    }

    /* 3D Glassmorphic Auth Card Container */
    .auth-card-shell {
        position: relative;
        border-radius: 28px;
        padding: 2px;
        overflow: hidden;
        background: rgba(255, 255, 255, 0.08);
        box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85);
        margin: 2rem auto;
        max-width: 520px;
    }

    .auth-card-shell::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            transparent,
            transparent 65%,
            rgba(255, 255, 255, 0.85) 85%,
            #818CF8 95%,
            transparent
        );
        animation: rotateBorderBeam 4s linear infinite;
        z-index: 1;
    }

    @keyframes rotateBorderBeam {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .auth-card-core {
        position: relative;
        z-index: 2;
        border-radius: 26px;
        background: rgba(11, 15, 28, 0.95);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        padding: 38px 40px;
    }

    .auth-emblem {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 14px auto;
        font-weight: 900;
        font-size: 1.3rem;
        color: #FFFFFF;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.4);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 9999px !important;
        padding: 4px !important;
        gap: 0 !important;
        margin-bottom: 24px !important;
    }

    .stTabs [data-baseweb="tab"] {
        flex: 1 !important;
        border-radius: 9999px !important;
        border: none !important;
        background: transparent !important;
        color: #94A3B8 !important;
        font-weight: 700 !important;
        font-size: 0.85rem !important;
        padding: 8px 16px !important;
        transition: all 0.25s ease !important;
        justify-content: center !important;
    }

    .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        color: #05070E !important;
        box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25) !important;
    }

    /* Native Form Inputs Styling */
    .stTextInput label, .stSelectbox label {
        color: #94A3B8 !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.04em !important;
        text-transform: uppercase !important;
        margin-bottom: 4px !important;
    }

    .stTextInput input {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        font-size: 0.95rem !important;
        padding: 10px 14px !important;
        transition: all 0.25s ease !important;
    }

    .stTextInput input:focus {
        border-color: #FFFFFF !important;
        background: rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.15) !important;
    }

    /* Submit Button (Origin Breathing Glass Button) */
    .stButton button[kind="primary"], .stFormSubmitButton button {
        width: 100% !important;
        padding: 12px 28px !important;
        border-radius: 9999px !important;
        background: #FFFFFF !important;
        color: #05070E !important;
        font-size: 0.95rem !important;
        font-weight: 800 !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.3), 0 0 15px 2px rgba(99, 102, 241, 0.3) !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
        margin-top: 10px !important;
    }

    .stButton button[kind="primary"]:hover, .stFormSubmitButton button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 16px 35px rgba(255, 255, 255, 0.45), 0 0 25px rgba(56, 189, 248, 0.45) !important;
    }
    </style>
""", unsafe_allow_html=True)

is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})

# =========================================================================
# 1. AUTHENTICATED STATE: THE ORIGINAL PREDICTION & EXPLAINABILITY SYSTEM
# =========================================================================
if is_auth:
    # Top navigation bar with active session badge & logout
    st.markdown("""
        <div style="max-width: 1200px; margin: 0 auto; padding: 24px 32px 10px 32px; display: flex; justify-content: space-between; align-items: center;">
            <a href="/" target="_top" style="font-size: 1.35rem; font-weight: 900; color: #FFFFFF; text-decoration: none;">SAPPM</a>
            <div style="display: flex; gap: 32px;">
                <span style="color: #FFFFFF; font-size: 0.92rem; font-weight: 700;">Predictor Dashboard</span>
            </div>
            <div>
                <span style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 9999px; color: #34D399; font-size: 0.8rem; font-weight: 700;">● Active Staff Session</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Header banner with staff profile & Sign Out
    col_hdr, col_out = st.columns([4, 1])
    with col_hdr:
        st.markdown(f"""
            <div style="padding: 1rem 0; margin-bottom: 1rem;">
                <h1 style="font-size: 2.2rem; font-weight: 900; margin: 0; color: #FFFFFF;">Student Academic Performance Prediction System</h1>
                <p style="color: #94A3B8; font-size: 1rem; margin-top: 0.4rem;">
                    Logged in as: <strong style="color: #FFFFFF;">{profile.get('full_name', 'Faculty Staff Member')}</strong> 
                    &nbsp;|&nbsp; Dept: <strong style="color: #818CF8;">{profile.get('department', 'Academic Affairs')}</strong>
                    &nbsp;|&nbsp; Staff ID: <strong style="color: #34D399;">{profile.get('staff_id', 'STF-001')}</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_out:
        st.markdown("<div style='padding-top: 1.5rem;'>", unsafe_allow_html=True)
        if st.button("Sign Out ↪", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["profile"] = None
            st.session_state["auth_error"] = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 16px 20px; margin-bottom: 24px;">
            <p style="margin: 0; color: #CBD5E1; font-size: 0.95rem;">
                This system predicts a student's academic grade using Machine Learning. It also explains why the prediction was made using Explainable AI (SHAP).
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Load trained model and label encoder
    model = None
    encoder = None
    explainer = None
    model_loaded = False

    try:
        model = joblib.load("models/random_forest_model.pkl")
        encoder = joblib.load("models/label_encoder.pkl")
        explainer = shap.TreeExplainer(model)
        model_loaded = True
    except Exception as e:
        model_loaded = False
        st.warning(f"Note on model loading: {e}")

    # Two column layout: Input Controls & Prediction Analytics
    c_left, c_right = st.columns([1, 1], gap="large")

    with c_left:
        st.subheader("Enter Student Information")
        study_hours = st.slider(
            "Weekly Self Study Hours",
            min_value=0.0,
            max_value=40.0,
            value=10.0,
            step=0.5
        )

        attendance = st.slider(
            "Attendance Percentage",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=1.0
        )

        participation = st.slider(
            "Class Participation",
            min_value=0.0,
            max_value=10.0,
            value=5.0,
            step=0.5
        )

        total_score = st.slider(
            "Total Score",
            min_value=0.0,
            max_value=100.0,
            value=50.0,
            step=1.0
        )

        predict_btn = st.button("Predict Grade", type="primary", use_container_width=True)

    with c_right:
        if predict_btn and model_loaded and model is not None and encoder is not None and explainer is not None:
            student_data = pd.DataFrame([{
                "weekly_self_study_hours": study_hours,
                "attendance_percentage": attendance,
                "class_participation": participation,
                "total_score": total_score
            }])

            # Make prediction
            prediction = model.predict(student_data)
            probabilities = model.predict_proba(student_data)
            predicted_grade = encoder.inverse_transform(prediction)
            confidence = probabilities.max() * 100

            st.success(f"Predicted Grade: **{predicted_grade[0]}**")
            st.info(f"Prediction Confidence: **{confidence:.2f}%**")

            # Probability Chart
            st.subheader("Grade Prediction Probabilities")
            grades = encoder.classes_
            fig, ax = plt.subplots(figsize=(6, 3))
            fig.patch.set_facecolor('#05070E')
            ax.set_facecolor('#090D1A')
            ax.bar(grades, probabilities[0], color='#818CF8', edgecolor='rgba(255,255,255,0.2)')
            ax.tick_params(colors='#CBD5E1')
            ax.set_xlabel("Grades", color='#94A3B8')
            ax.set_ylabel("Probability", color='#94A3B8')
            ax.set_title("Prediction Probability Distribution", color='#FFFFFF')
            for spine in ax.spines.values():
                spine.set_color('rgba(255,255,255,0.1)')
            st.pyplot(fig)

            # SHAP Explainability Section
            st.subheader("SHAP Prediction Explanation")
            shap_values = explainer.shap_values(student_data)
            shap_fig, shap_ax = plt.subplots(figsize=(6, 3))
            shap_fig.patch.set_facecolor('#05070E')
            shap_ax.set_facecolor('#090D1A')
            shap.summary_plot(shap_values, student_data, plot_type="bar", show=False)
            shap_ax.tick_params(colors='#CBD5E1')
            for spine in shap_ax.spines.values():
                spine.set_color('rgba(255,255,255,0.1)')
            st.pyplot(shap_fig)

            # Feature Importance Section
            st.subheader("Feature Importance")
            importance = model.feature_importances_
            features = ["Study Hours", "Attendance", "Participation", "Total Score"]
            fig2, ax2 = plt.subplots(figsize=(6, 3))
            fig2.patch.set_facecolor('#05070E')
            ax2.set_facecolor('#090D1A')
            ax2.bar(features, importance, color='#38BDF8', edgecolor='rgba(255,255,255,0.2)')
            ax2.tick_params(colors='#CBD5E1')
            ax2.set_ylabel("Importance", color='#94A3B8')
            ax2.set_title("Model Feature Importance", color='#FFFFFF')
            for spine in ax2.spines.values():
                spine.set_color('rgba(255,255,255,0.1)')
            st.pyplot(fig2)
        elif predict_btn and not model_loaded:
            st.error("Model assets could not be loaded. Please ensure model files are present in the models directory.")
        elif not predict_btn:
            st.markdown("""
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px dashed rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 4rem 2rem; text-align: center; margin-top: 1.5rem;">
                    <div style="font-size: 2.5rem; margin-bottom: 1rem;">📊</div>
                    <h3 style="color: #FFFFFF; margin: 0 0 0.5rem 0;">Awaiting Input Submission</h3>
                    <p style="color: #94A3B8; font-size: 0.92rem; max-width: 380px; margin: 0 auto;">
                        Adjust the student metrics on the left and click <strong>Predict Grade</strong> to generate real-time grade forecasts, confidence attributions, and SHAP decision explanations.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# =========================================================================
# 2. UNAUTHENTICATED STATE: 3D ROTATING LASER CARD WITH 100% NATIVE FORMS
# =========================================================================
else:
    # Native Streamlit Back Link
    st.page_link("app.py", label="← Back to Home")

    st.markdown('<div class="auth-ambient-glow"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.8, 1])

    with col2:
        st.markdown("""
            <div class="auth-card-shell">
                <div class="auth-card-core">
                    <div class="auth-emblem">S</div>
                    <h2 style="text-align: center; font-size: 1.65rem; font-weight: 900; letter-spacing: -0.03em; color: #FFFFFF; margin: 0 0 4px 0;">Welcome Back</h2>
                    <p style="text-align: center; font-size: 0.85rem; color: #94A3B8; margin: 0 0 20px 0;">Sign in or register to access student prediction analytics</p>
        """, unsafe_allow_html=True)

        tab_signin, tab_signup = st.tabs(["Sign In", "Create Account"])

        # TAB 1: SIGN IN
        with tab_signin:
            with st.form("signin_form", clear_on_submit=False):
                email = st.text_input("Institutional Email", placeholder="staff@university.edu", key="signin_email")
                password = st.text_input("Password", type="password", placeholder="••••••••••••", key="signin_password")

                col_rem, col_fgt = st.columns([1, 1])
                with col_rem:
                    st.checkbox("Remember me", value=True)
                with col_fgt:
                    st.markdown("<p style='text-align: right; margin: 0; font-size: 0.8rem;'><a href='#' style='color: #CBD5E1; text-decoration: none;'>Forgot password?</a></p>", unsafe_allow_html=True)

                submitted_signin = st.form_submit_button("Sign In to Portal", use_container_width=True)

                if submitted_signin:
                    if not email or not password:
                        st.error("Please enter both your email address and password.")
                    else:
                        with st.spinner("Verifying credentials with Supabase..."):
                            res = sign_in_staff(email, password)
                            if res.get("success"):
                                st.session_state["authenticated"] = True
                                st.session_state["profile"] = res.get("profile", {})
                                st.rerun()
                            else:
                                st.error(f"Sign in failed: {res.get('message', 'Invalid credentials.')}")

        # TAB 2: CREATE ACCOUNT
        with tab_signup:
            with st.form("signup_form", clear_on_submit=False):
                col_fn, col_ln = st.columns([1, 1])
                with col_fn:
                    fname = st.text_input("First Name", placeholder="Victor", key="signup_fname")
                with col_ln:
                    lname = st.text_input("Last Name", placeholder="Mbanugo", key="signup_lname")

                staffid = st.text_input("Staff ID / Faculty No.", placeholder="CSC-12345", key="signup_staffid")
                dept = st.text_input("Department / Faculty", value="Physical Sciences", key="signup_dept")
                signup_email = st.text_input("Institutional Email", placeholder="victor@university.edu", key="signup_email")

                col_pw1, col_pw2 = st.columns([1, 1])
                with col_pw1:
                    signup_pass = st.text_input("Password", type="password", placeholder="Min 6 characters", key="signup_pass")
                with col_pw2:
                    signup_cpass = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="signup_cpass")

                submitted_signup = st.form_submit_button("Register Staff Account", use_container_width=True)

                if submitted_signup:
                    if not fname or not lname or not staffid or not signup_email or not signup_pass or not signup_cpass:
                        st.error("All fields are required for staff registration.")
                    elif signup_pass != signup_cpass:
                        st.error("Passwords do not match! Please check and re-enter.")
                    elif len(signup_pass) < 6:
                        st.warning("Password must be at least 6 characters long.")
                    else:
                        with st.spinner("Registering credentials in Supabase..."):
                            res = sign_up_staff(
                                email=signup_email,
                                password=signup_pass,
                                first_name=fname,
                                last_name=lname,
                                staff_id=staffid,
                                department=dept
                            )
                            if res.get("success"):
                                sign_in_res = sign_in_staff(signup_email, signup_pass)
                                st.session_state["authenticated"] = True
                                st.session_state["profile"] = sign_in_res.get("profile", {
                                    "full_name": f"{fname} {lname}".strip(),
                                    "role": "Academic Staff",
                                    "department": dept,
                                    "staff_id": staffid
                                })
                                st.rerun()
                            else:
                                st.error(f"Registration failed: {res.get('message', 'Please check inputs.')}")

        st.markdown("</div></div>", unsafe_allow_html=True)
