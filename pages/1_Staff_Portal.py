"""
Staff Portal & Authentication Page for S.A.P.P.M
- Pre-auth: 100% Original Ultra-Premium 3D Perspective Tilt Card with Rotating Laser Border Beam, Staggered Spring Underline Inputs, Password Eye Toggles, and Origin Radial Ripple Button
- Post-auth: The Full Original Student Academic Performance Prediction System (app_3.py architecture with Sliders, Model Inference, Prediction Confidence, Probabilities Distribution Chart, SHAP Attribution, and Feature Importance)
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import streamlit.components.v1 as components
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

# Global Scrollbar & Layout Styling: Hide default sidebar and chrome
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
    </style>
""", unsafe_allow_html=True)

# Process incoming Supabase Auth requests from the 3D Auth Card
auth_action = st.query_params.get("action")

if auth_action == "signin":
    email = st.query_params.get("email", "").strip()
    password = st.query_params.get("password", "")
    
    if email and password:
        res = sign_in_staff(email, password)
        if res.get("success"):
            st.session_state["authenticated"] = True
            st.session_state["profile"] = res.get("profile", {})
            st.session_state["auth_error"] = None
            st.query_params.clear()
            st.rerun()
        else:
            st.session_state["auth_error"] = res.get("message", "Invalid email or password.")
            st.query_params.clear()
            st.rerun()

elif auth_action == "signup":
    email = st.query_params.get("email", "").strip()
    password = st.query_params.get("password", "")
    c_password = st.query_params.get("c_password", "")
    fname = st.query_params.get("fname", "").strip()
    lname = st.query_params.get("lname", "").strip()
    staffid = st.query_params.get("staffid", "").strip()
    dept = st.query_params.get("dept", "Academic Affairs").strip()

    if password != c_password:
        st.session_state["auth_error"] = "Registration failed: Passwords do not match!"
        st.query_params.clear()
        st.rerun()
    elif len(password) < 6:
        st.session_state["auth_error"] = "Registration failed: Password must be at least 6 characters long."
        st.query_params.clear()
        st.rerun()
    else:
        res = sign_up_staff(
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
            staff_id=staffid,
            department=dept
        )
        if res.get("success"):
            sign_in_res = sign_in_staff(email, password)
            st.session_state["authenticated"] = True
            st.session_state["profile"] = sign_in_res.get("profile", {
                "full_name": f"{fname} {lname}".strip(),
                "role": "Academic Staff",
                "department": dept,
                "staff_id": staffid
            })
            st.session_state["auth_error"] = None
            st.query_params.clear()
            st.rerun()
        else:
            st.session_state["auth_error"] = res.get("message", "Registration failed. Please check inputs.")
            st.query_params.clear()
            st.rerun()

