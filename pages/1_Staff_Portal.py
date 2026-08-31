"""
Staff Portal & Authentication Page for S.A.P.P.M
Engineered to 21st.dev Premium Standards:
- Bulletproof navTo top router for instant, smooth page switching
- Ultra-premium 21st.dev Double-Bezel Glass Back Button with kinetic sliding chevron arrow
- 3D Perspective Tilt Card with continuous 360° circulating laser border beam
- Staggered Spring Letter-Wave Underline Inputs (Zinc/Off-white)
- Origin Button (Button 1 Style) with kinetic sliding vector arrow
- Animated Watch / Watch-Off Eye Toggle
- Full Supabase Auth integration
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import streamlit.components.v1 as components
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

    /* Clean Scrollbar Styling */
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

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    iframe {
        width: 100% !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# Active session management
is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})

if is_auth:
    st.markdown("""
        <div style="max-width: 1200px; margin: 0 auto; padding: 24px 32px 10px 32px; display: flex; justify-content: space-between; align-items: center;">
            <a href="/" target="_top" style="font-size: 1.35rem; font-weight: 900; color: #FFFFFF; text-decoration: none;">SAPPM</a>
            <div style="display: flex; gap: 32px;">
                <a href="/Predict" target="_top" style="color: #94A3B8; font-size: 0.92rem; font-weight: 500; text-decoration: none;">Predict</a>
                <a href="/Explainability" target="_top" style="color: #94A3B8; font-size: 0.92rem; font-weight: 500; text-decoration: none;">Explainability</a>
                <a href="/Model_Analytics" target="_top" style="color: #94A3B8; font-size: 0.92rem; font-weight: 500; text-decoration: none;">Analytics</a>
                <a href="/Student_Records" target="_top" style="color: #94A3B8; font-size: 0.92rem; font-weight: 500; text-decoration: none;">Records</a>
            </div>
            <div>
                <span style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 9999px; color: #34D399; font-size: 0.8rem; font-weight: 700;">● Active Session</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="max-width: 800px; margin: 4rem auto; padding: 0 1.5rem; text-align: center;">
            <div style="background: rgba(18, 24, 40, 0.6); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 28px; padding: 3rem; backdrop-filter: blur(20px); box-shadow: 0 25px 60px -15px rgba(0,0,0,0.7);">
                <div style="font-size: 0.8rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">Verified Staff Session</div>
                <h1 style="font-size: 2.4rem; font-weight: 900; color: #FFFFFF; margin: 0 0 0.5rem 0;">Welcome, {profile.get("full_name", "Staff Member")}</h1>
                <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 2rem;">
                    Staff ID: <strong style="color: #60A5FA;">{profile.get("staff_id", "N/A")}</strong> &nbsp;|&nbsp; 
                    Role: <strong style="color: #34D399;">{profile.get("role", "Academic Advisor")}</strong> &nbsp;|&nbsp; 
                    Dept: <strong style="color: #A78BFA;">{profile.get("department", "Academic Affairs")}</strong>
                </p>
                <div style="display: flex; justify-content: center; gap: 1rem;">
                    <a href="/Predict" target="_top" style="background: #FFFFFF; color: #05070E; padding: 12px 28px; border-radius: 9999px; font-weight: 800; text-decoration: none; font-size: 0.95rem;">Launch Predictor ↗</a>
                    <a href="/Student_Records" target="_top" style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.15); color: #FFFFFF; padding: 12px 28px; border-radius: 9999px; font-weight: 700; text-decoration: none; font-size: 0.95rem;">Student Records ↗</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Sign Out of Session", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["user"] = None
            st.session_state["profile"] = None
            st.rerun()

