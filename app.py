"""
Main Application Entrypoint for S.A.P.P.M
Handles user authentication state, global styling, staff profile header,
and navigation routing across pages.
"""

import streamlit as st
from src.ui.styles import apply_global_styles
from src.ui.auth_ui import render_auth_modal
from src.auth import sign_out_staff

st.set_page_config(
    page_title="S.A.P.P.M - Student Academic Performance Prediction Model",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply our design system styles
apply_global_styles()

# Check authentication state in session
is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})

# Top Navigation Bar / User Profile Status
if is_auth:
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 1rem;">
                <div style="background: rgba(59, 130, 246, 0.15); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 8px; padding: 6px 12px; color: #60A5FA; font-weight: 700; font-size: 0.85rem;">
                    STAFF PORTAL
                </div>
                <div style="color: #F8FAFC; font-weight: 600; font-size: 0.95rem;">
                    👤 {profile.get('full_name', 'Staff Member')} <span style="color: #94A3B8; font-weight: 400;">({profile.get('staff_id', 'STF-01')})</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with header_col2:
        if st.button("🚪 Sign Out", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["user"] = None
            st.session_state["profile"] = None
            st.rerun()

# If user is not signed in, show welcome hero and login/signup card
if not is_auth:
    st.markdown("""
        <div class="hero-container">
            <span class="hero-badge">Institutional Machine Learning System</span>
            <h1 class="hero-title">Student Academic Performance<br>Prediction Model (S.A.P.P.M)</h1>
            <p class="hero-subtitle">
                An intelligent academic decision-support platform designed to predict student grade outcomes,
                detect at-risk learners early, and deliver actionable insights with Explainable AI.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Render Staff Login / Signup Form
    render_auth_modal()

    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Overview Cards below the login card
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #60A5FA;">1,000,000</div>
                <div class="stat-label">Trained Dataset Records</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #34D399;">99.81%</div>
                <div class="stat-label">Prediction Accuracy</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #FBBF24;">PostgreSQL</div>
                <div class="stat-label">Cloud Database (Supabase)</div>
            </div>
        """, unsafe_allow_html=True)

else:
    # When signed in, present the Dashboard Home
    st.markdown("""
        <div class="hero-container" style="padding-top: 1rem;">
            <h1 class="hero-title">Welcome to the S.A.P.P.M Portal</h1>
            <p class="hero-subtitle">
                Select an action below or use the sidebar navigation to run predictions,
                view SHAP explainability charts, or inspect historical records.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #60A5FA;">1,000,000</div>
                <div class="stat-label">Trained Records</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #34D399;">99.81%</div>
                <div class="stat-label">XGBoost Accuracy</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #A78BFA;">4 Features</div>
                <div class="stat-label">Core Predictors</div>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="stat-card">
                <div class="stat-value" style="color: #FBBF24;">Active</div>
                <div class="stat-label">Supabase Sync</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Action Cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
            <div class="glass-card">
                <h3 style="color: #60A5FA; margin-top:0;">🔮 Run Prediction</h3>
                <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                    Input a student's study hours, attendance, and scores to get an instant predicted grade, risk assessment, and recommendation.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Predictor", key="btn_pred", use_container_width=True):
            st.switch_page("pages/2_🔮_Predict.py")

    with c2:
        st.markdown("""
            <div class="glass-card">
                <h3 style="color: #34D399; margin-top:0;">📈 Model Benchmarks</h3>
                <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                    Compare evaluation metrics across XGBoost, Random Forest, and Logistic Regression algorithms stored in Supabase.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Benchmarks", key="btn_bench", use_container_width=True):
            st.switch_page("pages/4_📈_Model_Analytics.py")

    with c3:
        st.markdown("""
            <div class="glass-card">
                <h3 style="color: #F472B6; margin-top:0;">🗄️ Student Records</h3>
                <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                    Search, filter, inspect, and export historical student predictions and risk levels logged to the cloud database.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Browse Records", key="btn_recs", use_container_width=True):
            st.switch_page("pages/5_🗄️_Student_Records.py")