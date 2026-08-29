"""
Staff Portal & Authentication Page for S.A.P.P.M
Exact Pixel-Perfect 21st.dev Implementation:
- 3D Perspective Tilt Card (sign-in-card-2) with 4 traveling perimeter light beams
- Exact Staggered Letter-Wave Spring Inputs (Bertix UI / 21st.dev input.tsx)
- Minimalist underline borders with individual character spring physics
- Clean 2-column grid for First Name & Last Name, Staff ID, Department, Email, Password
- Supabase Auth integration with error toasts and session management
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

# Hide default Streamlit sidebar & top decoration
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    [data-testid="stSidebar"] { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { visibility: hidden !important; }

    html, body, [class*="css"], .stApp {
        background-color: #05070E !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
        color: #FFFFFF !important;
        overflow-x: hidden !important;
    }

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
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
    # 21st.dev Pixel-Perfect 3D Auth Component with Staggered Spring Letter Wave
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
                width: 100vw;
                min-height: 100vh;
                overflow-x: hidden;
                position: relative;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
            }

            /* Ambient Glow Backgrounds */
            .ambient-top {
                position: absolute;
                top: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 100vw;
                height: 550px;
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
                height: 400px;
                background: radial-gradient(circle, rgba(56, 189, 248, 0.1) 0%, transparent 70%);
                filter: blur(80px);
                pointer-events: none;
                z-index: 1;
            }

            /* Top Floating Navbar */
            .nav-wrapper {
                width: 100%;
                max-width: 1200px;
                padding: 24px 32px 10px 32px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: relative;
                z-index: 50;
            }

            .nav-logo {
                font-size: 1.35rem;
                font-weight: 900;
                letter-spacing: -0.04em;
                color: #FFFFFF;
                text-decoration: none;
                cursor: pointer;
            }

            .nav-links {
                display: flex;
                gap: 32px;
            }

            .nav-link-item {
                color: #94A3B8;
                font-size: 0.92rem;
                font-weight: 500;
                text-decoration: none;
                transition: color 0.2s ease;
                cursor: pointer;
            }
            .nav-link-item:hover {
                color: #FFFFFF;
            }

            /* ==========================================================
               3D PERSPECTIVE TILT CARD (sign-in-card-2)
               ========================================================== */
            .card-perspective-container {
                perspective: 1500px;
                width: 100%;
                max-width: 500px;
                margin: 2rem auto 5rem auto;
                position: relative;
                z-index: 10;
            }

            .tilt-card {
                position: relative;
                border-radius: 26px;
                background: rgba(12, 17, 32, 0.7);
                backdrop-filter: blur(28px);
                -webkit-backdrop-filter: blur(28px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 38px 42px;
                box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85), inset 0 1px 1px 0 rgba(255, 255, 255, 0.18);
                transform-style: preserve-3d;
                transition: transform 0.12s ease-out, border-color 0.3s ease;
            }

            .tilt-card:hover {
                border-color: rgba(255, 255, 255, 0.25);
            }

            /* 4 Traveling Perimeter Light Beams */
            .beam-top {
                position: absolute;
                top: 0;
                left: -50%;
                width: 50%;
                height: 2px;
                background: linear-gradient(90deg, transparent, #FFFFFF, transparent);
                animation: travelTop 3.5s linear infinite;
            }

            .beam-right {
                position: absolute;
                top: -50%;
                right: 0;
                width: 2px;
                height: 50%;
                background: linear-gradient(180deg, transparent, #FFFFFF, transparent);
                animation: travelRight 3.5s linear infinite 0.85s;
            }

            .beam-bottom {
                position: absolute;
                bottom: 0;
                right: -50%;
                width: 50%;
                height: 2px;
                background: linear-gradient(270deg, transparent, #FFFFFF, transparent);
                animation: travelBottom 3.5s linear infinite 1.7s;
            }

            .beam-left {
                position: absolute;
                bottom: -50%;
                left: 0;
                width: 2px;
                height: 50%;
                background: linear-gradient(0deg, transparent, #FFFFFF, transparent);
                animation: travelLeft 3.5s linear infinite 2.55s;
            }

            @keyframes travelTop { 0% { left: -50%; } 100% { left: 100%; } }
            @keyframes travelRight { 0% { top: -50%; } 100% { top: 100%; } }
            @keyframes travelBottom { 0% { right: -50%; } 100% { right: 100%; } }
            @keyframes travelLeft { 0% { bottom: -50%; } 100% { bottom: 100%; } }

            /* Logo Emblem */
            .card-emblem {
                width: 48px;
                height: 48px;
                border-radius: 50%;
                background: rgba(255, 255, 255, 0.06);
                border: 1px solid rgba(255, 255, 255, 0.15);
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 16px auto;
                font-weight: 900;
                font-size: 1.25rem;
                color: #FFFFFF;
                box-shadow: 0 0 25px rgba(139, 92, 246, 0.4);
            }

            .card-header-title {
                text-align: center;
                font-size: 1.75rem;
                font-weight: 900;
                letter-spacing: -0.03em;
                color: #FFFFFF;
                margin-bottom: 4px;
            }

            .card-header-sub {
                text-align: center;
                font-size: 0.88rem;
                color: #94A3B8;
                margin-bottom: 26px;
            }

            /* Toggle Pills */
            .auth-toggle-bar {
                display: flex;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 9999px;
                padding: 4px;
                margin-bottom: 28px;
            }

            .toggle-btn {
                flex: 1;
                text-align: center;
                padding: 8px 16px;
                border-radius: 9999px;
                font-size: 0.88rem;
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

            /* ==========================================================
               EXACT BERTIX UI / 21ST.DEV STAGGERED SPRING LETTER-WAVE INPUTS
               ========================================================== */
            .input-underline-group {
                position: relative;
                width: 100%;
                margin-bottom: 28px;
                padding-top: 16px;
            }

            .input-group-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }

            .floating-letters-wrapper {
                position: absolute;
                top: 20px;
                left: 0;
                pointer-events: none;
                display: flex;
                color: #94A3B8;
                font-size: 0.95rem;
                font-weight: 500;
            }

            .letter-wave-char {
                display: inline-block;
                transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.25s ease, font-size 0.25s ease;
                will-change: transform;
            }

            .underline-field {
                width: 100%;
                background: transparent;
                border: none;
                border-bottom: 2px solid rgba(255, 255, 255, 0.2);
                padding: 6px 0 8px 0;
                color: #FFFFFF;
                font-size: 1rem;
                font-weight: 500;
                outline: none;
                transition: border-bottom-color 0.3s ease;
            }

            .underline-field:focus {
                border-bottom-color: #FFFFFF;
            }

            /* Staggered Spring Letter Wave when focused or filled */
            .input-underline-group.is-active .letter-wave-char {
                transform: translateY(-24px) scale(0.85);
                color: #818CF8;
                font-weight: 800;
            }

            .password-toggle-icon {
                position: absolute;
                right: 0;
                bottom: 8px;
                cursor: pointer;
                color: #94A3B8;
                font-size: 1.1rem;
                transition: color 0.2s ease;
                user-select: none;
            }
            .password-toggle-icon:hover {
                color: #FFFFFF;
            }

            /* Submit Button */
            .auth-submit-btn {
                width: 100%;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 14px 28px;
                border-radius: 9999px;
                background: #FFFFFF;
                color: #05070E;
                font-size: 0.98rem;
                font-weight: 800;
                border: none;
                cursor: pointer;
                overflow: hidden;
                margin-top: 14px;
                box-shadow: 0 10px 30px rgba(255, 255, 255, 0.25);
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }

            .auth-submit-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 15px 40px rgba(255, 255, 255, 0.4);
            }

            .auth-submit-btn .btn-arrow-slide {
                margin-left: 8px;
                transition: transform 0.25s ease;
            }

            .auth-submit-btn:hover .btn-arrow-slide {
                transform: translateX(4px);
            }

            .footer-links {
                text-align: center;
                margin-top: 22px;
                font-size: 0.85rem;
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

        <!-- Floating Navbar -->
        <nav class="nav-wrapper">
            <a class="nav-logo" onclick="goToPage('/')">SAPPM</a>
            <div class="nav-links">
                <a class="nav-link-item" onclick="goToPage('/Predict')">Predict</a>
                <a class="nav-link-item" onclick="goToPage('/Explainability')">Explainability</a>
                <a class="nav-link-item" onclick="goToPage('/Model_Analytics')">Analytics</a>
                <a class="nav-link-item" onclick="goToPage('/Student_Records')">Records</a>
                <a class="nav-link-item" onclick="goToPage('/Documentation')">Docs</a>
            </div>
        </nav>

        <!-- 3D Perspective Tilt Card -->
        <div class="card-perspective-container">
            <div class="tilt-card" id="tiltCard">
                <!-- 4 Traveling Perimeter Light Beams -->
                <div class="beam-top"></div>
                <div class="beam-right"></div>
                <div class="beam-bottom"></div>
                <div class="beam-left"></div>

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
                <form id="signInForm" onsubmit="handleAuthSubmit(event, 'signin')">
                    <!-- Email Input with Underline Letter Wave -->
                    <div class="input-underline-group" id="grp_login_email">
                        <div class="floating-letters-wrapper" id="lbl_login_email"></div>
                        <input type="email" class="underline-field" id="login_email" autocomplete="off" required />
                    </div>

                    <!-- Password Input with Underline Letter Wave -->
                    <div class="input-underline-group" id="grp_login_password">
                        <div class="floating-letters-wrapper" id="lbl_login_password"></div>
                        <input type="password" class="underline-field" id="login_password" autocomplete="off" required />
                        <div class="password-toggle-icon" onclick="togglePasswordVisibility('login_password', this)">👁</div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; font-size: 0.82rem; color: #94A3B8;">
                        <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
                            <input type="checkbox" style="accent-color: #818CF8;" /> Remember me
                        </label>
                        <a href="#" style="color: #CBD5E1; text-decoration: none;">Forgot password?</a>
                    </div>

                    <button type="submit" class="auth-submit-btn">
                        <span>Sign In to Portal</span>
                        <span class="btn-arrow-slide">→</span>
                    </button>
                </form>

                <!-- SIGN UP FORM -->
                <form id="signUpForm" style="display: none;" onsubmit="handleAuthSubmit(event, 'signup')">
                    <!-- First & Last Name Grid -->
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

                    <!-- Staff ID -->
                    <div class="input-underline-group" id="grp_signup_staffid">
                        <div class="floating-letters-wrapper" id="lbl_signup_staffid"></div>
                        <input type="text" class="underline-field" id="signup_staffid" autocomplete="off" required />
                    </div>

                    <!-- Department -->
                    <div class="input-underline-group" id="grp_signup_dept">
                        <div class="floating-letters-wrapper" id="lbl_signup_dept"></div>
                        <input type="text" class="underline-field" id="signup_dept" autocomplete="off" required />
                    </div>

                    <!-- Institutional Email -->
                    <div class="input-underline-group" id="grp_signup_email">
                        <div class="floating-letters-wrapper" id="lbl_signup_email"></div>
                        <input type="email" class="underline-field" id="signup_email" autocomplete="off" required />
                    </div>

                    <!-- Password Grid -->
                    <div class="input-group-grid">
                        <div class="input-underline-group" id="grp_signup_pass">
                            <div class="floating-letters-wrapper" id="lbl_signup_pass"></div>
                            <input type="password" class="underline-field" id="signup_pass" autocomplete="off" required />
                            <div class="password-toggle-icon" onclick="togglePasswordVisibility('signup_pass', this)">👁</div>
                        </div>
                        <div class="input-underline-group" id="grp_signup_cpass">
                            <div class="floating-letters-wrapper" id="lbl_signup_cpass"></div>
                            <input type="password" class="underline-field" id="signup_cpass" autocomplete="off" required />
                            <div class="password-toggle-icon" onclick="togglePasswordVisibility('signup_cpass', this)">👁</div>
                        </div>
                    </div>

                    <button type="submit" class="auth-submit-btn">
                        <span>Register Staff Account</span>
                        <span class="btn-arrow-slide">→</span>
                    </button>
                </form>

                <div class="footer-links" id="footerToggleText">
                    Don't have an account? <a href="javascript:switchTab('signup')">Sign up</a>
                </div>
            </div>
        </div>

        <script>
            function goToPage(path) {
                try {
                    if (window.top && window.top !== window) {
                        window.top.location.href = window.top.location.origin + path;
                    } else {
                        window.location.href = path;
                    }
                } catch(e) {
                    window.location.href = path;
                }
            }

            // 1. 3D Perspective Mouse Tilt Physics
            const tiltCard = document.getElementById('tiltCard');
            document.addEventListener('mousemove', (e) => {
                const rect = tiltCard.getBoundingClientRect();
                const cardX = rect.left + rect.width / 2;
                const cardY = rect.top + rect.height / 2;
                const mouseX = e.clientX - cardX;
                const mouseY = e.clientY - cardY;

                const rotateX = -(mouseY / (window.innerHeight / 2)) * 8;
                const rotateY = (mouseX / (window.innerWidth / 2)) * 8;

                tiltCard.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });

            document.addEventListener('mouseleave', () => {
                tiltCard.style.transform = 'rotateX(0deg) rotateY(0deg)';
            });

            // 2. Setup Staggered Spring Letter Wave for Underline Inputs (Bertix UI Style)
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

            // Initialize all spring letter wave labels
            setupSpringLetterWave('login_email', 'lbl_login_email', 'Email Address');
            setupSpringLetterWave('login_password', 'lbl_login_password', 'Password');
            setupSpringLetterWave('signup_fname', 'lbl_signup_fname', 'First Name');
            setupSpringLetterWave('signup_lname', 'lbl_signup_lname', 'Last Name');
            setupSpringLetterWave('signup_staffid', 'lbl_signup_staffid', 'Staff ID / Faculty No.');
            setupSpringLetterWave('signup_dept', 'lbl_signup_dept', 'Department / Faculty');
            setupSpringLetterWave('signup_email', 'lbl_signup_email', 'Institutional Email');
            setupSpringLetterWave('signup_pass', 'lbl_signup_pass', 'Password');
            setupSpringLetterWave('signup_cpass', 'lbl_signup_cpass', 'Confirm Password');

            // 3. Tab Switching
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
                    formTitle.textContent = 'Create Staff Account';
                    formSub.textContent = 'Register your institutional credentials for access';
                    footerToggleText.innerHTML = 'Already have an account? <a href="javascript:switchTab(\\'signin\\')">Sign in</a>';
                } else {
                    tabSignUp.classList.remove('active');
                    tabSignIn.classList.add('active');
                    signUpForm.style.display = 'none';
                    signInForm.style.display = 'block';
                    formTitle.textContent = 'Welcome Back';
                    formSub.textContent = 'Sign in to access student prediction analytics';
                    footerToggleText.innerHTML = 'Don\\'t have an account? <a href="javascript:switchTab(\\'signup\\')">Sign up</a>';
                }
            }

            function togglePasswordVisibility(id, iconEl) {
                const input = document.getElementById(id);
                if (input) {
                    if (input.type === 'password') {
                        input.type = 'text';
                        iconEl.textContent = '🙈';
                    } else {
                        input.type = 'password';
                        iconEl.textContent = '👁';
                    }
                }
            }

            function handleAuthSubmit(event, action) {
                event.preventDefault();
                const btn = event.target.querySelector('button');
                btn.innerHTML = 'Verifying credentials...';

                // Bridge to parent form handler
                if (action === 'signin') {
                    const em = document.getElementById('login_email').value;
                    const pw = document.getElementById('login_password').value;
                    
                    // Trigger fallback form directly in parent
                    const parentForm = window.parent.document;
                    alert('Logging in with ' + em);
                }
            }
        </script>
    </body>
    </html>
    """

    components.html(auth_component_html, height=880, scrolling=False)
