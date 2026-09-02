"""
S.A.P.P.M - Student Academic Performance Prediction System
Unified Master Controller with Clean State-Driven View Routing
- State Views: "landing", "auth", "app", "restricted"
- Zero Iframe Trapping: Full-width root-level execution with instant DOM flushes via st.rerun()
- Pre-auth: 100% Original 3D Perspective Tilt Card with Rotating Laser Border Beam & Motion "Bars" Loader
- Post-auth: Full-Width Original Prediction Dashboard (app_3.py) with Slider05 44-Bar Equalizer Sliders & Matplotlib Explainability Charts
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import shap
from src.auth import sign_in_staff, sign_up_staff, sign_out_staff

# 1. Root Configuration & Full-Width Layout (Very first command)
st.set_page_config(
    page_title="SAPPM - Academic Performance Prediction System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Global Root CSS: Eliminate Default Padding, Sidebar Chrome & Internal Scrollbars
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    /* Clean Global Scrollbar */
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

    [data-testid="stAppViewBlockContainer"] {
        overflow-x: hidden !important;
        padding: 0 !important;
    }

    iframe {
        width: 100% !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Synchronize URL query params with session state view
if "current_view" not in st.session_state:
    query_view = st.query_params.get("view", "landing")
    st.session_state["current_view"] = query_view

query_view = st.query_params.get("view")
if query_view and query_view in ["landing", "auth", "app", "restricted"] and query_view != st.session_state["current_view"]:
    st.session_state["current_view"] = query_view

# Handle direct auth actions from query parameters
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
            st.session_state["current_view"] = "app"
            st.query_params.clear()
            st.query_params["view"] = "app"
            st.rerun()
        else:
            st.session_state["auth_error"] = res.get("message", "Invalid email or password.")
            st.session_state["current_view"] = "auth"
            st.query_params.clear()
            st.query_params["view"] = "auth"
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
        st.session_state["current_view"] = "auth"
        st.query_params.clear()
        st.query_params["view"] = "auth"
        st.rerun()
    elif len(password) < 6:
        st.session_state["auth_error"] = "Registration failed: Password must be at least 6 characters long."
        st.session_state["current_view"] = "auth"
        st.query_params.clear()
        st.query_params["view"] = "auth"
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
            st.session_state["current_view"] = "app"
            st.query_params.clear()
            st.query_params["view"] = "app"
            st.rerun()
        else:
            st.session_state["auth_error"] = res.get("message", "Registration failed. Please check inputs.")
            st.session_state["current_view"] = "auth"
            st.query_params.clear()
            st.query_params["view"] = "auth"
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
# VIEW 1: LANDING PAGE (HERO + 3D ROBOT + STATS + SPOTLIGHT)
# =========================================================================
if st.session_state["current_view"] == "landing":
    landing_page_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.72/build/spline-viewer.js"></script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; user-select: none; }
            body { background-color: #05070E; color: #FFFFFF; width: 100%; min-height: 100vh; overflow-x: hidden; position: relative; display: flex; flex-direction: column; justify-content: space-between; }
            
            .cursor-spotlight { position: fixed; width: 650px; height: 650px; border-radius: 50%; background: radial-gradient(circle, rgba(99, 102, 241, 0.14) 0%, rgba(56, 189, 248, 0.05) 45%, transparent 70%); filter: blur(55px); pointer-events: none; transform: translate(-50%, -50%); z-index: 1; transition: opacity 0.3s ease; }
            .ambient-glow-top { position: absolute; top: -10%; left: 50%; transform: translateX(-50%); width: 100vw; height: 500px; background: radial-gradient(circle, rgba(139, 92, 246, 0.18) 0%, rgba(99, 102, 241, 0.08) 40%, transparent 70%); filter: blur(80px); pointer-events: none; z-index: 0; }
            
            .navbar-container { position: relative; z-index: 100; max-width: 1200px; width: 100%; margin: 24px auto 0 auto; padding: 0 32px; display: flex; justify-content: space-between; align-items: center; }
            .nav-logo { font-size: 1.45rem; font-weight: 900; letter-spacing: -0.04em; color: #FFFFFF; cursor: pointer; }
            .nav-menu { display: flex; gap: 32px; align-items: center; }
            .nav-link { color: #94A3B8; font-size: 0.92rem; font-weight: 600; text-decoration: none; cursor: pointer; transition: color 0.2s ease; }
            .nav-link:hover { color: #FFFFFF; }
            .nav-actions { display: flex; gap: 14px; align-items: center; }

            .btn-star-login { position: relative; display: inline-flex; align-items: center; gap: 6px; padding: 9px 20px; border-radius: 9999px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); color: #FFFFFF; font-size: 0.85rem; font-weight: 700; cursor: pointer; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.2); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
            .btn-star-login:hover { background: rgba(255, 255, 255, 0.1); border-color: rgba(255, 255, 255, 0.35); transform: translateY(-2px); box-shadow: 0 8px 25px -2px rgba(99, 102, 241, 0.3), inset 0 1px 1px 0 rgba(255, 255, 255, 0.4); }

            .interactive-hover-btn { position: relative; display: inline-flex; align-items: center; justify-content: center; padding: 9px 24px; border-radius: 9999px; background: #FFFFFF; color: #05070E; font-size: 0.85rem; font-weight: 800; cursor: pointer; border: 1px solid rgba(255, 255, 255, 0.5); box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.3), 0 0 15px 2px rgba(99, 102, 241, 0.3); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
            .interactive-hover-btn:hover { transform: translateY(-2px); box-shadow: 0 15px 35px rgba(255, 255, 255, 0.45), 0 0 25px rgba(56, 189, 248, 0.45); }

            .hero-section { position: relative; z-index: 20; max-width: 900px; margin: 3rem auto 0 auto; text-align: center; padding: 0 20px; }
            .hero-headline { font-size: clamp(2.4rem, 5.2vw, 4.2rem); font-weight: 900; letter-spacing: -0.04em; line-height: 1.05; color: #FFFFFF; margin-bottom: 1rem; }
            .hero-subhead { font-size: clamp(0.95rem, 1.4vw, 1.15rem); color: #94A3B8; max-width: 600px; margin: 0 auto 2rem auto; font-weight: 500; line-height: 1.5; }

            .origin-btn { position: relative; display: inline-flex; align-items: center; gap: 8px; padding: 13px 30px; border-radius: 9999px; background: #FFFFFF; color: #05070E; font-size: 0.95rem; font-weight: 800; border: 1px solid rgba(255, 255, 255, 0.5); cursor: pointer; overflow: hidden; box-shadow: 0 12px 30px -4px rgba(255, 255, 255, 0.35), 0 0 20px 2px rgba(99, 102, 241, 0.35); transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); }
            .origin-btn:hover { transform: translateY(-2px); }

            .spline-stage-container { position: relative; width: 100vw; height: 420px; margin-top: -1.5rem; display: flex; justify-content: center; align-items: center; z-index: 10; pointer-events: auto; }
            spline-viewer { width: 100%; height: 100%; }

            .bottom-cards-dock { position: relative; z-index: 30; max-width: 1200px; width: 100%; margin: -4rem auto 2.5rem auto; padding: 0 32px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
            .liquid-micro-card { background: rgba(11, 15, 28, 0.65); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 18px 22px; box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.7), inset 0 1px 1px 0 rgba(255, 255, 255, 0.15); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
            .liquid-micro-card:hover { transform: translateY(-4px); border-color: rgba(255, 255, 255, 0.3); box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.9), inset 0 1px 1px 0 rgba(255, 255, 255, 0.3); }

            .micro-card-header { display: flex; justify-content: space-between; align-items: center; }
            .micro-badge-title { font-size: 0.72rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: #94A3B8; }
            .micro-main-text { font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin-top: 8px; line-height: 1.35; }
            .micro-stat { font-family: 'JetBrains Mono', monospace; font-size: 1.8rem; font-weight: 900; color: #FFFFFF; margin-top: 4px; }
            .progress-bar-wrap { width: 100%; height: 4px; background: rgba(255, 255, 255, 0.12); border-radius: 9999px; margin-top: 10px; overflow: hidden; }
            .progress-fill { height: 100%; background: linear-gradient(90deg, #6366F1, #38BDF8); border-radius: 9999px; }
        </style>
    </head>
    <body>
        <div class="cursor-spotlight" id="spotlight"></div>
        <div class="ambient-glow-top"></div>

        <nav class="navbar-container">
            <div class="nav-logo" onclick="navTo('/?view=landing')">SAPPM</div>
            <div class="nav-menu">
                <a class="nav-link" onclick="navTo('/?view=restricted')">Predict</a>
                <a class="nav-link" onclick="navTo('/?view=restricted')">Explainability</a>
                <a class="nav-link" onclick="navTo('/?view=restricted')">Analytics</a>
                <a class="nav-link" onclick="navTo('/?view=restricted')">Records</a>
                <a class="nav-link" onclick="navTo('/?view=restricted')">Documentation</a>
            </div>
            <div class="nav-actions">
                <div class="btn-star-login" onclick="navTo('/?view=auth')">Login</div>
                <div class="interactive-hover-btn" onclick="navTo('/?view=auth')">Sign Up →</div>
            </div>
        </nav>

        <section class="hero-section">
            <h1 class="hero-headline">Elevate Academic Intelligence</h1>
            <p class="hero-subhead">Forecast student performance trajectories with 99.81% precision, powered by Extreme Gradient Boosting & SHAP.</p>
            <button class="origin-btn" onclick="navTo('/?view=auth')">
                <span>Evaluate Performance</span>
                <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
            </button>
        </section>

        <div class="spline-stage-container">
            <spline-viewer id="splineViewer" url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
        </div>

        <div class="bottom-cards-dock">
            <div class="liquid-micro-card">
                <div class="micro-badge-title">Model Architecture</div>
                <div class="micro-main-text">Multiclass XGBoost</div>
            </div>
            <div class="liquid-micro-card">
                <div class="micro-badge-title">Model Accuracy</div>
                <div class="micro-stat">99.81%</div>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width: 99.81%;"></div></div>
            </div>
            <div class="liquid-micro-card">
                <div class="micro-badge-title">Active Inference</div>
                <div class="micro-stat">12ms</div>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width: 95%;"></div></div>
            </div>
            <div class="liquid-micro-card">
                <div class="micro-badge-title">Analyzed Records</div>
                <div class="micro-stat">1,000,000</div>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width: 100%;"></div></div>
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

            const spotlight = document.getElementById('spotlight');
            let currentX = window.innerWidth / 2;
            let currentY = window.innerHeight / 2;
            let targetX = currentX;
            let targetY = currentY;

            document.addEventListener('mousemove', (e) => {
                targetX = e.clientX;
                targetY = e.clientY;
                spotlight.style.opacity = '1';
            });

            document.addEventListener('mouseleave', () => {
                spotlight.style.opacity = '0';
            });

            function animate() {
                currentX += (targetX - currentX) * 0.12;
                currentY += (targetY - currentY) * 0.12;
                spotlight.style.left = `${currentX}px`;
                spotlight.style.top = `${currentY}px`;
                requestAnimationFrame(animate);
            }
            animate();

            const removeSplineLogo = () => {
                const viewer = document.getElementById('splineViewer');
                if (viewer && viewer.shadowRoot) {
                    const logo = viewer.shadowRoot.querySelector('#logo') || viewer.shadowRoot.querySelector('a[href*="spline"]');
                    if (logo) {
                        logo.style.display = 'none';
                        logo.style.opacity = '0';
                        logo.style.pointerEvents = 'none';
                        logo.remove();
                    }
                }
            };
            setInterval(removeSplineLogo, 200);
        </script>
    </body>
    </html>
    """
    components.html(landing_page_html, height=890, scrolling=False)


