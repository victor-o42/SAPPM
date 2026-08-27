"""
Staff Portal & Authentication Page for S.A.P.P.M
Dedicated route for staff member login, registration, and session management.
"""

import streamlit as st
from src.ui.styles import apply_global_styles
from src.ui.auth_ui import render_auth_modal
from src.auth import sign_out_staff

st.set_page_config(
    page_title="Staff Portal - S.A.P.P.M",
    page_icon="🔐",
    layout="wide"
)

apply_global_styles()

is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})

if is_auth:
    st.markdown('<div class="hero-container" style="padding-top: 1rem;">', unsafe_allow_html=True)
    st.markdown('<span class="hero-eyebrow">Verified Active Session</span>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="hero-headline">Welcome, {profile.get("full_name", "Staff Member")}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="hero-lead">Staff ID: <strong style="color:#60A5FA;">{profile.get("staff_id", "N/A")}</strong> &nbsp;|&nbsp; Role: <strong style="color:#34D399;">{profile.get("role", "Academic Advisor")}</strong> &nbsp;|&nbsp; Department: <strong style="color:#A78BFA;">{profile.get("department", "Academic Affairs")}</strong></p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown("""
            <div class="bezel-shell">
                <div class="bezel-core" style="text-align: center;">
                    <div style="font-size: 0.75rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.25rem;">Management Console</div>
                    <h3 style="margin: 0 0 1rem 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Academic Control Center</h3>
                    <p style="color: #94A3B8; font-size: 0.92rem; margin-bottom: 1.5rem;">You have active privileges to evaluate students, inspect SHAP factors, and export records.</p>
        """, unsafe_allow_html=True)
        
        bcol1, bcol2 = st.columns(2)
        with bcol1:
            if st.button("🔮 Launch Predictor", use_container_width=True, type="primary"):
                st.switch_page("pages/2_🔮_Predict.py")
        with bcol2:
            if st.button("🗄️ Browse Records", use_container_width=True):
                st.switch_page("pages/5_🗄️_Student_Records.py")
                
        st.markdown("<hr style='margin: 1.5rem 0;'>", unsafe_allow_html=True)
        if st.button("🚪 Sign Out of Portal", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["user"] = None
            st.session_state["profile"] = None
            st.rerun()
        st.markdown('</div></div>', unsafe_allow_html=True)

else:
    render_auth_modal()