else:
    # 21st.dev Cinematic Double-Bezel Auth Screen
    auth_component_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
                user-select: none;
            }

            body {
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
            }

            /* Ambient Glow Backgrounds */
            .ambient-top {
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
            }

            .ambient-bottom {
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
            }

            /* ==========================================================
               HIGH-END 21ST.DEV DOUBLE-BEZEL BACK TO HOME BUTTON
               ========================================================== */
            .back-home-wrapper {
                position: absolute;
                top: 28px;
                left: 36px;
                z-index: 50;
                cursor: pointer;
            }

            .back-home-pill {
                display: inline-flex;
                align-items: center;
                gap: 10px;
                padding: 9px 20px;
                border-radius: 9999px;
                background: rgba(15, 23, 42, 0.55);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.12);
                box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.2);
                color: #CBD5E1;
                font-size: 0.82rem;
                font-weight: 700;
                letter-spacing: 0.04em;
                text-transform: uppercase;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }

            .back-home-pill:hover {
                color: #FFFFFF;
                border-color: rgba(255, 255, 255, 0.35);
                background: rgba(15, 23, 42, 0.8);
                box-shadow: 0 12px 30px -2px rgba(99, 102, 241, 0.25), inset 0 1px 1px 0 rgba(255, 255, 255, 0.35);
                transform: translateX(-3px);
            }

            .back-home-pill .chevron-icon {
                transition: transform 0.3s ease;
                display: flex;
                align-items: center;
            }

            .back-home-pill:hover .chevron-icon {
                transform: translateX(-4px);
            }

            /* ==========================================================
               3D PERSPECTIVE TILT CARD WITH CONTINUOUS ORBITING BORDER BEAM
               ========================================================== */
            .card-perspective-container {
                perspective: 1500px;
                width: 100%;
                max-width: 480px;
                margin: 0 auto;
                position: relative;
                z-index: 10;
            }

            .tilt-card-wrapper {
                position: relative;
                border-radius: 28px;
                padding: 2px;
                overflow: hidden;
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85);
                transform-style: preserve-3d;
                transition: transform 0.12s ease-out;
            }

            .tilt-card-wrapper::before {
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
            }

            @keyframes rotateBorderBeam {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            .tilt-card {
                position: relative;
                z-index: 2;
                border-radius: 26px;
                background: rgba(11, 15, 28, 0.9);
                backdrop-filter: blur(30px);
                -webkit-backdrop-filter: blur(30px);
                padding: 34px 38px;
            }

            .card-emblem {
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
            }

            .card-header-title {
                text-align: center;
                font-size: 1.65rem;
                font-weight: 900;
                letter-spacing: -0.03em;
                color: #FFFFFF;
                margin-bottom: 4px;
            }

            .card-header-sub {
                text-align: center;
                font-size: 0.85rem;
                color: #94A3B8;
                margin-bottom: 22px;
            }

            .auth-toggle-bar {
                display: flex;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 9999px;
                padding: 4px;
                margin-bottom: 24px;
            }

            .toggle-btn {
                flex: 1;
                text-align: center;
                padding: 8px 16px;
                border-radius: 9999px;
                font-size: 0.85rem;
                font-weight: 700;
                cursor: pointer;
                transition: all 0.25s ease;
                color: #94A3B8;
            }

            .toggle-btn.active {
                background: #FFFFFF;
                color: #05070E;
                box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25);
            }

            .auth-form-animated {
                animation: smoothFormSlide 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            }

            @keyframes smoothFormSlide {
                from {
                    opacity: 0;
                    transform: translateY(10px) scale(0.98);
                }
                to {
                    opacity: 1;
                    transform: translateY(0) scale(1);
                }
            }

            /* Staggered Spring Underline Inputs */
            .input-underline-group {
                position: relative;
                width: 100%;
                margin-bottom: 22px;
                padding-top: 14px;
            }

            .input-group-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 16px;
            }

            .floating-letters-wrapper {
                position: absolute;
                top: 18px;
                left: 0;
                pointer-events: none;
                display: flex;
                color: #94A3B8;
                font-size: 0.92rem;
                font-weight: 500;
            }

            .letter-wave-char {
                display: inline-block;
                transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.25s ease;
                will-change: transform;
            }

            .underline-field {
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
            }

            .underline-field:focus {
                border-bottom-color: #FFFFFF;
            }

            .input-underline-group.is-active .letter-wave-char {
                transform: translateY(-22px) scale(0.85);
                color: #E2E8F0;
                font-weight: 700;
            }

            .password-toggle-btn {
                position: absolute;
                right: 0;
                bottom: 8px;
                cursor: pointer;
                color: #94A3B8;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: color 0.2s ease, transform 0.2s ease;
            }
            .password-toggle-btn:hover {
                color: #FFFFFF;
                transform: scale(1.1);
            }
            .password-toggle-btn svg {
                width: 18px;
                height: 18px;
                stroke: currentColor;
                transition: all 0.25s ease;
            }

            .origin-submit-btn {
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
            }

            @keyframes authBtnBreathingShadow {
                0% {
                    box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.25), 0 0 15px 2px rgba(99, 102, 241, 0.25);
                }
                50% {
                    box-shadow: 0 16px 35px -2px rgba(255, 255, 255, 0.45), 0 0 25px 5px rgba(56, 189, 248, 0.45);
                }
                100% {
                    box-shadow: 0 12px 30px -4px rgba(255, 255, 255, 0.3), 0 0 18px 3px rgba(99, 102, 241, 0.35);
                }
            }

            .origin-submit-btn:hover {
                transform: translateY(-2px) scale(1.01);
                animation: none;
                box-shadow: 0 18px 45px rgba(255, 255, 255, 0.45), 0 0 30px rgba(56, 189, 248, 0.5);
            }

            .origin-submit-btn .origin-ripple {
                position: absolute;
                border-radius: 50%;
                background: #05070E;
                transform: translate(-50%, -50%) scale(0);
                pointer-events: none;
                transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 1;
            }

            .origin-submit-btn.active .origin-ripple {
                transform: translate(-50%, -50%) scale(1);
            }

            .origin-submit-btn .button-label {
                position: relative;
                z-index: 2;
                display: inline-flex;
                align-items: center;
                gap: 10px;
                transition: color 0.3s ease;
            }
            .origin-submit-btn.active .button-label {
                color: #FFFFFF;
            }

            .kinetic-vector-arrow {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }
            .origin-submit-btn:hover .kinetic-vector-arrow {
                transform: translateX(5px);
                animation: arrowKineticPulse 1.2s ease-in-out infinite alternate;
            }

            @keyframes arrowKineticPulse {
                0% { transform: translateX(4px); }
                100% { transform: translateX(8px); }
            }

            .footer-links {
                text-align: center;
                margin-top: 18px;
                font-size: 0.82rem;
                color: #64748B;
            }
            .footer-links a {
                color: #CBD5E1;
                text-decoration: none;
                font-weight: 700;
            }
        </style>
    </head>
    <body>
        <div class="ambient-top"></div>
        <div class="ambient-bottom"></div>

        <!-- 21st.dev Double-Bezel Glass Back to Home Button -->
        <div class="back-home-wrapper" onclick="navTo('/')">
            <div class="back-home-pill">
                <span class="chevron-icon">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="12" x2="5" y2="12"></line>
                        <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                </span>
                <span>Back to Home</span>
            </div>
        </div>

        <!-- 3D Perspective Tilt Card with Continuous 360deg Laser Border Beam -->
        <div class="card-perspective-container">
            <div class="tilt-card-wrapper" id="tiltCardWrapper">
                <div class="tilt-card">
                    <!-- Emblem Header -->
                    <div class="card-emblem">S</div>
                    <h2 class="card-header-title" id="formTitle">Welcome Back</h2>
                    <p class="card-header-sub" id="formSub">Sign in to access student prediction analytics</p>

                    <!-- Toggle Pills -->
                    <div class="auth-toggle-bar">
                        <div class="toggle-btn active" id="tabSignIn" onclick="switchTab('signin')">Sign In</div>
                        <div class="toggle-btn" id="tabSignUp" onclick="switchTab('signup')">Create Account</div>
                    </div>

                    <!-- SIGN IN FORM -->
                    <form id="signInForm" class="auth-form-animated" onsubmit="handleAuthSubmit(event, 'signin')">
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
                    <form id="signUpForm" class="auth-form-animated" style="display: none;" onsubmit="handleAuthSubmit(event, 'signup')">
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
            function navTo(url) {
                try {
                    if (window.parent && window.parent.location) {
                        window.parent.location.assign(url);
                        return;
                    }
                } catch(e) {}
                try {
                    if (window.top && window.top.location) {
                        window.top.location.assign(url);
                        return;
                    }
                } catch(e) {}
                window.location.assign(url);
            }

            // 1. 3D Perspective Mouse Tilt Physics
            const tiltCardWrapper = document.getElementById('tiltCardWrapper');
            document.addEventListener('mousemove', (e) => {
                const rect = tiltCardWrapper.getBoundingClientRect();
                const cardX = rect.left + rect.width / 2;
                const cardY = rect.top + rect.height / 2;
                const mouseX = e.clientX - cardX;
                const mouseY = e.clientY - cardY;

                const rotateX = -(mouseY / (window.innerHeight / 2)) * 6;
                const rotateY = (mouseX / (window.innerWidth / 2)) * 6;

                tiltCardWrapper.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });

            document.addEventListener('mouseleave', () => {
                tiltCardWrapper.style.transform = 'rotateX(0deg) rotateY(0deg)';
            });

            // 2. Setup Staggered Spring Letter Wave for Underline Inputs
            const setupSpringLetterWave = (inputId, labelId, labelText) => {
                const input = document.getElementById(inputId);
                const labelContainer = document.getElementById(labelId);
                const group = input.parentElement;

                if (!input || !labelContainer) return;

                labelContainer.innerHTML = '';
                labelText.split('').forEach((char, idx) => {
                    const span = document.createElement('span');
                    span.className = 'letter-wave-char';
                    span.textContent = char === ' ' ? '\\u00A0' : char;
                    span.style.transitionDelay = `${idx * 0.03}s`;
                    labelContainer.appendChild(span);
                });

                const updateWaveState = () => {
                    if (document.activeElement === input || input.value.trim().length > 0) {
                        group.classList.add('is-active');
                    } else {
                        group.classList.remove('is-active');
                    }
                };

                input.addEventListener('focus', updateWaveState);
                input.addEventListener('blur', updateWaveState);
                input.addEventListener('input', updateWaveState);
            };

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
            function switchTab(tab) {
                const signInForm = document.getElementById('signInForm');
                const signUpForm = document.getElementById('signUpForm');
                const tabSignIn = document.getElementById('tabSignIn');
                const tabSignUp = document.getElementById('tabSignUp');
                const formTitle = document.getElementById('formTitle');
                const formSub = document.getElementById('formSub');
                const footerToggleText = document.getElementById('footerToggleText');

                if (tab === 'signup') {
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
                } else {
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
                }
            }

            // 4. Animated Watch / Watch-Off Eye Toggle Logic
            function togglePasswordEye(id, containerEl) {
                const input = document.getElementById(id);
                if (!input) return;

                if (input.type === 'password') {
                    input.type = 'text';
                    containerEl.innerHTML = `
                        <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                    `;
                } else {
                    input.type = 'password';
                    containerEl.innerHTML = `
                        <svg class="eye-svg" viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                            <line x1="1" y1="1" x2="23" y2="23"></line>
                        </svg>
                    `;
                }
            }

            // 5. Origin Button Radial Ripple Physics
            const attachOriginRipple = (btnId) => {
                const btn = document.getElementById(btnId);
                if (!btn) return;
                const ripple = btn.querySelector('.origin-ripple');

                btn.addEventListener('mouseenter', (e) => {
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

                    ripple.style.left = `${x}px`;
                    ripple.style.top = `${y}px`;
                    ripple.style.width = `${diameter}px`;
                    ripple.style.height = `${diameter}px`;
                    btn.classList.add('active');
                });

                btn.addEventListener('mouseleave', () => {
                    btn.classList.remove('active');
                });
            };

            attachOriginRipple('btnSignInOrigin');
            attachOriginRipple('btnSignUpOrigin');

            function handleAuthSubmit(event, action) {
                event.preventDefault();
                const btn = event.target.querySelector('button');
                const label = btn.querySelector('.button-label');
                label.innerHTML = '<span>Verifying credentials...</span>';
            }
        </script>
    </body>
    </html>
    """

    components.html(auth_component_html, height=920, scrolling=False)
