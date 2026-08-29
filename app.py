"""
S.A.P.P.M - Ultra-Sleek Minimalist 3D Intelligence Landing Page
Full-Viewport Agency Experience:
- Floating glass island navbar with direct links & CTA
- Centered typography with Evaluate Performance action
- Centerpiece 3D robot tracking cursor framed by 4 unified Roobinium frosted glass micro-cards:
    1. Top-Left: Model Architecture (Multiclass XGBoost Engine)
    2. Top-Right: Model Accuracy (99.81%)
    3. Bottom-Left: Inference Speed (< 15ms)
    4. Bottom-Right: Dataset Records (1,000,000)
- Unified color palette: Consistent Indigo-to-Cyan gradient bars & pure white typography
- Tight, balanced framing closer to the robot
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

    html, body, [class*="css"], .stApp {
        background-color: #05070E !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #FFFFFF !important;
        overflow: hidden !important;
        height: 100vh !important;
        width: 100vw !important;
    }

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Complete Roobinium 4-Card Hero Viewport
roobinium_full_viewport_html = """
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
            background-color: #05070E;
            color: #FFFFFF;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Dynamic Cursor Spotlight */
        .cursor-spotlight {
            position: fixed;
            width: 650px;
            height: 650px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.16) 0%, rgba(56, 189, 248, 0.08) 35%, rgba(139, 92, 246, 0.03) 55%, transparent 70%);
            filter: blur(45px);
            pointer-events: none;
            transform: translate(-50%, -50%);
            z-index: 2;
            transition: opacity 0.3s ease;
            opacity: 0;
            will-change: left, top;
        }

        /* Ambient Nebula Glow */
        .ambient-glow-top {
            position: absolute;
            top: 25%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 900px;
            height: 550px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, rgba(56, 189, 248, 0.04) 50%, transparent 80%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 1;
        }

        /* 1. Sleek Floating Island Navbar */
        .navbar-container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
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

        .nav-menu {
            display: flex;
            align-items: center;
            gap: 36px;
        }

        .nav-link {
            color: #94A3B8;
            font-size: 0.92rem;
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
            color: #CBD5E1;
            font-size: 0.92rem;
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
            color: #05070E;
            border: none;
            border-radius: 9999px;
            padding: 10px 24px;
            font-size: 0.92rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 18px rgba(255, 255, 255, 0.2);
        }
        .btn-pill-white:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(255, 255, 255, 0.35);
        }

        /* 2. Centered Minimalist Hero Header */
        .hero-section {
            text-align: center;
            padding-top: 0.75rem;
            position: relative;
            z-index: 10;
            max-width: 900px;
            margin: 0 auto;
        }

        .hero-title {
            font-size: 3.6rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            line-height: 1.12;
            color: #FFFFFF;
            margin-bottom: 0.6rem;
        }

        .hero-subtitle {
            font-size: 1.08rem;
            color: #94A3B8;
            font-weight: 400;
            max-width: 600px;
            margin: 0 auto 1.35rem auto;
            line-height: 1.55;
        }

        .hero-cta {
            background: #FFFFFF;
            color: #05070E;
            border: none;
            border-radius: 9999px;
            padding: 13px 34px;
            font-size: 0.95rem;
            font-weight: 800;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 10px 35px rgba(255, 255, 255, 0.25);
            display: inline-flex;
            align-items: center;
            gap: 10px;
        }
        .hero-cta:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 15px 45px rgba(255, 255, 255, 0.4);
        }

        /* 3. 3D Spline Canvas Container */
        .spline-stage {
            position: relative;
            width: 100%;
            height: 560px;
            margin-top: -20px;
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

        /* 4 Floating Roobinium Micro-Cards (Unified Exact Aesthetic & Closer Proportions) */
        .floating-card {
            position: absolute;
            z-index: 20;
            background: rgba(18, 24, 40, 0.65);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 18px 24px;
            width: 235px;
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .floating-card:hover {
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-3px);
        }

        /* Balanced Tight Proportions Closer to the Robot */
        .card-top-left {
            left: calc(50% - 410px);
            top: 110px;
        }

        .card-top-right {
            right: calc(50% - 410px);
            top: 110px;
        }

        .card-bottom-left {
            left: calc(50% - 410px);
            bottom: 60px;
        }

        .card-bottom-right {
            right: calc(50% - 410px);
            bottom: 60px;
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

        /* Unified Gradient Bar Across All 4 Cards */
        .progress-bar-wrap {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 9999px;
            margin-top: 10px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #6366F1, #38BDF8);
            border-radius: 9999px;
        }

        @media (max-width: 1000px) {
            .card-top-left { left: 20px; top: 80px; }
            .card-top-right { right: 20px; top: 80px; }
            .card-bottom-left { left: 20px; bottom: 40px; }
            .card-bottom-right { right: 20px; bottom: 40px; }
        }

        @media (max-width: 800px) {
            .hero-title { font-size: 2.4rem; }
            .floating-card { display: none; }
            .nav-menu { display: none; }
            .spline-stage { height: 420px; }
        }
    </style>
</head>
<body>
    <!-- Dynamic Spotlight -->
    <div class="cursor-spotlight" id="spotlight"></div>
    <div class="ambient-glow-top"></div>

    <!-- 1. Sleek Floating Navbar -->
    <nav class="navbar-container">
        <a class="nav-logo" onclick="window.parent.location.href='/'">
            <span>SAPPM</span>
        </a>

        <div class="nav-menu">
            <a class="nav-link" onclick="window.parent.location.href='/Predict'">Predict</a>
            <a class="nav-link" onclick="window.parent.location.href='/Explainability'">Explainability</a>
            <a class="nav-link" onclick="window.parent.location.href='/Model_Analytics'">Analytics</a>
            <a class="nav-link" onclick="window.parent.location.href='/Student_Records'">Records</a>
            <a class="nav-link" onclick="window.parent.location.href='/Documentation'">Documentation</a>
        </div>

        <div class="nav-actions">
            <button class="btn-ghost" onclick="window.parent.location.href='/Staff_Portal'">Login</button>
            <button class="btn-pill-white" onclick="window.parent.location.href='/Predict'">Evaluate Now</button>
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

    <!-- 3. 3D Spline Centerpiece with 4 Unified Floating Cards -->
    <div class="spline-stage">
        <spline-viewer id="splineViewer" url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
        
        <!-- 1. Top-Left Card: Model Architecture -->
        <div class="floating-card card-top-left">
            <div class="micro-tag">
                <span>Model Architecture</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-main-text">Multiclass XGBoost Engine</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill" style="width: 95%;"></div>
            </div>
        </div>

        <!-- 2. Top-Right Card: Model Accuracy -->
        <div class="floating-card card-top-right">
            <div class="micro-tag">
                <span>Model Accuracy</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-stat">99.81%</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill" style="width: 99.8%;"></div>
            </div>
        </div>

        <!-- 3. Bottom-Left Card: Inference Speed -->
        <div class="floating-card card-bottom-left">
            <div class="micro-tag">
                <span>Inference Speed</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-stat">&lt; 15ms</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill" style="width: 96%;"></div>
            </div>
        </div>

        <!-- 4. Bottom-Right Card: Dataset Records -->
        <div class="floating-card card-bottom-right">
            <div class="micro-tag">
                <span>Dataset Records</span>
                <div class="arrow-chip">↗</div>
            </div>
            <div class="micro-stat">1,000,000</div>
            <div class="progress-bar-wrap">
                <div class="progress-fill" style="width: 100%;"></div>
            </div>
        </div>
    </div>

    <!-- Spotlight physics & watermark remover script -->
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

# Render Full-Viewport Experience (Fixed 100vh)
components.html(roobinium_full_viewport_html, height=920, scrolling=False)