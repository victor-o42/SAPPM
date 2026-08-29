"""
Staff Portal & Authentication Page for S.A.P.P.M
Engineered to match 21st.dev sign-in-card-2 & input.tsx:
- 3D Perspective Tilt Card with Mouse Physics
- 4 Traveling Light Beams circulating along the perimeter borders
- Animated Floating Letter-Wave Inputs (staggered letter wave on focus/typing)
- Separate First Name, Last Name, Staff ID, Department, Email, Password fields
- Origin Button / Interactive Hover submit with kinetic animated arrow
- Full integration with Supabase Auth
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

# Hide default Streamlit sidebar & chrome
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

# Check active auth session
is_auth = st.session_state.get("authenticated", False)
profile = st.session_state.get("profile", {})

# If user is already authenticated, render the Management Console
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
    # 3D Perspective Tilt Card with Staggered Letter Wave Inputs & Supabase Auth Bridge
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
                justify-content: space-between;
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
                max-width: 480px;
                margin: 1.5rem auto 4rem auto;
                position: relative;
                z-index: 10;
            }

            .tilt-card {
                position: relative;
                border-radius: 26px;
                background: rgba(12, 17, 32, 0.65);
                backdrop-filter: blur(28px);
                -webkit-backdrop-filter: blur(28px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 36px 38px;
                box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.18);
                transform-style: preserve-3d;
                transition: transform 0.15s ease-out, border-color 0.3s ease;
            }

            .tilt-card:hover {
                border-color: rgba(255, 255, 255, 0.22);
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
                font-size: 1.2rem;
                color: #FFFFFF;
                box-shadow: 0 0 25px rgba(139, 92, 246, 0.35);
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
                margin-bottom: 24px;
            }

            /* Toggle Pills between Sign In & Sign Up */
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

            /* ==========================================================
               ANIMATED FLOATING LETTER-WAVE INPUTS (input.tsx)
               ========================================================== */
            .input-group {
                position: relative;
                margin-bottom: 20px;
                width: 100%;
            }

            .input-group-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 14px;
            }

            .floating-label-container {
                position: absolute;
                top: 14px;
                left: 14px;
                pointer-events: none;
                display: flex;
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
                color: #94A3B8;
                font-size: 0.9rem;
            }

            .letter-span {
                display: inline-block;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), color 0.3s ease;
                will-change: transform;
            }

            .wave-input {
                width: 100%;
                background: rgba(255, 255, 255, 0.04);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 14px;
                padding: 14px 14px;
                color: #FFFFFF;
                font-size: 0.95rem;
                font-weight: 500;
                outline: none;
                transition: all 0.25s ease;
            }

            .wave-input:focus {
                border-color: rgba(255, 255, 255, 0.35);
                background: rgba(255, 255, 255, 0.08);
                box-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
            }

            /* When input is focused or has content, wave the letters upward */
            .input-group.active .floating-label-container {
                top: -8px;
                left: 8px;
                font-size: 0.72rem;
                color: #818CF8;
                font-weight: 800;
                background: #090D1A;
                padding: 0 6px;
                border-radius: 4px;
            }

            .input-group.active .letter-span {
                transform: translateY(-2px);
            }

            .password-toggle-icon {
                position: absolute;
                right: 14px;
                top: 15px;
                cursor: pointer;
                color: #94A3B8;
                transition: color 0.2s ease;
            }
            .password-toggle-icon:hover {
                color: #FFFFFF;
            }

            /* Action Submit Button (Interactive Hover / Origin Style) */
            .auth-submit-btn {
                width: 100%;
                position: relative;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 13px 24px;
                border-radius: 9999px;
                background: #FFFFFF;
                color: #05070E;
                font-size: 0.95rem;
                font-weight: 800;
                border: none;
                cursor: pointer;
                overflow: hidden;
                margin-top: 10px;
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
                margin-top: 18px;
                font-size: 0.82rem;
                color: #64748B;
            }
            .footer-links a {
                color: #CBD5E1;
                text-decoration: none;
                font-weight: 600;
            }
        </style>
    </head>
    <body>
        <div class="ambient-top"></div>
        <div class="ambient-bottom"></div>

        <!-- Floating Navbar -->
        <nav class="nav-wrapper">
            <a class="nav-logo" href="/" target="_top">SAPPM</a>
            <div class="nav-links">
                <a class="nav-link-item" href="/Predict" target="_top">Predict</a>
                <a class="nav-link-item" href="/Explainability" target="_top">Explainability</a>
                <a class="nav-link-item" href="/Model_Analytics" target="_top">Analytics</a>
                <a class="nav-link-item" href="/Student_Records" target="_top">Records</a>
                <a class="nav-link-item" href="/Documentation" target="_top">Docs</a>
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
                    <!-- Email Input with Letter Wave -->
                    <div class="input-group" id="grp_login_email">
                        <div class="floating-label-container" id="lbl_login_email">
                            <!-- Letters rendered via JS -->
                        </div>
                        <input type="email" class="wave-input" id="login_email" required />
                    </div>

                    <!-- Password Input with Letter Wave -->
                    <div class="input-group" id="grp_login_password">
                        <div class="floating-label-container" id="lbl_login_password">
                            <!-- Letters rendered via JS -->
                        </div>
                        <input type="password" class="wave-input" id="login_password" required />
                        <div class="password-toggle-icon" onclick="togglePasswordVisibility('login_password')">
                            👁
                        </div>
                    </div>

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; font-size: 0.8rem; color: #94A3B8;">
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
                        <div class="input-group" id="grp_signup_fname">
                            <div class="floating-label-container" id="lbl_signup_fname"></div>
                            <input type="text" class="wave-input" id="signup_fname" required />
                        </div>
                        <div class="input-group" id="grp_signup_lname">
                            <div class="floating-label-container" id="lbl_signup_lname"></div>
                            <input type="text" class="wave-input" id="signup_lname" required />
                        </div>
                    </div>

                    <!-- Staff ID -->
                    <div class="input-group" id="grp_signup_staffid">
                        <div class="floating-label-container" id="lbl_signup_staffid"></div>
                        <input type="text" class="wave-input" id="signup_staffid" placeholder="" required />
                    </div>

                    <!-- Department -->
                    <div class="input-group" id="grp_signup_dept">
                        <div class="floating-label-container" id="lbl_signup_dept"></div>
                        <input type="text" class="wave-input" id="signup_dept" required />
                    </div>

                    <!-- Institutional Email -->
                    <div class="input-group" id="grp_signup_email">
                        <div class="floating-label-container" id="lbl_signup_email"></div>
                        <input type="email" class="wave-input" id="signup_email" required />
                    </div>

                    <!-- Password Grid -->
                    <div class="input-group-grid">
                        <div class="input-group" id="grp_signup_pass">
                            <div class="floating-label-container" id="lbl_signup_pass"></div>
                            <input type="password" class="wave-input" id="signup_pass" required />
                        </div>
                        <div class="input-group" id="grp_signup_cpass">
                            <div class="floating-label-container" id="lbl_signup_cpass"></div>
                            <input type="password" class="wave-input" id="signup_cpass" required />
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

        <!-- 3D Tilt Physics & Letter Wave Animation Logic -->
        <script>
            // 1. 3D Perspective Mouse Tilt
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

            // 2. Setup Floating Letter Waves for all inputs
            const setupLetterWave = (inputId, labelId, labelText) => {
                const input = document.getElementById(inputId);
                const labelContainer = document.getElementById(labelId);
                const group = input.parentElement;

                if (!input || !labelContainer) return;

                labelContainer.innerHTML = '';
                labelText.split('').forEach((char, idx) => {
                    const span = document.createElement('span');
                    span.className = 'letter-span';
                    span.textContent = char === ' ' ? '\\u00A0' : char;
                    span.style.transitionDelay = `${idx * 0.02}s`;
                    labelContainer.appendChild(span);
                });

                const checkState = () => {
                    if (input === document.activeElement || input.value.trim().length > 0) {
                        group.classList.add('active');
                    } else {
                        group.classList.remove('active');
                    }
                };

                input.addEventListener('focus', checkState);
                input.addEventListener('blur', checkState);
                input.addEventListener('input', checkState);
            };

            // Initialize all labels
            setupLetterWave('login_email', 'lbl_login_email', 'Email address');
            setupLetterWave('login_password', 'lbl_login_password', 'Password');
            setupLetterWave('signup_fname', 'lbl_signup_fname', 'First Name');
            setupLetterWave('signup_lname', 'lbl_signup_lname', 'Last Name');
            setupLetterWave('signup_staffid', 'lbl_signup_staffid', 'Staff ID / Faculty No.');
            setupLetterWave('signup_dept', 'lbl_signup_dept', 'Department / Faculty');
            setupLetterWave('signup_email', 'lbl_signup_email', 'Institutional Email');
            setupLetterWave('signup_pass', 'lbl_signup_pass', 'Password (Min 6 chars)');
            setupLetterWave('signup_cpass', 'lbl_signup_cpass', 'Confirm Password');

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

            function togglePasswordVisibility(id) {
                const input = document.getElementById(id);
                if (input) {
                    input.type = input.type === 'password' ? 'text' : 'password';
                }
            }

            // 4. Submit to parent Streamlit
            function handleAuthSubmit(event, action) {
                event.preventDefault();
                const btn = event.target.querySelector('button');
                btn.innerHTML = 'Verifying credentials...';

                if (action === 'signin') {
                    const email = document.getElementById('login_email').value;
                    const pass = document.getElementById('login_password').value;
                    window.parent.postMessage({
                        type: 'streamlit:auth',
                        action: 'signin',
                        email: email,
                        password: pass
                    }, '*');
                } else {
                    const fname = document.getElementById('signup_fname').value;
                    const lname = document.getElementById('signup_lname').value;
                    const staffid = document.getElementById('signup_staffid').value;
                    const dept = document.getElementById('signup_dept').value;
                    const email = document.getElementById('signup_email').value;
                    const pass = document.getElementById('signup_pass').value;
                    const cpass = document.getElementById('signup_cpass').value;

                    if (pass !== cpass) {
                        alert('Passwords do not match.');
                        btn.innerHTML = 'Register Staff Account →';
                        return;
                    }

                    window.parent.postMessage({
                        type: 'streamlit:auth',
                        action: 'signup',
                        fname: fname,
                        lname: lname,
                        staffid: staffid,
                        dept: dept,
                        email: email,
                        password: pass
                    }, '*');
                }
            }
        </script>
    </body>
    </html>
    """

    # Render interactive 3D auth card
    components.html(auth_component_html, height=920, scrolling=False)

    # Streamlit Direct Form Fallback & Supabase Login Handler
    with st.expander("⚡ Quick Fallback Form / Direct Sign In", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Direct Sign In")
            with st.form("fallback_signin"):
                f_email = st.text_input("Email", placeholder="staff@university.edu")
                f_pass = st.text_input("Password", type="password")
                if st.form_submit_button("Sign In"):
                    res = sign_in_staff(f_email, f_pass)
                    if res["success"]:
                        st.session_state["authenticated"] = True
                        st.session_state["user"] = res["user"]
                        st.session_state["profile"] = res["profile"]
                        st.success(res["message"])
                        st.rerun()
                    else:
                        st.error(res["message"])
        with c2:
            st.subheader("Direct Registration")
            with st.form("fallback_signup"):
                fn = st.text_input("First Name")
                ln = st.text_input("Last Name")
                sid = st.text_input("Staff ID")
                dept = st.text_input("Department", value="Computer Science")
                em = st.text_input("Email")
                pwd = st.text_input("Password", type="password")
                if st.form_submit_button("Create Account"):
                    res = sign_up_staff(em, pwd, fn, ln, sid, dept)
                    if res["success"]:
                        st.success(res["message"])
                    else:
                        st.error(res["message"])