is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})
auth_error = st.session_state.get("auth_error", None)

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
            st.query_params.clear()
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
# 2. UNAUTHENTICATED STATE: 100% EXACT ORIGINAL PREMIUM 3D AUTH CARD
# =========================================================================
else:
    # Native Streamlit Back Link
    st.page_link("app.py", label="← Back to Home")

    err_msg_js = f"'{auth_error}'" if auth_error else "null"

    # 21st.dev Cinematic Double-Bezel Auth Screen
    auth_component_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
                user-select: none;
            }}

            body {{
                background-color: #05070E;
                color: #FFFFFF;
                width: 100%;
                min-height: 100vh;
                overflow-x: hidden;
                position: relative;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding-top: 2rem;
            }}

            /* Ambient Glow Backgrounds */
            .ambient-top {{
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 100vw;
                height: 500px;
                background: radial-gradient(circle, rgba(139, 92, 246, 0.22) 0%, rgba(99, 102, 241, 0.12) 40%, transparent 75%);
                filter: blur(80px);
                pointer-events: none;
                z-index: 1;
            }}

            .ambient-bottom {{
                position: absolute;
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 90vw;
                height: 350px;
                background: radial-gradient(circle, rgba(56, 189, 248, 0.1) 0%, transparent 70%);
                filter: blur(80px);
                pointer-events: none;
                z-index: 1;
            }}

            /* 3D PERSPECTIVE TILT CARD */
            .card-perspective-container {{
                perspective: 1500px;
                width: 100%;
                max-width: 480px;
                margin: 0 auto;
                position: relative;
                z-index: 10;
            }}

            .tilt-card-wrapper {{
                position: relative;
                border-radius: 28px;
                padding: 2px;
                overflow: hidden;
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85);
                transform-style: preserve-3d;
                transition: transform 0.12s ease-out;
            }}

            .tilt-card-wrapper::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: conic-gradient(
                    transparent,
                    transparent 65%,
                    rgba(255, 255, 255, 0.9) 85%,
                    #818CF8 95%,
                    transparent
                );
                animation: rotateBorderBeam 4s linear infinite;
                z-index: 1;
            }}

            @keyframes rotateBorderBeam {{
                0% {{ transform: rotate(0deg); }}
                100% {{ transform: rotate(360deg); }}
            }}

            .tilt-card {{
                position: relative;
                z-index: 2;
                border-radius: 26px;
                background: rgba(11, 15, 28, 0.9);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                padding: 34px 38px;
            }}

            .card-emblem {{
                width: 46px;
                height: 46px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.15);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 14px auto;
                font-weight: 900;
                font-size: 1.25rem;
                color: #FFFFFF;
                box-shadow: 0 0 25px rgba(139, 92, 246, 0.4);
            }}

            .card-header-title {{
                text-align: center;
                font-size: 1.65rem;
                font-weight: 900;
                letter-spacing: -0.03em;
                color: #FFFFFF;
                margin-bottom: 4px;
            }}

            .card-header-sub {{
                text-align: center;
                font-size: 0.85rem;
                color: #94A3B8;
                margin-bottom: 18px;
            }}

            /* Error alert container */
            .auth-error-banner {{
                display: none;
                background: rgba(239, 68, 68, 0.15);
                border: 1px solid rgba(239, 68, 68, 0.4);
                border-radius: 12px;
                padding: 10px 14px;
                color: #F87171;
                font-size: 0.82rem;
                font-weight: 600;
                margin-bottom: 18px;
                text-align: center;
                animation: shakeAlert 0.35s ease;
            }}

            @keyframes shakeAlert {{
                0%, 100% {{ transform: translateX(0); }}
                20%, 60% {{ transform: translateX(-6px); }}
                40%, 80% {{ transform: translateX(6px); }}
            }}

            .auth-toggle-bar {{
                display: flex;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 9999px;
                padding: 4px;
                margin-bottom: 24px;
            }}

            .toggle-btn {{
                flex: 1;
                text-align: center;
                padding: 8px 16px;
                border-radius: 9999px;
                font-size: 0.85rem;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.25s ease;
                color: #94A3B8;
            }}

            .toggle-btn.active {{
                background: #FFFFFF;
                color: #05070E;
                box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
            }}

            .auth-form-animated {{
                animation: smoothFormSlide 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            }}

            @keyframes smoothFormSlide {{
                from {{
                    opacity: 0;
                    transform: translateY(10px) scale(0.98);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }}
            }}

            /* Staggered Spring Underline Inputs */
            .input-underline-group {{
                position: relative;
                width: 100%;
                margin-bottom: 22px;
                padding-top: 14px;
            }}

            .input-group-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px;
            }}

            .floating-letters-wrapper {{
                position: absolute;
                top: 18px;
                left: 0;
                pointer-events: none;
                display: flex;
                color: #94A3B8;
                font-size: 0.92rem;
                font-weight: 500;
            }}

            .letter-wave-char {{
                display: inline-block;
                transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.25s ease;
                will-change: transform;
            }}

            .underline-field {{
                width: 100%;
                background: transparent;
                border: none;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
                padding: 6px 0 8px 0;
                color: #FFFFFF;
                font-size: 0.95rem;
                font-weight: 500;
                outline: none;
                transition: border-bottom-color 0.3s ease;
            }}

            .underline-field:focus {{
                border-bottom-color: #FFFFFF;
            }}

            .input-underline-group.is-active .letter-wave-char {{
                transform: translateY(-22px) scale(0.85);
                color: #E2E8F0;
                font-weight: 700;
            }}

            .password-toggle-btn {{
                position: absolute;
                right: 0;
                bottom: 8px;
                cursor: pointer;
                color: #94A3B8;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: color 0.2s ease, transform 0.2s ease;
            }}
            .password-toggle-btn:hover {{
                color: #FFFFFF;
                transform: scale(1.1);
            }}
            .password-toggle-btn svg {{
                width: 18px;
                height: 18px;
                stroke: currentColor;
                transition: all 0.25s ease;
            }}

            .origin-submit-btn {{
                width: 100%;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 13px 28px;
                border-radius: 9999px;
                background: #FFFFFF;
                color: #05070E;
                font-size: 0.95rem;
                font-weight: 800;
                border: 1px solid rgba(255, 255, 255, 0.5);
                cursor: pointer;
                overflow: hidden;
                margin-top: 12px;
                animation: authBtnBreathingShadow 3s ease-in-out infinite alternate;
                transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), color 0.3s ease;
            }}

            @keyframes authBtnBreathingShadow {{
                0% {{
                    box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.25), 0 0 15px 2px rgba(99, 102, 241, 0.25);
                }}
                50% {{
                    box-shadow: 0 16px 35px -2px rgba(255, 255, 255, 0.45), 0 0 25px 5px rgba(56, 189, 248, 0.45);
                }}
                100% {{
                    box-shadow: 0 12px 30px -4px rgba(255, 255, 255, 0.3), 0 0 18px 3px rgba(99, 102, 241, 0.35);
                }}
            }}

            .origin-submit-btn:hover {{
                transform: translateY(-2px) scale(1.01);
                animation: none;
                box-shadow: 0 18px 45px rgba(255, 255, 255, 0.45), 0 0 30px rgba(56, 189, 248, 0.5);
            }}

            .origin-submit-btn .origin-ripple {{
                position: absolute;
                border-radius: 50%;
                background: #05070E;
                transform: translate(-50%, -50%) scale(0);
                pointer-events: none;
                transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 1;
            }}

            .origin-submit-btn.active .origin-ripple {{
                transform: translate(-50%, -50%) scale(1);
            }}

            .origin-submit-btn .button-label {{
                position: relative;
                z-index: 2;
                display: inline-flex;
                align-items: center;
                gap: 10px;
                transition: color 0.3s ease;
            }}
            .origin-submit-btn.active .button-label {{
                color: #FFFFFF;
            }}

            .kinetic-vector-arrow {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }}
            .origin-submit-btn:hover .kinetic-vector-arrow {{
                transform: translateX(5px);
                animation: arrowKineticPulse 1.2s ease-in-out infinite alternate;
            }}

            @keyframes arrowKineticPulse {{
                0% {{ transform: translateX(4px); }}
                100% {{ transform: translateX(8px); }}
            }}

            .footer-links {{
                text-align: center;
                margin-top: 18px;
                font-size: 0.82rem;
                color: #64748B;
            }}
            .footer-links a {{
                color: #CBD5E1;
                text-decoration: none;
                font-weight: 700;
            }}
        </style>
    </head>
    <body>
        <div class="ambient-top"></div>
        <div class="ambient-bottom"></div>

        <!-- 3D Perspective Tilt Card with Continuous 360deg Laser Border Beam -->
        <div class="card-perspective-container">
            <div class="tilt-card-wrapper" id="tiltCardWrapper">
                <div class="tilt-card">
                    <!-- Emblem Header -->
                    <div class="card-emblem">S</div>
                    <h2 class="card-header-title" id="formTitle">Welcome Back</h2>
                    <p class="card-header-sub" id="formSub">Sign in to access student prediction analytics</p>

                    <!-- Error Alert Banner -->
                    <div class="auth-error-banner" id="errorBanner"></div>

                    <!-- Toggle Pills -->
                    <div class="auth-toggle-bar">
                        <div class="toggle-btn active" id="tabSignIn" onclick="switchTab('signin')">Sign In</div>
                        <div class="toggle-btn" id="tabSignUp" onclick="switchTab('signup')">Create Account</div>
                    </div>

                    <!-- SIGN IN FORM -->
                    <form id="signInForm" class="auth-form-animated" onsubmit="handleAuthAction(event, 'signin')">
                        <div class="input-underline-group" id="grp_login_email">
                            <div class="floating-letters-wrapper" id="lbl_login_email"></div>
                            <input type="email" class="underline-field" id="login_email" autocomplete="off" required />
                        </div>

                        <div class="input-underline-group" id="grp_login_password">
                            <div class="floating-letters-wrapper" id="lbl_login_password"></div>
                            <input type="password" class="underline-field" id="login_password" autocomplete="off" required />
                            <div class="password-toggle-btn" onclick="togglePasswordEye('login_password', this)">
                                <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                                    <line x1="1" y1="1" x2="23" y2="23"></line>
                                </svg>
                            </div>
                        </div>

                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 0.8rem; color: #94A3B8;">
                            <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                                <input type="checkbox" style="accent-color: #818CF8;" /> Remember me
                            </label>
                            <a href="#" style="color: #CBD5E1; text-decoration: none;">Forgot password?</a>
                        </div>

                        <!-- ORIGIN BUTTON 1 WITH KINETIC VECTOR ARROW -->
                        <button type="submit" class="origin-submit-btn" id="btnSignInOrigin">
                            <div class="origin-ripple"></div>
                            <span class="button-label">
                                <span>Sign In to Portal</span>
                                <span class="kinetic-vector-arrow">
                                    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                        <line x1="5" y1="12" x2="19" y2="12"></line>
                                        <polyline points="12 5 19 12 12 19"></polyline>
                                    </svg>
                                </span>
                            </span>
                        </button>
                    </form>

                    <!-- SIGN UP FORM -->
                    <form id="signUpForm" class="auth-form-animated" style="display: none;" onsubmit="handleAuthAction(event, 'signup')">
                        <div class="input-group-grid">
                            <div class="input-underline-group" id="grp_signup_fname">
                                <div class="floating-letters-wrapper" id="lbl_signup_fname"></div>
                                <input type="text" class="underline-field" id="signup_fname" autocomplete="off" required />
                            </div>
                            <div class="input-underline-group" id="grp_signup_lname">
                                <div class="floating-letters-wrapper" id="lbl_signup_lname"></div>
                                <input type="text" class="underline-field" id="signup_lname" autocomplete="off" required />
                            </div>
                        </div>

                        <div class="input-underline-group" id="grp_signup_staffid">
                            <div class="floating-letters-wrapper" id="lbl_signup_staffid"></div>
                            <input type="text" class="underline-field" id="signup_staffid" autocomplete="off" required />
                        </div>

                        <div class="input-underline-group" id="grp_signup_dept">
                            <div class="floating-letters-wrapper" id="lbl_signup_dept"></div>
                            <input type="text" class="underline-field" id="signup_dept" autocomplete="off" required />
                        </div>

                        <div class="input-underline-group" id="grp_signup_email">
                            <div class="floating-letters-wrapper" id="lbl_signup_email"></div>
                            <input type="email" class="underline-field" id="signup_email" autocomplete="off" required />
                        </div>

                        <div class="input-group-grid">
                            <div class="input-underline-group" id="grp_signup_pass">
                                <div class="floating-letters-wrapper" id="lbl_signup_pass"></div>
                                <input type="password" class="underline-field" id="signup_pass" autocomplete="off" required />
                                <div class="password-toggle-btn" onclick="togglePasswordEye('signup_pass', this)">
                                    <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                                        <line x1="1" y1="1" x2="23" y2="23"></line>
                                    </svg>
                                </div>
                            </div>
                            <div class="input-underline-group" id="grp_signup_cpass">
                                <div class="floating-letters-wrapper" id="lbl_signup_cpass"></div>
                                <input type="password" class="underline-field" id="signup_cpass" autocomplete="off" required />
                                <div class="password-toggle-btn" onclick="togglePasswordEye('signup_cpass', this)">
                                    <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                        <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                                        <line x1="1" y1="1" x2="23" y2="23"></line>
                                    </svg>
                                </div>
                            </div>
                        </div>

                        <!-- ORIGIN BUTTON 1 WITH KINETIC VECTOR ARROW -->
                        <button type="submit" class="origin-submit-btn" id="btnSignUpOrigin">
                            <div class="origin-ripple"></div>
                            <span class="button-label">
                                <span>Register Staff Account</span>
                                <span class="kinetic-vector-arrow">
                                    <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                        <line x1="5" y1="12" x2="19" y2="12"></line>
                                        <polyline points="12 5 19 12 12 19"></polyline>
                                    </svg>
                                </span>
                            </span>
                        </button>
                    </form>

                    <div class="footer-links" id="footerToggleText">
                        Don't have an account? <a href="javascript:switchTab('signup')">Sign up</a>
                    </div>
                </div>
            </div>
        </div>

        <script>
            const serverError = {err_msg_js};
            const errorBanner = document.getElementById('errorBanner');
            if (serverError) {{
                errorBanner.textContent = serverError;
                errorBanner.style.display = 'block';
            }}

            function showError(msg) {{
                errorBanner.textContent = msg;
                errorBanner.style.display = 'block';
                errorBanner.classList.remove('auth-error-banner');
                void errorBanner.offsetWidth;
                errorBanner.classList.add('auth-error-banner');
            }}

            function hideError() {{
                errorBanner.style.display = 'none';
            }}

            // 1. 3D Perspective Mouse Tilt Physics
            const tiltCardWrapper = document.getElementById('tiltCardWrapper');
            document.addEventListener('mousemove', (e) => {{
                const rect = tiltCardWrapper.getBoundingClientRect();
                const cardX = rect.left + rect.width / 2;
                const cardY = rect.top + rect.height / 2;
                const mouseX = e.clientX - cardX;
                const mouseY = e.clientY - cardY;

                const rotateX = -(mouseY / (window.innerHeight / 2)) * 6;
                const rotateY = (mouseX / (window.innerWidth / 2)) * 6;

                tiltCardWrapper.style.transform = `rotateX(${{rotateX}}deg) rotateY(${{rotateY}}deg)`;
            }});

            document.addEventListener('mouseleave', () => {{
                tiltCardWrapper.style.transform = 'rotateX(0deg) rotateY(0deg)';
            }});

            // 2. Setup Staggered Spring Letter Wave for Underline Inputs
            const setupSpringLetterWave = (inputId, labelId, labelText) => {{
                const input = document.getElementById(inputId);
                const labelContainer = document.getElementById(labelId);
                const group = input.parentElement;

                if (!input || !labelContainer) return;

                labelContainer.innerHTML = '';
                labelText.split('').forEach((char, idx) => {{
                    const span = document.createElement('span');
                    span.className = 'letter-wave-char';
                    span.textContent = char === ' ' ? '\\u00A0' : char;
                    span.style.transitionDelay = `${{idx * 0.03}}s`;
                    labelContainer.appendChild(span);
                }});

                const updateWaveState = () => {{
                    if (document.activeElement === input || input.value.trim().length > 0) {{
                        group.classList.add('is-active');
                    }} else {{
                        group.classList.remove('is-active');
                    }}
                }};

                input.addEventListener('focus', updateWaveState);
                input.addEventListener('blur', updateWaveState);
                input.addEventListener('input', updateWaveState);
            }};

            // Initialize all labels
            setupSpringLetterWave('login_email', 'lbl_login_email', 'Email Address');
            setupSpringLetterWave('login_password', 'lbl_login_password', 'Password');
            setupSpringLetterWave('signup_fname', 'lbl_signup_fname', 'First Name');
            setupSpringLetterWave('signup_lname', 'lbl_signup_lname', 'Last Name');
            setupSpringLetterWave('signup_staffid', 'lbl_signup_staffid', 'Staff ID / Faculty No.');
            setupSpringLetterWave('signup_dept', 'lbl_signup_dept', 'Department / Faculty');
            setupSpringLetterWave('signup_email', 'lbl_signup_email', 'Institutional Email');
            setupSpringLetterWave('signup_pass', 'lbl_signup_pass', 'Password');
            setupSpringLetterWave('signup_cpass', 'lbl_signup_cpass', 'Confirm Password');

            // 3. Smooth Tab Switching
            function switchTab(tab) {{
                hideError();
                const signInForm = document.getElementById('signInForm');
                const signUpForm = document.getElementById('signUpForm');
                const tabSignIn = document.getElementById('tabSignIn');
                const tabSignUp = document.getElementById('tabSignUp');
                const formTitle = document.getElementById('formTitle');
                const formSub = document.getElementById('formSub');
                const footerToggleText = document.getElementById('footerToggleText');

                if (tab === 'signup') {{
                    tabSignIn.classList.remove('active');
                    tabSignUp.classList.add('active');
                    signInForm.style.display = 'none';
                    signUpForm.style.display = 'block';
                    signUpForm.classList.remove('auth-form-animated');
                    void signUpForm.offsetWidth;
                    signUpForm.classList.add('auth-form-animated');
                    formTitle.textContent = 'Create Staff Account';
                    formSub.textContent = 'Register your institutional credentials for access';
                    footerToggleText.innerHTML = 'Already have an account? <a href="javascript:switchTab(\\'signin\\')">Sign in</a>';
                }} else {{
                    tabSignUp.classList.remove('active');
                    tabSignIn.classList.add('active');
                    signUpForm.style.display = 'none';
                    signInForm.style.display = 'block';
                    signInForm.classList.remove('auth-form-animated');
                    void signInForm.offsetWidth;
                    signInForm.classList.add('auth-form-animated');
                    formTitle.textContent = 'Welcome Back';
                    formSub.textContent = 'Sign in to access student prediction analytics';
                    footerToggleText.innerHTML = 'Don\\'t have an account? <a href="javascript:switchTab(\\'signup\\')">Sign up</a>';
                }}
            }}

            // 4. Animated Watch / Watch-Off Eye Toggle Logic
            function togglePasswordEye(id, containerEl) {{
                const input = document.getElementById(id);
                if (!input) return;

                if (input.type === 'password') {{
                    input.type = 'text';
                    containerEl.innerHTML = `
                        <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                    `;
                }} else {{
                    input.type = 'password';
                    containerEl.innerHTML = `
                        <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                            <line x1="1" y1="1" x2="23" y2="23"></line>
                        </svg>
                    `;
                }}
            }}

            // 5. Origin Button Radial Ripple Physics
            const attachOriginRipple = (btnId) => {{
                const btn = document.getElementById(btnId);
                if (!btn) return;
                const ripple = btn.querySelector('.origin-ripple');

                btn.addEventListener('mouseenter', (e) => {{
                    const rect = btn.getBoundingClientRect();
                    const x = e.clientX - rect.left;
                    const y = e.clientY - rect.top;
                    
                    const diameter = Math.ceil(
                        2 * Math.max(
                            Math.hypot(x, y),
                            Math.hypot(rect.width - x, y),
                            Math.hypot(x, rect.height - y),
                            Math.hypot(rect.width - x, rect.height - y)
                        )
                    );

                    ripple.style.left = `${{x}}px`;
                    ripple.style.top = `${{y}}px`;
                    ripple.style.width = `${{diameter}}px`;
                    ripple.style.height = `${{diameter}}px`;
                    btn.classList.add('active');
                }});

                btn.addEventListener('mouseleave', () => {{
                    btn.classList.remove('active');
                }});
            }};

            attachOriginRipple('btnSignInOrigin');
            attachOriginRipple('btnSignUpOrigin');

            // 6. Direct Top-Window Navigation
            function handleAuthAction(event, action) {{
                event.preventDefault();
                hideError();

                if (action === 'signin') {{
                    const email = document.getElementById('login_email').value.trim();
                    const pass = document.getElementById('login_password').value;

                    if (!email || !pass) {{
                        showError('Please enter both your email address and password.');
                        return;
                    }}

                    const btn = document.getElementById('btnSignInOrigin');
                    const label = btn.querySelector('.button-label');
                    label.innerHTML = '<span>Verifying credentials...</span>';

                    const targetUrl = `/Staff_Portal?action=signin&email=${{encodeURIComponent(email)}}&password=${{encodeURIComponent(pass)}}`;
                    try {{
                        window.top.location.href = targetUrl;
                    }} catch(e) {{
                        try {{
                            window.parent.location.href = targetUrl;
                        }} catch(err) {{
                            window.location.href = targetUrl;
                        }}
                    }}

                }} else if (action === 'signup') {{
                    const fname = document.getElementById('signup_fname').value.trim();
                    const lname = document.getElementById('signup_lname').value.trim();
                    const staffid = document.getElementById('signup_staffid').value.trim();
                    const dept = document.getElementById('signup_dept').value.trim();
                    const email = document.getElementById('signup_email').value.trim();
                    const pass = document.getElementById('signup_pass').value;
                    const cpass = document.getElementById('signup_cpass').value;

                    if (!fname || !lname || !staffid || !dept || !email || !pass || !cpass) {{
                        showError('All fields are required for staff registration.');
                        return;
                    }}

                    if (pass !== cpass) {{
                        showError('Passwords do not match! Please check and re-enter.');
                        return;
                    }}

                    if (pass.length < 6) {{
                        showError('Password must be at least 6 characters long.');
                        return;
                    }}

                    const btn = document.getElementById('btnSignUpOrigin');
                    const label = btn.querySelector('.button-label');
                    label.innerHTML = '<span>Registering credentials...</span>';

                    const targetUrl = `/Staff_Portal?action=signup&email=${{encodeURIComponent(email)}}&password=${{encodeURIComponent(pass)}}&c_password=${{encodeURIComponent(cpass)}}&fname=${{encodeURIComponent(fname)}}&lname=${{encodeURIComponent(lname)}}&staffid=${{encodeURIComponent(staffid)}}&dept=${{encodeURIComponent(dept)}}`;
                    try {{
                        window.top.location.href = targetUrl;
                    }} catch(e) {{
                        try {{
                            window.parent.location.href = targetUrl;
                        }} catch(err) {{
                            window.location.href = targetUrl;
                        }}
                    }}
                }}
            }}
        </script>
    </body>
    </html>
    """

    components.html(auth_component_html, height=920, scrolling=False)
