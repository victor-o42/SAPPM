"""
S.A.P.P.M - Ultra-Sleek Minimalist 3D Intelligence Landing Page
Inspired by Roobinium Design:
- Dynamic mouse-following radial spotlight shadow & glow
- Floating glass island navbar with Login & Sign Up CTA pills
- Clean, uncluttered centered typography with generous whitespace
- Centerpiece 3D interactive robot tracking cursor with organic physics
- Cleaned canvas with Spline badge removed
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SAPPM - Student Academic Performance Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ultra-clean CSS: hide default Streamlit chrome & sidebar completely
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    /* Hide Streamlit default sidebar and top decoration */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        display: none !important;
    }
    #MainMenu, footer {
        visibility: hidden !important;
    }

    /* Canvas background */
    html, body, [class*="css"], .stApp {
        background-color: #070913 !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
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

# Complete Roobinium-Style Hero Component with Spotlight & Badge Removed
roobinium_hero_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.72/build/spline-viewer.js"></script>
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
            background-color: #070913;
            color: #FFFFFF;
            width: 100vw;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        /* 1. Dynamic Cursor-Tracking Spotlight Glow */
        .cursor-spotlight {
            position: fixed;
            width: 600px;
            height: 600px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.16) 0%, rgba(56, 189, 248, 0.08) 35%, rgba(139, 92, 246, 0.03) 55%, transparent 70%);
            filter: blur(40px);
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: 2;
            transition: opacity 0.3s ease;
            opacity: 0;
            will-change: left, top;
        }

        /* Ambient Static Lighting */
        .ambient-glow {
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 900px;
            height: 550px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, rgba(56, 189, 248, 0.04) 50%, transparent 80%);
            filter: blur(70px);
            pointer-events: none;
            z-index: 1;
        }

        /* 2. Sleek Floating Island Navbar */
        .navbar-container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 24px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            z-index: 50;
        }

        .nav-logo {
            font-size: 1.25rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .nav-menu {
            display: flex;
            align-items: center;
            gap: 32px;
        }

        .nav-link {
            color: #94A3B8;
            font-size: 0.9rem;
            font-weight: 500;
            text-decoration: none;
            transition: color 0.2s ease;
            cursor: pointer;
        }
        .nav-link:hover {
            color: #FFFFFF;
        }

        .nav-actions {
            display: flex;
            align-items: center;
            gap: 16px;
        }

        .btn-ghost {
            background: transparent;
            border: none;
            color: #E2E8F0;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            padding: 8px 16px;
            transition: color 0.2s ease;
        }
        .btn-ghost:hover {
            color: #FFFFFF;
        }

        .btn-pill-white {
            background: #FFFFFF;
            color: #070913;
            border: none;
            border-radius: 9999px;
            padding: 10px 22px;
            font-size: 0.9rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 15px rgba(255, 255, 255, 0.2);
        }
        .btn-pill-white:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.35);
        }

        /* 3. Centered Minimalist Hero Header */
        .hero-section {
            text-align: center;
            padding-top: 2rem;
            position: relative;
            z-index: 10;
            max-width: 900px;
            margin: 0 auto;
        }

        .hero-title {
            font-size: 3.8rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 1.15;
            color: #FFFFFF;
            margin-bottom: 1rem;
        }

        .hero-subtitle {
            font-size: 1.1rem;
            color: #94A3B8;
            font-weight: 400;
            max-width: 580px;
            margin: 0 auto 2rem auto;
            line-height: 1.6;
        }

        .hero-cta {
            background: #FFFFFF;
            color: #070913;
            border: none;
            border-radius: 9999px;
            padding: 14px 34px;
            font-size: 0.95rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 10px 30px rgba(255, 255, 255, 0.25);
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .hero-cta:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 15px 40px rgba(255, 255, 255, 0.4);
        }

        /* 4. 3D Spline Canvas Container */
        .spline-stage {
            position: relative;
            width: 100%;
            height: 520px;
            margin-top: -30px;
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        spline-viewer {
            width: 100%;
            height: 100%;
            pointer-events: auto;
        }

        /* 5. Floating Frosted Glass Micro-Cards */
        .card-floating-left {
            position: absolute;
            left: calc(50% - 480px);
            bottom: 80px;
            z-index: 20;
            background: rgba(18, 24, 40, 0.65);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 18px 24px;
            width: 230px;
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
        }
        .card-floating-left:hover {
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px);
        }

        .card-floating-right {
            position: absolute;
            right: calc(50% - 480px);
            bottom: 80px;
            z-index: 20;
            background: rgba(18, 24, 40, 0.65);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 18px 24px;
            width: 230px;
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
        }
        .card-floating-right:hover {
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px);
        }

        .micro-tag {
            font-size: 0.72rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 700;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .arrow-chip {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.65rem;
            color: #FFFFFF;
        }

        .micro-main-text {
            font-size: 1.05rem;
            font-weight: 700;
            color: #FFFFFF;
            margin-top: 8px;
            line-height: 1.35;
        }

        .micro-stat {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.8rem;
            font-weight: 900;
            color: #FFFFFF;
            margin-top: 4px;
        }

        .progress-bar-wrap {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 9999px;
            margin-top: 10px;
            overflow: hidden;
        }
        .progress-fill {
            width: 96%;
            height: 100%;
            background: linear-gradient(90deg, #6366F1, #38BDF8);
            border-radius: 9999px;
        }

        @media (max-width: 950px) {
            .hero-title { font-size: 2.5rem; }
            .card-floating-left, .card-floating-right { display: none; }
            .spline-stage { height: 420px; }
            .nav-menu { display: none; }
        }
    </style>
</head>
<body>
    <!-- Spotlight mouse-follower element -->
    <div class="cursor-spotlight" id="spotlight"></div>
    <div class="ambient-glow"></div>

    <!-- 1. Sleek Floating Navbar -->
    <nav class="navbar-container">
        <div class="nav-logo">
            <span>SAPPM</span>
        </div>

        <div class="nav-menu">
            <a class="nav-link" onclick="window.parent.location.href='/Predict'">Predict</a>
            <a class="nav-link" onclick="window.parent.location.href='/Explainability'">Explainability</a>
            <a class="nav-link" onclick="window.parent.location.href='/Model_Analytics'">Analytics</a>
            <a class="nav-link" onclick="window.parent.location.href='/Student_Records'">Records</a>
            <a class="nav-link" onclick="window.parent.location.href='/Documentation'">Documentation</a>
        </div>

        <div class="nav-actions">
            <button class="btn-ghost" onclick="window.parent.location.href='/Staff_Portal'">Login</button>
            <button class="btn-pill-white" onclick="window.parent.location.href='/Predict'">Launch Studio</button>
        </div>
    </nav>

    <!-- 2. Centered Typography -->
    <section class="hero-section">
        <h1 class="hero-title">Elevate Academic Intelligence</h1>
        <p class="hero-subtitle">
            Forecast student performance trajectories with 99.81% precision, powered by Extreme Gradient Boosting & SHAP.
        </p>
        <button class="hero-cta" onclick="window.parent.location.href='/Predict'">
            Evaluate Performance ↗
        </button>
    </section>

    <!-- 3. 3D Spline Canvas -->
    <div class="spline-stage">
        <spline-viewer id="splineViewer" url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
        
        <!-- Floating Left Card -->
        <div class="card-floating-left">
            <div class="micro-tag">
                <span>Model Architecture</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-main-text">Multiclass XGBoost Engine</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill"></div>
            </div>
        </div>

        <!-- Floating Right Card -->
        <div class="card-floating-right">
            <div class="micro-tag">
                <span>Model Accuracy</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-stat">99.81%</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill" style="width: 99.8%;"></div>
            </div>
        </div>
    </div>

    <!-- Spotlight cursor physics & Spline logo remover script -->
    <script>
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

        // Smooth physics interpolation loop
        function animate() {
            currentX += (targetX - currentX) * 0.12;
            currentY += (targetY - currentY) * 0.12;
            spotlight.style.left = `${currentX}px`;
            spotlight.style.top = `${currentY}px`;
            requestAnimationFrame(animate);
        }
        animate();

        // Remove Spline watermark badge automatically
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

# Render Full-Height Hero Viewport with Spotlight & Cleaned Badge
components.html(roobinium_hero_html, height=840)

# Quick Streamlit Navigation Actions Below
st.markdown("""
    <div style="max-width: 1100px; margin: 0 auto 4rem auto; padding: 0 1.5rem;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
            <div style="background: rgba(18, 24, 40, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 0.75rem; color: #818CF8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Prediction Service</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #FFFFFF; margin: 0.4rem 0 1rem 0;">Student Forecast</div>
                <a href="/Predict" target="_self" style="display: inline-block; background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.4); color: #FFFFFF; padding: 8px 18px; border-radius: 9999px; font-weight: 600; text-decoration: none; font-size: 0.85rem;">Open Predictor ↗</a>
            </div>
            <div style="background: rgba(18, 24, 40, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 0.75rem; color: #34D399; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Explainability</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #FFFFFF; margin: 0.4rem 0 1rem 0;">SHAP Attribution</div>
                <a href="/Explainability" target="_self" style="display: inline-block; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.4); color: #FFFFFF; padding: 8px 18px; border-radius: 9999px; font-weight: 600; text-decoration: none; font-size: 0.85rem;">Inspect SHAP ↗</a>
            </div>
            <div style="background: rgba(18, 24, 40, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 0.75rem; color: #60A5FA; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Model Registry</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #FFFFFF; margin: 0.4rem 0 1rem 0;">Algorithm Benchmarks</div>
                <a href="/Model_Analytics" target="_self" style="display: inline-block; background: rgba(59, 130, 246, 0.2); border: 1px solid rgba(59, 130, 246, 0.4); color: #FFFFFF; padding: 8px 18px; border-radius: 9999px; font-weight: 600; text-decoration: none; font-size: 0.85rem;">View Analytics ↗</a>
            </div>
            <div style="background: rgba(18, 24, 40, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 18px; padding: 1.5rem; text-align: center;">
                <div style="font-size: 0.75rem; color: #FBBF24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;">Database Logs</div>
                <div style="font-size: 1.2rem; font-weight: 800; color: #FFFFFF; margin: 0.4rem 0 1rem 0;">Student Records</div>
                <a href="/Student_Records" target="_self" style="display: inline-block; background: rgba(245, 158, 11, 0.2); border: 1px solid rgba(245, 158, 11, 0.4); color: #FFFFFF; padding: 8px 18px; border-radius: 9999px; font-weight: 600; text-decoration: none; font-size: 0.85rem;">Browse Logs ↗</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)