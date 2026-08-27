"""
Modern Authentication UI Component
Renders responsive login and signup cards for staff members with form validation.
"""

import streamlit as st
from src.auth import sign_in_staff, sign_up_staff
from src.ui.icons import icon

def render_auth_modal():
    """
    Renders the staff login & registration portal with Double-Bezel styling and SVG icons.
    """
    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        st.markdown(f"""
            <div class="bezel-shell">
                <div class="bezel-core">
                    <div style="text-align: center; margin-bottom: 1.5rem;">
                        <span class="hero-eyebrow" style="margin-bottom: 0.85rem;">{icon("lock", size=14, color="#A5B4FC")} &nbsp;Institutional Access</span>
                        <h2 style="font-size: 1.8rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em; margin: 0 0 0.4rem 0;">Staff Portal</h2>
                        <p style="font-size: 0.95rem; color: #94A3B8; margin: 0;">Sign in or register to access the prediction system & student records.</p>
                    </div>
        """, unsafe_allow_html=True)

        tab_login, tab_signup = st.tabs(["Sign In", "Create Staff Account"])

        # Sign In Tab
        with tab_login:
            with st.form("login_form", clear_on_submit=False):
                email = st.text_input("Institutional Email", placeholder="staff@university.edu", key="login_email")
                password = st.text_input("Password", type="password", placeholder="••••••••••••", key="login_password")
                
                submitted = st.form_submit_button("Sign In to Portal", use_container_width=True)
                
                if submitted:
                    if not email or not password:
                        st.error("Please enter both email and password.")
                    else:
                        with st.spinner("Verifying credentials..."):
                            res = sign_in_staff(email, password)
                            if res["success"]:
                                st.session_state["authenticated"] = True
                                st.session_state["user"] = res["user"]
                                st.session_state["profile"] = res["profile"]
                                st.success(res["message"])
                                st.rerun()
                            else:
                                st.error(f"Sign in failed: {res['message']}")

        # Sign Up Tab
        with tab_signup:
            with st.form("signup_form", clear_on_submit=False):
                full_name = st.text_input("Full Name", placeholder="e.g. Dr. Jane Smith", key="signup_name")
                staff_id = st.text_input("Staff ID / Faculty Number", placeholder="e.g. STF-2026-1042 (or any test ID)", key="signup_staff_id")
                department = st.text_input("Department / Unit", value="Academic Affairs & Student Guidance", key="signup_dept")
                email = st.text_input("Email Address", placeholder="jane.smith@university.edu", key="signup_email")
                password = st.text_input("Create Password", type="password", placeholder="Min 6 characters", key="signup_password")
                confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="signup_confirm_password")

                submitted_signup = st.form_submit_button("Register Staff Account", use_container_width=True)

                if submitted_signup:
                    if not full_name or not staff_id or not email or not password:
                        st.error("Please fill in all required fields.")
                    elif len(password) < 6:
                        st.warning("Password must be at least 6 characters.")
                    elif password != confirm_password:
                        st.error("Passwords do not match.")
                    else:
                        with st.spinner("Creating staff account..."):
                            res = sign_up_staff(
                                email=email,
                                password=password,
                                full_name=full_name,
                                staff_id=staff_id,
                                department=department
                            )
                            if res["success"]:
                                st.success("Account created successfully! You can now sign in.")
                            else:
                                st.error(f"Registration failed: {res['message']}")

        st.markdown('</div></div>', unsafe_allow_html=True)