# =========================================================================
# VIEW 2: AUTHENTICATION (3D PERSPECTIVE TILT CARD + MOTION BARS LOADER)
# =========================================================================
elif st.session_state["current_view"] == "auth":
    err_msg_js = f"'{auth_error}'" if auth_error else "null"

    auth_component_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');
            * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; user-select: none; }}
            body {{ background-color: #05070E; color: #FFFFFF; width: 100%; min-height: 100vh; overflow-x: hidden; position: relative; display: flex; flex-direction: column; justify-content: center; align-items: center; padding-top: 1rem; }}

            .back-home-pill {{ position: fixed; top: 24px; left: 36px; z-index: 99999; display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px; border-radius: 9999px; background: rgba(15, 23, 42, 0.65); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.2); color: #CBD5E1; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; cursor: pointer; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }}
            .back-home-pill:hover {{ color: #FFFFFF; border-color: rgba(255, 255, 255, 0.4); background: rgba(15, 23, 42, 0.9); transform: translateX(-4px); }}

            .ambient-top {{ position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100vw; height: 500px; background: radial-gradient(circle, rgba(139, 92, 246, 0.22) 0%, rgba(99, 102, 241, 0.12) 40%, transparent 75%); filter: blur(80px); pointer-events: none; z-index: 1; }}

            .card-perspective-container {{ perspective: 1500px; width: 100%; max-width: 480px; margin: 0 auto; position: relative; z-index: 10; }}
            .tilt-card-wrapper {{ position: relative; border-radius: 28px; padding: 2px; overflow: hidden; background: rgba(255, 255, 255, 0.08); box-shadow: 0 30px 70px -15px rgba(0, 0, 0, 0.85); transform-style: preserve-3d; transition: transform 0.12s ease-out; }}
            .tilt-card-wrapper::before {{ content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: conic-gradient(transparent, transparent 65%, rgba(255, 255, 255, 0.9) 85%, #818CF8 95%, transparent); animation: rotateBorderBeam 4s linear infinite; z-index: 1; }}

            @keyframes rotateBorderBeam {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}

            .tilt-card {{ position: relative; z-index: 2; border-radius: 26px; background: rgba(11, 15, 28, 0.9); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px); padding: 34px 38px; }}
            .card-emblem {{ width: 46px; height: 46px; border-radius: 50%; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.15); display: flex; align-items: center; justify-content: center; margin: 0 auto 14px auto; font-weight: 900; font-size: 1.25rem; color: #FFFFFF; box-shadow: 0 0 25px rgba(139, 92, 246, 0.4); }}
            .card-header-title {{ text-align: center; font-size: 1.65rem; font-weight: 900; letter-spacing: -0.03em; color: #FFFFFF; margin-bottom: 4px; }}
            .card-header-sub {{ text-align: center; font-size: 0.85rem; color: #94A3B8; margin-bottom: 18px; }}

            .auth-error-banner {{ display: none; background: rgba(239, 68, 68, 0.15); border: 1px solid rgba(239, 68, 68, 0.4); border-radius: 12px; padding: 10px 14px; color: #F87171; font-size: 0.82rem; font-weight: 600; margin-bottom: 18px; text-align: center; }}
            .auth-toggle-bar {{ display: flex; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 9999px; padding: 4px; margin-bottom: 24px; }}
            .toggle-btn {{ flex: 1; text-align: center; padding: 8px 16px; border-radius: 9999px; font-size: 0.85rem; font-weight: 700; cursor: pointer; transition: all 0.25s ease; color: #94A3B8; }}
            .toggle-btn.active {{ background: #FFFFFF; color: #05070E; box-shadow: 0 4px 15px rgba(255, 255, 255, 0.25); }}

            .input-underline-group {{ position: relative; width: 100%; margin-bottom: 22px; padding-top: 14px; }}
            .input-group-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
            .floating-letters-wrapper {{ position: absolute; top: 18px; left: 0; pointer-events: none; display: flex; color: #94A3B8; font-size: 0.92rem; font-weight: 500; }}
            .letter-wave-char {{ display: inline-block; transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.25s ease; will-change: transform; }}
            .underline-field {{ width: 100%; background: transparent; border: none; border-bottom: 2px solid rgba(255, 255, 255, 0.2); padding: 6px 0 8px 0; color: #FFFFFF; font-size: 0.95rem; font-weight: 500; outline: none; transition: border-bottom-color 0.3s ease; }}
            .underline-field:focus {{ border-bottom-color: #FFFFFF; }}
            .input-underline-group.is-active .letter-wave-char {{ transform: translateY(-22px) scale(0.85); color: #E2E8F0; font-weight: 700; }}

            .password-toggle-btn {{ position: absolute; right: 0; bottom: 8px; cursor: pointer; color: #94A3B8; display: flex; align-items: center; justify-content: center; }}
            .password-toggle-btn svg {{ width: 18px; height: 18px; stroke: currentColor; }}

            .origin-submit-btn {{ width: 100%; position: relative; display: flex; align-items: center; justify-content: center; padding: 13px 28px; border-radius: 9999px; background: #FFFFFF; color: #05070E; font-size: 0.95rem; font-weight: 800; border: 1px solid rgba(255, 255, 255, 0.5); cursor: pointer; overflow: hidden; margin-top: 12px; box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.25), 0 0 15px 2px rgba(99, 102, 241, 0.25); transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1); }}
            .origin-submit-btn:hover {{ transform: translateY(-2px); box-shadow: 0 16px 35px rgba(255, 255, 255, 0.4), 0 0 25px rgba(56, 189, 248, 0.4); }}

            .bars-loader-overlay {{ display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 26px; background: rgba(8, 12, 24, 0.96); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); z-index: 50; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 30px; }}
            .motion-bars-wrap {{ display: flex; align-items: center; justify-content: center; gap: 7px; height: 42px; margin-bottom: 18px; }}
            .motion-bar-item {{ width: 7px; height: 42px; border-radius: 9999px; background: linear-gradient(180deg, #FFFFFF 0%, #818CF8 55%, #38BDF8 100%); transform-origin: bottom; animation: beuiBarsScale 1s cubic-bezier(0.42, 0, 0.58, 1) infinite; box-shadow: 0 0 16px rgba(129, 140, 248, 0.7); }}
            .motion-bar-item:nth-child(1) {{ animation-delay: 0s; }}
            .motion-bar-item:nth-child(2) {{ animation-delay: 0.12s; }}
            .motion-bar-item:nth-child(3) {{ animation-delay: 0.24s; }}
            .motion-bar-item:nth-child(4) {{ animation-delay: 0.36s; }}

            @keyframes beuiBarsScale {{ 0%, 100% {{ transform: scaleY(0.24); opacity: 0.45; }} 50% {{ transform: scaleY(1.0); opacity: 1; filter: drop-shadow(0 0 10px #38BDF8); }} }}
            .loader-status-title {{ font-size: 1.15rem; font-weight: 800; color: #FFFFFF; }}
            .footer-links {{ text-align: center; margin-top: 18px; font-size: 0.82rem; color: #64748B; }}
            .footer-links a {{ color: #CBD5E1; text-decoration: none; font-weight: 700; }}
        </style>
    </head>
    <body>
        <div class="back-home-pill" onclick="navTo('/?view=landing')">← Back to Home</div>
        <div class="ambient-top"></div>

        <div class="card-perspective-container">
            <div class="tilt-card-wrapper" id="tiltCardWrapper">
                <div class="tilt-card">
                    <div class="bars-loader-overlay" id="barsLoaderOverlay">
                        <div class="motion-bars-wrap">
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                            <span class="motion-bar-item"></span>
                        </div>
                        <div class="loader-status-title" id="loaderTitle">Signing in...</div>
                    </div>

                    <div class="card-emblem">S</div>
                    <h2 class="card-header-title" id="formTitle">Welcome Back</h2>
                    <p class="card-header-sub" id="formSub">Sign in to access student prediction analytics</p>

                    <div class="auth-error-banner" id="errorBanner"></div>

                    <div class="auth-toggle-bar">
                        <div class="toggle-btn active" id="tabSignIn" onclick="switchTab('signin')">Sign In</div>
                        <div class="toggle-btn" id="tabSignUp" onclick="switchTab('signup')">Create Account</div>
                    </div>

                    <form id="signInForm" onsubmit="handleAuthAction(event, 'signin')">
                        <div class="input-underline-group" id="grp_login_email">
                            <div class="floating-letters-wrapper" id="lbl_login_email"></div>
                            <input type="email" class="underline-field" id="login_email" autocomplete="off" required />
                        </div>
                        <div class="input-underline-group" id="grp_login_password">
                            <div class="floating-letters-wrapper" id="lbl_login_password"></div>
                            <input type="password" class="underline-field" id="login_password" autocomplete="off" required />
                            <div class="password-toggle-btn" onclick="togglePasswordEye('login_password', this)">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
                            </div>
                        </div>
                        <button type="submit" class="origin-submit-btn">Sign In to Portal</button>
                    </form>

                    <form id="signUpForm" style="display: none;" onsubmit="handleAuthAction(event, 'signup')">
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
                            </div>
                            <div class="input-underline-group" id="grp_signup_cpass">
                                <div class="floating-letters-wrapper" id="lbl_signup_cpass"></div>
                                <input type="password" class="underline-field" id="signup_cpass" autocomplete="off" required />
                            </div>
                        </div>
                        <button type="submit" class="origin-submit-btn">Register Staff Account</button>
                    </form>

                    <div class="footer-links" id="footerToggleText">
                        Don't have an account? <a href="javascript:switchTab('signup')">Sign up</a>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function navTo(url) {{
                try {{ if (window.parent && window.parent.location) {{ window.parent.location.assign(url); return; }} }} catch(e) {{}}
                window.location.assign(url);
            }}

            const serverError = {err_msg_js};
            const errorBanner = document.getElementById('errorBanner');
            if (serverError) {{ errorBanner.textContent = serverError; errorBanner.style.display = 'block'; }}

            const tiltCardWrapper = document.getElementById('tiltCardWrapper');
            document.addEventListener('mousemove', (e) => {{
                const rect = tiltCardWrapper.getBoundingClientRect();
                const cardX = rect.left + rect.width / 2;
                const cardY = rect.top + rect.height / 2;
                const rotateX = -((e.clientY - cardY) / (window.innerHeight / 2)) * 6;
                const rotateY = ((e.clientX - cardX) / (window.innerWidth / 2)) * 6;
                tiltCardWrapper.style.transform = `rotateX(${{rotateX}}deg) rotateY(${{rotateY}}deg)`;
            }});
            document.addEventListener('mouseleave', () => {{ tiltCardWrapper.style.transform = 'rotateX(0deg) rotateY(0deg)'; }});

            const setupSpringLetters = (inputId, labelId, labelText) => {{
                const input = document.getElementById(inputId);
                const labelContainer = document.getElementById(labelId);
                if (!input || !labelContainer) return;
                labelContainer.innerHTML = '';
                labelText.split('').forEach((char, idx) => {{
                    const span = document.createElement('span');
                    span.className = 'letter-wave-char';
                    span.textContent = char === ' ' ? '\\u00A0' : char;
                    span.style.transitionDelay = `${{idx * 0.03}}s`;
                    labelContainer.appendChild(span);
                }});
                const update = () => {{
                    if (document.activeElement === input || input.value.trim().length > 0) {{ input.parentElement.classList.add('is-active'); }}
                    else {{ input.parentElement.classList.remove('is-active'); }}
                }};
                input.addEventListener('focus', update);
                input.addEventListener('blur', update);
                input.addEventListener('input', update);
            }};

            setupSpringLetters('login_email', 'lbl_login_email', 'Email Address');
            setupSpringLetters('login_password', 'lbl_login_password', 'Password');
            setupSpringLetters('signup_fname', 'lbl_signup_fname', 'First Name');
            setupSpringLetters('signup_lname', 'lbl_signup_lname', 'Last Name');
            setupSpringLetters('signup_staffid', 'lbl_signup_staffid', 'Staff ID / Faculty No.');
            setupSpringLetters('signup_dept', 'lbl_signup_dept', 'Department / Faculty');
            setupSpringLetters('signup_email', 'lbl_signup_email', 'Institutional Email');
            setupSpringLetters('signup_pass', 'lbl_signup_pass', 'Password');
            setupSpringLetters('signup_cpass', 'lbl_signup_cpass', 'Confirm Password');

            function switchTab(tab) {{
                const sIn = document.getElementById('signInForm');
                const sUp = document.getElementById('signUpForm');
                const tIn = document.getElementById('tabSignIn');
                const tUp = document.getElementById('tabSignUp');
                const title = document.getElementById('formTitle');
                const sub = document.getElementById('formSub');
                const footer = document.getElementById('footerToggleText');
                if (tab === 'signup') {{
                    tIn.classList.remove('active'); tUp.classList.add('active');
                    sIn.style.display = 'none'; sUp.style.display = 'block';
                    title.textContent = 'Create Staff Account'; sub.textContent = 'Register your institutional credentials for access';
                    footer.innerHTML = 'Already have an account? <a href="javascript:switchTab(\\'signin\\')">Sign in</a>';
                }} else {{
                    tUp.classList.remove('active'); tIn.classList.add('active');
                    sUp.style.display = 'none'; sIn.style.display = 'block';
                    title.textContent = 'Welcome Back'; sub.textContent = 'Sign in to access student prediction analytics';
                    footer.innerHTML = 'Don\\'t have an account? <a href="javascript:switchTab(\\'signup\\')">Sign up</a>';
                }}
            }}

            function togglePasswordEye(id, btn) {{
                const input = document.getElementById(id);
                if (input.type === 'password') {{
                    input.type = 'text';
                    btn.innerHTML = '<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z\"></path><circle cx=\"12\" cy=\"12\" r=\"3\"></circle></svg>';
                }} else {{
                    input.type = 'password';
                    btn.innerHTML = '<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><path d=\"M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24\"></path><line x1=\"1\" y1=\"1\" x2=\"23\" y2=\"23\"></line></svg>';
                }}
            }}

            function handleAuthAction(event, action) {{
                event.preventDefault();
                if (action === 'signin') {{
                    const email = document.getElementById('login_email').value.trim();
                    const pass = document.getElementById('login_password').value;
                    if (!email || !pass) return;
                    document.getElementById('loaderTitle').textContent = 'Signing in...';
                    document.getElementById('barsLoaderOverlay').style.display = 'flex';
                    setTimeout(() => {{
                        navTo(`/?view=auth&action=signin&email=${{encodeURIComponent(email)}}&password=${{encodeURIComponent(pass)}}`);
                    }}, 450);
                }} else if (action === 'signup') {{
                    const fname = document.getElementById('signup_fname').value.trim();
                    const lname = document.getElementById('signup_lname').value.trim();
                    const staffid = document.getElementById('signup_staffid').value.trim();
                    const dept = document.getElementById('signup_dept').value.trim();
                    const email = document.getElementById('signup_email').value.trim();
                    const pass = document.getElementById('signup_pass').value;
                    const cpass = document.getElementById('signup_cpass').value;
                    if (!fname || !lname || !staffid || !dept || !email || !pass || !cpass || pass !== cpass) return;
                    document.getElementById('loaderTitle').textContent = 'Creating account...';
                    document.getElementById('barsLoaderOverlay').style.display = 'flex';
                    setTimeout(() => {{
                        navTo(`/?view=auth&action=signup&email=${{encodeURIComponent(email)}}&password=${{encodeURIComponent(pass)}}&c_password=${{encodeURIComponent(cpass)}}&fname=${{encodeURIComponent(fname)}}&lname=${{encodeURIComponent(lname)}}&staffid=${{encodeURIComponent(staffid)}}&dept=${{encodeURIComponent(dept)}}`);
                    }}, 450);
                }}
            }}
        </script>
    </body>
    </html>
    """
    components.html(auth_component_html, height=920, scrolling=False)


# =========================================================================
# VIEW 3: APPLICATION DASHBOARD (ORIGINAL PREDICTOR + SLIDER05 EQUALIZER)
# =========================================================================
elif st.session_state["current_view"] == "app":
    # Top navigation bar with active session badge & logout
    st.markdown("""
        <div style="max-width: 1300px; margin: 0 auto; padding: 24px 32px 10px 32px; display: flex; justify-content: space-between; align-items: center;">
            <a href="/?view=landing" target="_top" style="font-size: 1.35rem; font-weight: 900; color: #FFFFFF; text-decoration: none;">SAPPM</a>
            <div style="display: flex; gap: 32px;">
                <span style="color: #FFFFFF; font-size: 0.92rem; font-weight: 700;">Predictor Dashboard</span>
            </div>
            <div>
                <span style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 14px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 9999px; color: #34D399; font-size: 0.8rem; font-weight: 700;">
                    <span style="width: 7px; height: 7px; border-radius: 50%; background: #34D399; display: inline-block; box-shadow: 0 0 8px #34D399;"></span> Active Staff Session
                </span>
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
        if st.button("Sign Out", use_container_width=True):
            sign_out_staff()
            st.session_state["authenticated"] = False
            st.session_state["profile"] = None
            st.session_state["current_view"] = "landing"
            st.query_params.clear()
            st.query_params["view"] = "landing"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 16px; padding: 16px 20px; margin-bottom: 24px;">
            <p style="margin: 0; color: #CBD5E1; font-size: 0.95rem;">
                This system predicts a student's academic grade using Machine Learning. It also explains why the prediction was made using Explainable AI (SHAP).
            </p>
        </div>
    """, unsafe_allow_html=True)

    model, encoder, explainer, model_loaded = get_ml_pipeline()

    # Check if prediction was triggered via Slider05
    is_predict_req = st.query_params.get("predict") == "true"
    init_study = float(st.query_params.get("study", 10.0)) if is_predict_req else 10.0
    init_att = float(st.query_params.get("att", 75.0)) if is_predict_req else 75.0
    init_part = float(st.query_params.get("part", 5.0)) if is_predict_req else 5.0
    init_score = float(st.query_params.get("score", 50.0)) if is_predict_req else 50.0

    c_left, c_right = st.columns([1.1, 1], gap="large")

    with c_left:
        slider_05_component_html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');
                * {{ margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; user-select: none; }}
                body {{ background: transparent; color: #FFFFFF; padding: 6px 8px; }}
                .slider-group-wrap {{ position: relative; margin-bottom: 24px; }}
                .slider-label-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }}
                .slider-title {{ font-size: 0.85rem; font-weight: 700; color: #CBD5E1; letter-spacing: 0.02em; display: inline-flex; align-items: center; gap: 10px; cursor: pointer; transition: color 0.25s ease; }}
                .slider-group-wrap:hover .slider-title {{ color: #FFFFFF; }}
                .icon-box {{ display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 8px; background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1); }}
                .slider-group-wrap:hover .icon-box {{ background: rgba(255, 255, 255, 0.12); border-color: rgba(255, 255, 255, 0.3); transform: scale(1.14); box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4); }}
                .icon-box svg {{ width: 15px; height: 15px; stroke: #94A3B8; transition: all 0.35s cubic-bezier(0.34, 1.56, 0.64, 1); }}
                .slider-group-wrap:hover .icon-study svg {{ stroke: #818CF8; transform: rotate(-12deg) scale(1.18); filter: drop-shadow(0 0 6px rgba(129, 140, 248, 0.8)); }}
                .slider-group-wrap:hover .icon-att svg {{ stroke: #38BDF8; transform: rotate(12deg) scale(1.18); filter: drop-shadow(0 0 6px rgba(56, 189, 248, 0.8)); }}
                .slider-group-wrap:hover .icon-part svg {{ stroke: #34D399; transform: translateY(-3px) scale(1.2); filter: drop-shadow(0 0 6px rgba(52, 211, 153, 0.8)); }}
                .slider-group-wrap:hover .icon-score svg {{ stroke: #FBBF24; transform: rotate(18deg) scale(1.18); filter: drop-shadow(0 0 6px rgba(251, 191, 36, 0.8)); }}
                .slider-badge-val {{ font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #FFFFFF; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.12); padding: 2px 10px; border-radius: 8px; transition: all 0.25s ease; }}
                .slider-group-wrap:hover .slider-badge-val {{ border-color: rgba(255, 255, 255, 0.3); background: rgba(255, 255, 255, 0.1); box-shadow: 0 0 12px rgba(255, 255, 255, 0.15); }}
                .slider-05-container {{ position: relative; width: 100%; padding-top: 36px; }}
                .slider-05-track {{ position: relative; display: flex; align-items: flex-end; width: 100%; height: 36px; padding: 0 16px 12px 16px; background: #0B0F19; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 12px; cursor: pointer; touch-action: none; transition: height 0.3s cubic-bezier(0.16, 1, 0.3, 1), padding-bottom 0.3s ease, border-color 0.2s ease; overflow: hidden; }}
                .slider-05-track.is-active {{ height: 84px; padding-bottom: 16px; border-color: rgba(255, 255, 255, 0.4); }}
                .bars-wrapper {{ display: flex; align-items: flex-end; width: 100%; gap: 3px; }}
                .equalizer-bar {{ flex: 1; height: 10px; border-radius: 9999px; background: rgba(255, 255, 255, 0.15); transition: background 0.25s ease; will-change: height; }}
                .equalizer-bar.is-filled {{ background: #FFFFFF; z-index: 10; }}
                .floating-tooltip {{ position: absolute; top: 0px; transform: translate(-50%, 10px) scale(0.8); opacity: 0; pointer-events: none; background: #1E293B; color: #FFFFFF; font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 800; padding: 5px 16px; border-radius: 14px; border: 1px solid rgba(255, 255, 255, 0.18); box-shadow: 0 12px 30px -4px rgba(0, 0, 0, 0.7); transition: opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1), transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1); z-index: 30; white-space: nowrap; }}
                .slider-05-container.is-active .floating-tooltip {{ opacity: 1; transform: translate(-50%, -24px) scale(1); }}
                .predict-action-btn {{ width: 100%; padding: 13px 28px; border-radius: 9999px; background: #FFFFFF; color: #05070E; font-size: 0.95rem; font-weight: 800; border: 1px solid rgba(255, 255, 255, 0.5); box-shadow: 0 10px 25px -5px rgba(255, 255, 255, 0.25), 0 0 15px 2px rgba(99, 102, 241, 0.25); cursor: pointer; transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1); display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 18px; }}
                .predict-action-btn svg {{ transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }}
                .predict-action-btn:hover {{ transform: translateY(-2px); box-shadow: 0 16px 35px rgba(255, 255, 255, 0.4), 0 0 25px rgba(56, 189, 248, 0.4); }}
                .predict-action-btn:hover svg {{ transform: translateX(5px) scale(1.15); }}
                .predict-action-btn:active {{ transform: translateY(0); }}
            </style>
        </head>
        <body>
            <div class="slider-group-wrap">
                <div class="slider-label-row">
                    <span class="slider-title">
                        <span class="icon-box icon-study"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></span>
                        Weekly Self Study Hours
                    </span>
                    <span class="slider-badge-val" id="badge_study">{init_study} hrs</span>
                </div>
                <div class="slider-05-container" id="container_study">
                    <div class="floating-tooltip" id="tooltip_study">{init_study}</div>
                    <div class="slider-05-track" id="track_study"><div class="bars-wrapper" id="bars_study"></div></div>
                </div>
            </div>

            <div class="slider-group-wrap">
                <div class="slider-label-row">
                    <span class="slider-title">
                        <span class="icon-box icon-att"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg></span>
                        Attendance Percentage
                    </span>
                    <span class="slider-badge-val" id="badge_att">{init_att}%</span>
                </div>
                <div class="slider-05-container" id="container_att">
                    <div class="floating-tooltip" id="tooltip_att">{init_att}%</div>
                    <div class="slider-05-track" id="track_att"><div class="bars-wrapper" id="bars_att"></div></div>
                </div>
            </div>

            <div class="slider-group-wrap">
                <div class="slider-label-row">
                    <span class="slider-title">
                        <span class="icon-box icon-part"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></span>
                        Class Participation
                    </span>
                    <span class="slider-badge-val" id="badge_part">{init_part} / 10</span>
                </div>
                <div class="slider-05-container" id="container_part">
                    <div class="floating-tooltip" id="tooltip_part">{init_part}</div>
                    <div class="slider-05-track" id="track_part"><div class="bars-wrapper" id="bars_part"></div></div>
                </div>
            </div>

            <div class="slider-group-wrap">
                <div class="slider-label-row">
                    <span class="slider-title">
                        <span class="icon-box icon-score"><svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg></span>
                        Total Score
                    </span>
                    <span class="slider-badge-val" id="badge_score">{init_score} / 100</span>
                </div>
                <div class="slider-05-container" id="container_score">
                    <div class="floating-tooltip" id="tooltip_score">{init_score}</div>
                    <div class="slider-05-track" id="track_score"><div class="bars-wrapper" id="bars_score"></div></div>
                </div>
            </div>

            <button class="predict-action-btn" onclick="submitSlider05Prediction()">
                <span>Predict Grade</span>
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>

            <script>
                const NUM_BARS = 44;
                const PADDING = 16;
                const sliderConfigs = {{
                    study: {{ min: 0, max: 40, step: 0.5, value: {init_study}, suffix: ' hrs' }},
                    att: {{ min: 0, max: 100, step: 1, value: {init_att}, suffix: '%' }},
                    part: {{ min: 0, max: 10, step: 0.5, value: {init_part}, suffix: ' / 10' }},
                    score: {{ min: 0, max: 100, step: 1, value: {init_score}, suffix: ' / 100' }}
                }};

                function createSlider05(key, config) {{
                    const container = document.getElementById('container_' + key);
                    const track = document.getElementById('track_' + key);
                    const barsWrapper = document.getElementById('bars_' + key);
                    const tooltip = document.getElementById('tooltip_' + key);
                    const badge = document.getElementById('badge_' + key);

                    barsWrapper.innerHTML = '';
                    const barItems = [];
                    for (let i = 0; i < NUM_BARS; i++) {{
                        const bar = document.createElement('div');
                        bar.className = 'equalizer-bar';
                        barsWrapper.appendChild(bar);
                        barItems.push({{ el: bar, currentHeight: 10, targetHeight: 10 }});
                    }}

                    let isDragging = false;
                    let isHovering = false;
                    let targetMouseX = 0;
                    let smoothMouseX = 0;

                    function calculateValueFromX(x) {{
                        const rect = track.getBoundingClientRect();
                        const innerWidth = rect.width - PADDING * 2;
                        const pct = Math.max(0, Math.min(1, (x - PADDING) / innerWidth));
                        let rawVal = config.min + pct * (config.max - config.min);
                        return config.step >= 1 ? Math.round(rawVal) : Math.round(rawVal * 2) / 2;
                    }}

                    function handlePointerUpdate(e, shouldChangeVal) {{
                        const rect = track.getBoundingClientRect();
                        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
                        targetMouseX = Math.max(0, Math.min(rect.width, clientX - rect.left));
                        if (shouldChangeVal || isDragging) {{
                            const newVal = calculateValueFromX(targetMouseX);
                            config.value = newVal;
                            badge.textContent = newVal + config.suffix;
                        }}
                    }}

                    function renderFrame() {{
                        const active = isHovering || isDragging;
                        const rect = track.getBoundingClientRect();
                        const width = rect.width || 400;
                        const innerWidth = width - PADDING * 2;
                        const progress = (config.value - config.min) / (config.max - config.min);

                        smoothMouseX += (targetMouseX - smoothMouseX) * 0.22;
                        const normalHeight = 10, hoverBaseHeight = 50, dipHeight = 20, maxDistance = 140;

                        barItems.forEach((item, idx) => {{
                            const barProgress = idx / (NUM_BARS - 1);
                            const isFilled = barProgress <= progress;
                            if (isFilled) item.el.classList.add('is-filled'); else item.el.classList.remove('is-filled');

                            if (!active) {{ item.targetHeight = normalHeight; }}
                            else {{
                                const barX = PADDING + barProgress * innerWidth;
                                const dist = Math.abs(smoothMouseX - barX);
                                let tHeight = hoverBaseHeight;
                                if (dist < maxDistance) {{
                                    const relDist = dist / maxDistance;
                                    const dip = (Math.cos(relDist * Math.PI) + 1) / 2;
                                    tHeight = hoverBaseHeight - dip * (hoverBaseHeight - dipHeight);
                                }}
                                if (isFilled) {{
                                    const activeRange = barProgress / Math.max(progress, 0.01);
                                    tHeight += Math.sin(activeRange * Math.PI) * 6;
                                }}
                                item.targetHeight = Math.max(10, tHeight);
                            }}
                            item.currentHeight += (item.targetHeight - item.currentHeight) * 0.28;
                            item.el.style.height = item.currentHeight.toFixed(1) + 'px';
                        }});

                        if (active) {{
                            const clampedX = Math.max(PADDING, Math.min(width - PADDING, smoothMouseX));
                            tooltip.style.left = clampedX.toFixed(1) + 'px';
                            tooltip.textContent = config.value + config.suffix;
                        }}
                        requestAnimationFrame(renderFrame);
                    }}

                    track.addEventListener('mouseenter', (e) => {{ isHovering = true; container.classList.add('is-active'); track.classList.add('is-active'); handlePointerUpdate(e, false); smoothMouseX = targetMouseX; }});
                    track.addEventListener('mouseleave', () => {{ isHovering = false; if (!isDragging) {{ container.classList.remove('is-active'); track.classList.remove('is-active'); }} }});
                    track.addEventListener('mousemove', (e) => {{ handlePointerUpdate(e, isDragging); }});
                    track.addEventListener('mousedown', (e) => {{ isDragging = true; container.classList.add('is-active'); track.classList.add('is-active'); handlePointerUpdate(e, true); }});
                    window.addEventListener('mouseup', () => {{ if (isDragging) {{ isDragging = false; if (!isHovering) {{ container.classList.remove('is-active'); track.classList.remove('is-active'); }} }} }});
                    requestAnimationFrame(renderFrame);
                }}

                createSlider05('study', sliderConfigs.study);
                createSlider05('att', sliderConfigs.att);
                createSlider05('part', sliderConfigs.part);
                createSlider05('score', sliderConfigs.score);

                function submitSlider05Prediction() {{
                    const study = sliderConfigs.study.value;
                    const att = sliderConfigs.att.value;
                    const part = sliderConfigs.part.value;
                    const score = sliderConfigs.score.value;
                    const targetUrl = `/?view=app&predict=true&study=${{study}}&att=${{att}}&part=${{part}}&score=${{score}}`;
                    try {{ if (window.parent && window.parent.location) {{ window.parent.location.assign(targetUrl); return; }} }} catch(e) {{}}
                    window.location.assign(targetUrl);
                }}
            </script>
        </body>
        </html>
        """
        components.html(slider_05_component_html, height=520, scrolling=False)

    with c_right:
        if is_predict_req and model_loaded and model is not None and encoder is not None and explainer is not None:
            student_data = pd.DataFrame([{
                "weekly_self_study_hours": init_study,
                "attendance_percentage": init_att,
                "class_participation": init_part,
                "total_score": init_score
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
        elif is_predict_req and not model_loaded:
            st.error("Model assets could not be loaded. Please ensure model files are present in the models directory.")
        elif not is_predict_req:
            st.markdown("""
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px dashed rgba(255, 255, 255, 0.15); border-radius: 20px; padding: 4rem 2rem; text-align: center; margin-top: 1.5rem;">
                    <div style="display: flex; justify-content: center; margin-bottom: 1.2rem;">
                        <svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#64748B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>
                        </svg>
                    </div>
                    <h3 style="color: #FFFFFF; margin: 0 0 0.5rem 0;">Awaiting Input Submission</h3>
                    <p style="color: #94A3B8; font-size: 0.92rem; max-width: 380px; margin: 0 auto;">
                        Adjust the student metrics on the left and click <strong>Predict Grade</strong> to generate real-time grade forecasts, confidence attributions, and SHAP decision explanations.
                    </p>
                </div>
            """, unsafe_allow_html=True)


# =========================================================================
# VIEW 4: ACCESS RESTRICTED (MINIMALIST 404 PAGE)
# =========================================================================
elif st.session_state["current_view"] == "restricted":
    restricted_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');
            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; user-select: none; }
            body { background-color: #05070E; color: #FFFFFF; width: 100%; height: 100vh; overflow: hidden; position: relative; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
            .ambient-glow { position: absolute; top: 40%; left: 50%; transform: translate(-50%, -50%); width: 600px; height: 400px; background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(56, 189, 248, 0.08) 50%, transparent 75%); filter: blur(80px); pointer-events: none; z-index: 1; }
            .content-box { position: relative; z-index: 10; max-width: 480px; padding: 0 20px; }
            .badge-tag { display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; border-radius: 9999px; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12); color: #94A3B8; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 24px; }
            .error-code { font-family: 'JetBrains Mono', monospace; font-size: clamp(4.5rem, 10vw, 7rem); font-weight: 900; line-height: 1; letter-spacing: -0.05em; color: #FFFFFF; margin-bottom: 12px; }
            .error-title { font-size: 1.4rem; font-weight: 800; color: #FFFFFF; margin-bottom: 10px; }
            .error-desc { font-size: 0.95rem; color: #94A3B8; line-height: 1.5; margin-bottom: 32px; font-weight: 500; }
            .back-btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; padding: 12px 28px; border-radius: 9999px; background: #FFFFFF; color: #05070E; font-size: 0.88rem; font-weight: 800; text-decoration: none; border: 1px solid rgba(255, 255, 255, 0.5); cursor: pointer; transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1); }
            .back-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(255, 255, 255, 0.35); }
        </style>
    </head>
    <body>
        <div class="ambient-glow"></div>
        <div class="content-box">
            <div class="badge-tag">Status 404</div>
            <div class="error-code">404</div>
            <h1 class="error-title">Page Not Found</h1>
            <p class="error-desc">The page or module you are looking for doesn't exist or is currently unavailable.</p>
            <div class="back-btn" onclick="navTo('/?view=landing')">← Back to Home</div>
        </div>
        <script>
            function navTo(url) {
                try { if (window.parent && window.parent.location) { window.parent.location.assign(url); return; } } catch(e) {}
                window.location.assign(url);
            }
        </script>
    </body>
    </html>
    """
    components.html(restricted_html, height=750, scrolling=False)