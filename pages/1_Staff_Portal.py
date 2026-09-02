"""
Staff Portal & Authentication Page for S.A.P.P.M
- Pre-auth: 100% Original Ultra-Premium 3D Perspective Tilt Card with Rotating Laser Border Beam, Staggered Spring Underline Inputs, Password Eye Toggles, and Origin Radial Ripple Button
- Transition: High-End Motion "Bars" Loader (4 kinetic pulsating glowing bars with concise status: "Signing in...")
- Navigation: Parent window location assign (Exact same bulletproof router used in Landing Page)
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
from src.db.prediction_db import save_student_prediction, get_all_prediction_history

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
        overflow-x: hidden !important;
    }

    /* Eliminate Streamlit default block-container max-width and padding — same as landing page */
    .main .block-container {
        max-width: 100% !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin: 0 !important;
    }

    [data-testid="stAppViewBlockContainer"] {
        overflow-x: hidden !important;
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe {
        width: 100% !important;
        border: none !important;
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

    /* Auth-style Underline Input Styling for Student Inputs */
    div[data-testid="stTextInput"] {
        margin-bottom: 6px !important;
    }

    div[data-testid="stTextInput"] label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.78rem !important;
        font-weight: 700 !important;
        color: #94A3B8 !important;
        letter-spacing: 0.06em !important;
        text-transform: uppercase !important;
        margin-bottom: 2px !important;
        transition: color 0.25s ease !important;
    }

    div[data-testid="stTextInput"]:hover label,
    div[data-testid="stTextInput"]:focus-within label {
        color: #FFFFFF !important;
    }

    div[data-testid="stTextInput"] div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 0px !important;
        box-shadow: none !important;
        transition: border-bottom-color 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease !important;
    }

    div[data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
        border-bottom: 2px solid #818CF8 !important;
        box-shadow: 0 4px 15px -3px rgba(129, 140, 248, 0.4) !important;
    }

    div[data-testid="stTextInput"] input {
        background-color: transparent !important;
        color: #FFFFFF !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        padding: 6px 0 8px 0 !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: rgba(148, 163, 184, 0.45) !important;
        font-weight: 400 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Process incoming Supabase Auth requests from query params
auth_action = st.query_params.get("action")

if auth_action in ["signin", "signup"]:
    # Full-screen kinetic Motion "Bars" loader during server-side verification (eliminates blank dark screen)
    status_text = "Authenticating staff session..." if auth_action == "signin" else "Registering staff account..."
    st.markdown(f"""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: #05070E; z-index: 9999999; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="display: flex; gap: 7px; height: 42px; margin-bottom: 20px;">
                <span style="width: 7px; height: 42px; border-radius: 9999px; background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%); animation: authBarsPulsate 1s cubic-bezier(0.42, 0, 0.58, 1) infinite; box-shadow: 0 0 16px rgba(129, 140, 248, 0.8);"></span>
                <span style="width: 7px; height: 42px; border-radius: 9999px; background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%); animation: authBarsPulsate 1s cubic-bezier(0.42, 0, 0.58, 1) 0.12s infinite; box-shadow: 0 0 16px rgba(129, 140, 248, 0.8);"></span>
                <span style="width: 7px; height: 42px; border-radius: 9999px; background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%); animation: authBarsPulsate 1s cubic-bezier(0.42, 0, 0.58, 1) 0.24s infinite; box-shadow: 0 0 16px rgba(129, 140, 248, 0.8);"></span>
                <span style="width: 7px; height: 42px; border-radius: 9999px; background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%); animation: authBarsPulsate 1s cubic-bezier(0.42, 0, 0.58, 1) 0.36s infinite; box-shadow: 0 0 16px rgba(129, 140, 248, 0.8);"></span>
            </div>
            <div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; letter-spacing: -0.02em;">{status_text}</div>
            <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 6px; font-family: 'Plus Jakarta Sans', sans-serif;">Verifying institutional credentials with Supabase...</div>
        </div>
        <style>
            @keyframes authBarsPulsate {{
                0%, 100% {{ transform: scaleY(0.24); opacity: 0.45; }}
                50% {{ transform: scaleY(1.0); opacity: 1; filter: drop-shadow(0 0 12px #38BDF8); }}
            }}
        </style>
    """, unsafe_allow_html=True)

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

@st.cache_resource(show_spinner=False)
def get_ml_pipeline():
    try:
        model = joblib.load("models/random_forest_model.pkl")
        encoder = joblib.load("models/label_encoder.pkl")
        explainer = shap.TreeExplainer(model)
        return model, encoder, explainer, True
    except Exception as e:
        return None, None, None, False

# =========================================================================
# 1. AUTHENTICATED STATE: STUDENT PREDICTOR & HISTORY MANAGEMENT
# =========================================================================
if is_auth:
    # Top navigation bar & clean portal title
    st.markdown("""
        <div style="max-width: 1200px; margin: 0 auto; padding: 24px 32px 10px 32px; display: flex; justify-content: space-between; align-items: center;">
            <a href="/" target="_top" style="font-size: 1.35rem; font-weight: 900; color: #FFFFFF; text-decoration: none;">SAPPM</a>
            <div style="display: flex; gap: 32px;">
                <span style="color: #94A3B8; font-size: 0.92rem; font-weight: 700;">Predictor & Records Portal</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Header banner with staff profile & Sign Out
    col_hdr, col_out = st.columns([4, 1])
    with col_hdr:
        st.markdown(f"""
            <div style="padding: 1rem 0 0.5rem 0;">
                <h1 style="font-size: 2.2rem; font-weight: 900; margin: 0; color: #FFFFFF;">Student Academic Performance Prediction System</h1>
                <p style="color: #94A3B8; font-size: 1rem; margin-top: 0.4rem;">
                    Staff Advisor: <strong style="color: #FFFFFF;">{profile.get('full_name', 'Faculty Staff Member')}</strong> 
                    &nbsp;|&nbsp; Dept: <strong style="color: #818CF8;">{profile.get('department', 'Academic Affairs')}</strong>
                    &nbsp;|&nbsp; Staff ID: <strong style="color: #34D399;">{profile.get('staff_id', 'STF-001')}</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_out:
        st.markdown("<div style='padding-top: 1.5rem;'>", unsafe_allow_html=True)
        if st.button("Sign Out", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["profile"] = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # Clean Navigation Tabs: Performance Predictor & Prediction History
    tab_predict, tab_history = st.tabs(["🔮 Performance Predictor", "📜 Prediction History"])

    with tab_predict:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 14px 20px; margin-bottom: 20px;">
                <p style="margin: 0; color: #CBD5E1; font-size: 0.95rem;">
                    Enter the student's identification details and academic indicators below to generate an ML-backed grade forecast and SHAP explanation.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 1. Student Identification Input Row
        st.markdown("""
            <div style="background: rgba(11, 15, 28, 0.65); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 18px; padding: 18px 24px 14px 24px; margin-bottom: 24px; box-shadow: 0 12px 30px -8px rgba(0, 0, 0, 0.6), inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 12px;">
                    <span style="font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #818CF8; background: rgba(129, 140, 248, 0.12); border: 1px solid rgba(129, 140, 248, 0.3); padding: 3px 10px; border-radius: 9999px;">Step 1</span>
                    <span style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF;">Student Identification</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        col_fn, col_ln, col_reg = st.columns([1, 1, 1])
        with col_fn:
            first_name = st.text_input("First Name", placeholder="e.g. David", key="stu_fname")
        with col_ln:
            last_name = st.text_input("Last Name", placeholder="e.g. Adeleke", key="stu_lname")
        with col_reg:
            reg_no = st.text_input("Registration Number", placeholder="e.g. 2024/CSC/0142", key="stu_regno")

        # Staggered Spring Letter Wave Character Physics (Matches Auth Screen 1:1)
        components.html("""
        <script>
            function attachSpringLetterWave() {
                try {
                    const doc = window.parent.document;
                    if (!doc) return;
                    const textInputs = doc.querySelectorAll('div[data-testid="stTextInput"]');
                    textInputs.forEach(wrapper => {
                        if (wrapper.dataset.springWaveApplied) return;
                        const labelEl = wrapper.querySelector('label p') || wrapper.querySelector('label');
                        const inputEl = wrapper.querySelector('input');
                        if (!labelEl || !inputEl) return;
                        
                        const text = labelEl.textContent.trim();
                        if (!text || text.includes('🔍')) return;
                        
                        wrapper.dataset.springWaveApplied = 'true';
                        wrapper.style.position = 'relative';
                        wrapper.style.paddingTop = '14px';
                        
                        labelEl.innerHTML = '';
                        labelEl.style.position = 'absolute';
                        labelEl.style.top = '16px';
                        labelEl.style.left = '0';
                        labelEl.style.pointerEvents = 'none';
                        labelEl.style.display = 'flex';
                        labelEl.style.color = '#94A3B8';
                        labelEl.style.fontSize = '0.78rem';
                        labelEl.style.fontWeight = '700';
                        labelEl.style.letterSpacing = '0.06em';
                        labelEl.style.textTransform = 'uppercase';
                        
                        text.split('').forEach((char, idx) => {
                            const span = document.createElement('span');
                            span.className = 'letter-wave-char';
                            span.textContent = char === ' ' ? '\u00A0' : char;
                            span.style.display = 'inline-block';
                            span.style.transition = 'transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.25s ease';
                            span.style.transitionDelay = (idx * 0.03) + 's';
                            span.style.willChange = 'transform';
                            labelEl.appendChild(span);
                        });
                        
                        const update = () => {
                            const isActive = (doc.activeElement === inputEl || inputEl.value.trim().length > 0);
                            const spans = labelEl.querySelectorAll('.letter-wave-char');
                            spans.forEach(s => {
                                if (isActive) {
                                    s.style.transform = 'translateY(-22px) scale(0.85)';
                                    s.style.color = '#818CF8';
                                    s.style.fontWeight = '800';
                                } else {
                                    s.style.transform = 'translateY(0px) scale(1)';
                                    s.style.color = '#94A3B8';
                                    s.style.fontWeight = '700';
                                }
                            });
                        };
                        
                        inputEl.addEventListener('focus', update);
                        inputEl.addEventListener('blur', update);
                        inputEl.addEventListener('input', update);
                        update();
                    });
                } catch(e) {}
            }
            setInterval(attachSpringLetterWave, 200);
        </script>
        """, height=0)

        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

        # 2. Academic Sliders & Output Layout
        c_left, c_right = st.columns([1, 1.15], gap="large")

        with c_left:
            st.markdown("<h4 style='font-size: 1.05rem; font-weight: 700; color: #E2E8F0; margin-bottom: 0.8rem;'>2. Academic & Behavioral Indicators</h4>", unsafe_allow_html=True)
            
            study_hours = st.slider(
                "Weekly Self Study Hours",
                min_value=0.0,
                max_value=40.0,
                value=10.0,
                step=0.5,
                help="Average hours the student spends on private self-study per week."
            )

            attendance = st.slider(
                "Attendance Percentage",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                step=1.0,
                help="Overall lecture and lab attendance rate."
            )

            participation = st.slider(
                "Class Participation",
                min_value=0.0,
                max_value=10.0,
                value=5.0,
                step=0.5,
                help="Active engagement rating during classes and seminars (0 to 10 scale)."
            )

            predict_btn = st.button("Predict Grade", type="primary", use_container_width=True)

        with c_right:
            st.markdown("<h4 style='font-size: 1.05rem; font-weight: 700; color: #E2E8F0; margin-bottom: 0.8rem;'>3. Prediction & Explainability Analysis</h4>", unsafe_allow_html=True)

            if predict_btn:
                if not first_name.strip() or not last_name.strip() or not reg_no.strip():
                    st.warning("⚠️ Please fill in the student's **First Name**, **Last Name**, and **Registration Number** before generating a prediction.")
                else:
                    student_full_name = f"{first_name.strip()} {last_name.strip()}"
                    clean_reg_no = reg_no.strip().upper()

                    # Model inference
                    model, encoder, explainer, model_loaded = get_ml_pipeline()
                    if model_loaded and model is not None and encoder is not None and explainer is not None:
                        # Estimate total score continuously from study metrics for the model pipeline
                        derived_score = min(100.0, max(10.0, (attendance * 0.45) + (study_hours * 2.5) + (participation * 2.0)))
                        
                        student_data = pd.DataFrame([{
                            "weekly_self_study_hours": float(study_hours),
                            "attendance_percentage": float(attendance),
                            "class_participation": float(participation),
                            "total_score": float(derived_score)
                        }])

                        prediction = model.predict(student_data)
                        probabilities = model.predict_proba(student_data)
                        predicted_grade = str(encoder.inverse_transform(prediction)[0])
                        confidence = float(probabilities.max() * 100)

                        # Save prediction to database
                        save_student_prediction(
                            student_name=student_full_name,
                            reg_no=clean_reg_no,
                            study_hours=study_hours,
                            attendance=attendance,
                            participation=participation,
                            predicted_grade=predicted_grade,
                            confidence=confidence,
                            predicted_by=profile.get("full_name", "Staff Member")
                        )

                        # Render Results
                        st.success(f"🎯 Predicted Grade for **{student_full_name}** ({clean_reg_no}): **Grade {predicted_grade}**")
                        st.info(f"✨ Prediction Confidence: **{confidence:.2f}%** &nbsp;|&nbsp; 💾 *Saved to Prediction History*")

                        # Probability Chart
                        st.subheader("Grade Prediction Probabilities")
                        grades = encoder.classes_
                        fig, ax = plt.subplots(figsize=(6, 3))
                        fig.patch.set_facecolor('#05070E')
                        ax.set_facecolor('#090D1A')
                        ax.bar(grades, probabilities[0], color='#818CF8', edgecolor='#CBD5E1', alpha=0.9)
                        ax.tick_params(colors='#CBD5E1')
                        ax.set_xlabel("Grades", color='#94A3B8')
                        ax.set_ylabel("Probability", color='#94A3B8')
                        ax.set_title("Prediction Probability Distribution", color='#FFFFFF')
                        for spine in ax.spines.values():
                            spine.set_color('#334155')
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
                            spine.set_color('#334155')
                        st.pyplot(shap_fig)

                        # Feature Importance Section
                        st.subheader("Feature Importance")
                        importance = model.feature_importances_
                        features = ["Study Hours", "Attendance", "Participation", "Total Score"]
                        fig2, ax2 = plt.subplots(figsize=(6, 3))
                        fig2.patch.set_facecolor('#05070E')
                        ax2.set_facecolor('#090D1A')
                        ax2.bar(features, importance, color='#38BDF8', edgecolor='#CBD5E1', alpha=0.9)
                        ax2.tick_params(colors='#CBD5E1')
                        ax2.set_ylabel("Importance", color='#94A3B8')
                        ax2.set_title("Model Feature Importance", color='#FFFFFF')
                        for spine in ax2.spines.values():
                            spine.set_color('#334155')
                        st.pyplot(fig2)
                    else:
                        st.error("ML model files could not be loaded. Please ensure models directory is populated.")
            else:
                st.markdown("""
                    <div style="background: rgba(255, 255, 255, 0.02); border: 1px dashed rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 4rem 2rem; text-align: center; margin-top: 0.5rem;">
                        <div style="display: flex; justify-content: center; margin-bottom: 1.2rem;">
                            <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>
                            </svg>
                        </div>
                        <h3 style="color: #FFFFFF; margin: 0 0 0.5rem 0;">Awaiting Prediction Request</h3>
                        <p style="color: #94A3B8; font-size: 0.92rem; max-width: 380px; margin: 0 auto;">
                            Enter the student's name, reg number, adjust the 3 sliders on the left, and click <strong>Predict Grade</strong> to evaluate performance.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

    # History Review Tab
    with tab_history:
        st.markdown("""
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 14px 20px; margin-bottom: 20px;">
                <p style="margin: 0; color: #CBD5E1; font-size: 0.95rem;">
                    Audit log of all student academic evaluations recorded in the database.
                </p>
            </div>
        """, unsafe_allow_html=True)

        history_records = get_all_prediction_history(limit=150)

        if history_records and len(history_records) > 0:
            # Metric Summary Cards
            total_records = len(history_records)
            grades_list = [r["predicted_grade"] for r in history_records]
            grade_a_count = grades_list.count("A")
            avg_conf = sum(r["confidence"] for r in history_records) / total_records

            m_col1, m_col2, m_col3 = st.columns(3)
            with m_col1:
                st.metric("Total Evaluations Recorded", total_records)
            with m_col2:
                st.metric("Average Confidence", f"{avg_conf:.1f}%")
            with m_col3:
                st.metric("High Performers (Grade A)", grade_a_count)

            st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

            # Search Filter
            search_query = st.text_input("🔍 Search History by Student Name or Reg No", placeholder="e.g. David or CSC", key="history_search")

            filtered_records = history_records
            if search_query.strip():
                q = search_query.strip().lower()
                filtered_records = [
                    r for r in history_records
                    if q in r["student_name"].lower() or q in r["reg_no"].lower()
                ]

            # Format Clean Table
            table_data = []
            for r in filtered_records:
                table_data.append({
                    "Student Name": r["student_name"],
                    "Reg No": r["reg_no"],
                    "Weekly Study Hrs": f"{r['study_hours']:.1f} hrs",
                    "Attendance %": f"{r['attendance']:.0f}%",
                    "Class Participation": f"{r['participation']:.1f} / 10",
                    "Prediction Result": f"Grade {r['predicted_grade']} ({r['confidence']:.1f}%)",
                    "Date Recorded": r["created_at"]
                })

            df_history = pd.DataFrame(table_data)
            st.dataframe(df_history, use_container_width=True, hide_index=True)
        else:
            st.markdown("""
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px dashed rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 4rem 2rem; text-align: center; margin-top: 1rem;">
                    <div style="display: flex; justify-content: center; margin-bottom: 1.2rem;">
                        <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
                        </svg>
                    </div>
                    <h3 style="color: #FFFFFF; margin: 0 0 0.5rem 0;">No Prediction History Found</h3>
                    <p style="color: #94A3B8; font-size: 0.92rem; max-width: 380px; margin: 0 auto;">
                        Evaluations generated in the <strong>Performance Predictor</strong> tab will automatically be logged and displayed here.
                    </p>
                </div>
            """, unsafe_allow_html=True)

# =========================================================================
# 2. UNAUTHENTICATED STATE: 100% ORIGINAL 3D AUTH CARD WITH "BARS" LOADER
# =========================================================================
else:
    # Native Streamlit Back Link
    st.page_link("app.py", label="← Back to Home")

    err_msg_js = f"'{auth_error}'" if auth_error else "null"

    # 21st.dev Cinematic Double-Bezel Auth Screen + Motion "Bars" Loader
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

            /* MOTION BARS LOADER OVERLAY */
            .bars-loader-overlay {{
                display: none;
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border-radius: 26px;
                background: rgba(8, 12, 24, 0.96);
                backdrop-filter: blur(24px);
                -webkit-backdrop-filter: blur(24px);
                z-index: 50;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 30px;
                animation: fadeInOverlay 0.25s ease forwards;
            }}

            @keyframes fadeInOverlay {{
                from {{ opacity: 0; transform: scale(0.96); }}
                to {{ opacity: 1; transform: scale(1); }}
            }}

            .motion-bars-wrap {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 7px;
                height: 42px;
                margin-bottom: 18px;
            }}

            .motion-bar-item {{
                width: 7px;
                height: 42px;
                border-radius: 9999px;
                background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%);
                transform-origin: bottom;
                animation: beuiBarsScale 1s cubic-bezier(0.42, 0, 0.58, 1) infinite;
                box-shadow: 0 0 16px rgba(129, 140, 248, 0.7);
            }}

            .motion-bar-item:nth-child(1) {{ animation-delay: 0s; }}
            .motion-bar-item:nth-child(2) {{ animation-delay: 0.12s; }}
            .motion-bar-item:nth-child(3) {{ animation-delay: 0.24s; }}
            .motion-bar-item:nth-child(4) {{ animation-delay: 0.36s; }}

            @keyframes beuiBarsScale {{
                0%, 100% {{
                    transform: scaleY(0.24);
                    opacity: 0.45;
                }}
                50% {{
                    transform: scaleY(1.0);
                    opacity: 1;
                    filter: drop-shadow(0 0 10px #38BDF8);
                }}
            }}

            .loader-status-title {{
                font-size: 1.15rem;
                font-weight: 800;
                color: #FFFFFF;
                letter-spacing: -0.02em;
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
                    <!-- MOTION BARS FULL-CARD TRANSITION OVERLAY -->
                    <div class="bars-loader-overlay" id="barsLoaderOverlay">
                        <div class="motion-bars-wrap">
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                        </div>
                        <div class="loader-status-title" id="loaderTitle">Signing in...</div>
                    </div>

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

            // 6. MOTION "BARS" LOADER & NATIVE PARENT NAVIGATION ROUTER
            function triggerBarsLoader(title) {{
                const loader = document.getElementById('barsLoaderOverlay');
                document.getElementById('loaderTitle').textContent = title;
                loader.style.display = 'flex';
            }}

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

                    // Show the Motion "Bars" loader
                    triggerBarsLoader('Signing in...');

                    const targetUrl = '/Staff_Portal?action=signin&email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(pass);
                    setTimeout(() => {{
                        try {{
                            if (window.parent && window.parent.location) {{
                                window.parent.location.assign(targetUrl);
                                return;
                            }}
                        }} catch(e) {{}}
                        try {{
                            if (window.top && window.top.location) {{
                                window.top.location.assign(targetUrl);
                                return;
                            }}
                        }} catch(e) {{}}
                        window.location.assign(targetUrl);
                    }}, 500);

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

                    // Show the Motion "Bars" loader
                    triggerBarsLoader('Creating account...');

                    const targetUrl = '/Staff_Portal?action=signup&email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(pass) + '&c_password=' + encodeURIComponent(cpass) + '&fname=' + encodeURIComponent(fname) + '&lname=' + encodeURIComponent(lname) + '&staffid=' + encodeURIComponent(staffid) + '&dept=' + encodeURIComponent(dept);
                    setTimeout(() => {{
                        try {{
                            if (window.parent && window.parent.location) {{
                                window.parent.location.assign(targetUrl);
                                return;
                            }}
                        }} catch(e) {{}}
                        try {{
                            if (window.top && window.top.location) {{
                                window.top.location.assign(targetUrl);
                                return;
                            }}
                        }} catch(e) {{}}
                        window.location.assign(targetUrl);
                    }}, 500);
                }}
            }}
        </script>
    </body>
    </html>
    """

    components.html(auth_component_html, height=920, scrolling=False)
