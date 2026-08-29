"""
S.A.P.P.M - Ultra-Sleek Minimalist 3D Intelligence Landing Page
Full-Viewport Agency Experience with 3 High-End 21st.dev Buttons:
1. Center CTA: Origin Button (Pointer-origin radial expansion fill + animated breathing neon shadow)
2. Navbar Login: Star Button (Constellation starfield SVG with circulating perimeter light beam)
3. Navbar Sign Up: Interactive Hover Button by Dillion Verma (Magic UI expanding dot & arrow slide)
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

# Complete Roobinium 4-Card Hero Viewport with 3 High-End 21st.dev Animated Buttons
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

        /* 1. Dynamic Cursor Spotlight */
        .cursor-spotlight {
            position: fixed;
            width: 650px;
            height: 650px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.35) 0%, rgba(56, 189, 248, 0.22) 30%, rgba(139, 92, 246, 0.1) 50%, transparent 70%);
            filter: blur(40px);
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
            background: radial-gradient(circle, rgba(99, 102, 241, 0.18) 0%, rgba(56, 189, 248, 0.08) 50%, transparent 80%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 1;
        }

        /* Navbar Container */
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

        /* ==========================================================
           BUTTON 2: STAR BUTTON (Login) - 21st.dev
           ========================================================== */
        .star-button-wrapper {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 2px;
            border-radius: 9999px;
            overflow: hidden;
            cursor: pointer;
            text-decoration: none;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            transition: all 0.3s ease;
        }
        .star-button-wrapper:hover {
            border-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
            transform: translateY(-1px);
        }

        .star-button-inner {
            position: relative;
            z-index: 2;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 20px;
            border-radius: 9999px;
            background: #090D1A;
            color: #E2E8F0;
            font-size: 0.9rem;
            font-weight: 600;
            overflow: hidden;
        }

        .star-svg-bg {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            opacity: 0.35;
            pointer-events: none;
        }

        .star-orbit-beam {
            position: absolute;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: radial-gradient(circle, #818CF8 0%, #38BDF8 50%, transparent 80%);
            filter: blur(6px);
            animation: starBeamOrbit 4s linear infinite;
            z-index: 1;
        }

        @keyframes starBeamOrbit {
            0% { top: -25px; left: -25px; }
            25% { top: -25px; left: calc(100% - 25px); }
            50% { top: calc(100% - 25px); left: calc(100% - 25px); }
            75% { top: calc(100% - 25px); left: -25px; }
            100% { top: -25px; left: -25px; }
        }

        /* ==========================================================
           BUTTON 3: INTERACTIVE HOVER BUTTON (Sign Up) - by Dillion Verma (Magic UI)
           ========================================================== */
        .interactive-hover-btn {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 9px 24px;
            border-radius: 9999px;
            background: #FFFFFF;
            color: #05070E;
            font-size: 0.92rem;
            font-weight: 700;
            cursor: pointer;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.4);
            box-shadow: 0 4px 18px rgba(255, 255, 255, 0.25);
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .interactive-hover-btn .btn-text-content {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            position: relative;
            z-index: 2;
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), color 0.3s ease;
        }

        .interactive-hover-btn .btn-dot {
            width: 6px;
            height: 6px;
            background: #05070E;
            border-radius: 50%;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .interactive-hover-btn .btn-arrow-slide {
            position: absolute;
            right: 18px;
            opacity: 0;
            transform: translateX(10px);
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            font-size: 1rem;
            color: #FFFFFF;
            z-index: 2;
        }

        .interactive-hover-btn .expanding-circle {
            position: absolute;
            right: 22px;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #4F46E5;
            transition: transform 0.45s cubic-bezier(0.16, 1, 0.3, 1);
            transform: scale(0);
            z-index: 1;
        }

        .interactive-hover-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(79, 70, 229, 0.45);
        }
        .interactive-hover-btn:hover .expanding-circle {
            transform: scale(38);
        }
        .interactive-hover-btn:hover .btn-text-content {
            transform: translateX(-12px);
            color: #FFFFFF;
        }
        .interactive-hover-btn:hover .btn-dot {
            opacity: 0;
        }
        .interactive-hover-btn:hover .btn-arrow-slide {
            opacity: 1;
            transform: translateX(0);
        }

        /* Centered Hero Header */
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

        /* ==========================================================
           BUTTON 1: ORIGIN BUTTON (Evaluate Performance) - 21st.dev
           Animated pointer-origin expansion + pulsing breathing shadow
           ========================================================== */
        .origin-button {
            position: relative;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 14px 38px;
            border-radius: 9999px;
            background: #FFFFFF;
            color: #05070E;
            font-size: 0.98rem;
            font-weight: 800;
            cursor: pointer;
            overflow: hidden;
            border: 1px solid rgba(255, 255, 255, 0.5);
            animation: breathingShadow 3s ease-in-out infinite alternate;
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 10;
        }

        @keyframes breathingShadow {
            0% {
                box-shadow: 0 10px 30px -5px rgba(255, 255, 255, 0.3), 0 0 15px 2px rgba(99, 102, 241, 0.3);
            }
            50% {
                box-shadow: 0 18px 45px -2px rgba(255, 255, 255, 0.5), 0 0 28px 6px rgba(56, 189, 248, 0.5);
            }
            100% {
                box-shadow: 0 12px 35px -4px rgba(255, 255, 255, 0.35), 0 0 20px 4px rgba(99, 102, 241, 0.4);
            }
        }

        .origin-button:hover {
            transform: translateY(-2px) scale(1.02);
            animation: none;
            box-shadow: 0 20px 50px rgba(99, 102, 241, 0.6), 0 0 35px rgba(56, 189, 248, 0.7);
        }

        .origin-button .origin-ripple {
            position: absolute;
            border-radius: 50%;
            background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%);
            transform: translate(-50%, -50%) scale(0);
            pointer-events: none;
            transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1;
        }

        .origin-button.active .origin-ripple {
            transform: translate(-50%, -50%) scale(1);
        }

        .origin-button .button-label {
            position: relative;
            z-index: 2;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            transition: color 0.3s ease;
        }
        .origin-button.active .button-label {
            color: #FFFFFF;
        }

        /* 3D Spline Canvas Container */
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

        /* Translucent Liquid Glass Micro-Cards */
        .floating-card {
            position: absolute;
            z-index: 20;
            background: rgba(15, 23, 42, 0.35);
            backdrop-filter: blur(10px) saturate(180%);
            -webkit-backdrop-filter: blur(10px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.14);
            border-radius: 20px;
            padding: 18px 24px;
            width: 235px;
            box-shadow: 0 15px 35px 0 rgba(0, 0, 0, 0.45), inset 0 1px 1px 0 rgba(255, 255, 255, 0.22);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .floating-card:hover {
            background: rgba(15, 23, 42, 0.45);
            border-color: rgba(255, 255, 255, 0.28);
            transform: translateY(-3px);
            box-shadow: 0 20px 45px 0 rgba(99, 102, 241, 0.25), inset 0 1px 1px 0 rgba(255, 255, 255, 0.3);
        }

        .card-top-left { left: calc(50% - 410px); top: 110px; }
        .card-top-right { right: calc(50% - 410px); top: 110px; }
        .card-bottom-left { left: calc(50% - 410px); bottom: 60px; }
        .card-bottom-right { right: calc(50% - 410px); bottom: 60px; }

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
            background: rgba(255, 255, 255, 0.1);
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
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
        }

        .micro-stat {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.8rem;
            font-weight: 900;
            color: #FFFFFF;
            margin-top: 4px;
            text-shadow: 0 2px 12px rgba(0, 0, 0, 0.7);
        }

        .progress-bar-wrap {
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.12);
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
            <!-- BUTTON 2: STAR BUTTON (Login) -->
            <div class="star-button-wrapper" onclick="window.parent.location.href='/Staff_Portal'">
                <div class="star-orbit-beam"></div>
                <div class="star-button-inner">
                    <svg class="star-svg-bg" viewBox="0 0 100 40" fill="none">
                        <path d="M32.34 26.68C32.34 26.3152 32.0445 26.02 31.68 26.02C31.3155 26.02 31.02 26.3152 31.02 26.68Z" fill="white" />
                        <path d="M56.1 3.96C56.4645 3.96 56.76 4.25519 56.76 4.62C56.76 4.98481 56.4645 5.28 56.1 5.28Z" fill="white" />
                        <path d="M74.58 5.28C74.7701 5.28 74.9413 5.36057 75.0618 5.48882Z" fill="white" />
                        <path d="M19.32 18.48C19.32 18.1152 19.0245 17.82 18.66 17.82Z" fill="white" />
                        <path d="M85.66 24.34C86.0245 24.34 86.32 24.6352 86.32 25Z" fill="white" />
                    </svg>
                    <span>Login</span>
                </div>
            </div>

            <!-- BUTTON 3: INTERACTIVE HOVER BUTTON by Dillion Verma (Sign Up) -->
            <div class="interactive-hover-btn" onclick="window.parent.location.href='/Staff_Portal'">
                <div class="expanding-circle"></div>
                <span class="btn-text-content">
                    <span>Sign Up</span>
                    <span class="btn-dot"></span>
                </span>
                <span class="btn-arrow-slide">→</span>
            </div>
        </div>
    </nav>

    <!-- 2. Centered Typography -->
    <section class="hero-section">
        <h1 class="hero-title">Elevate Academic Intelligence</h1>
        <p class="hero-subtitle">
            Forecast student performance trajectories with 99.81% precision, powered by Extreme Gradient Boosting & SHAP.
        </p>
        
        <!-- BUTTON 1: ORIGIN BUTTON (Evaluate Performance) -->
        <button class="origin-button" id="originBtn" onclick="window.parent.location.href='/Predict'">
            <div class="origin-ripple" id="originRipple"></div>
            <span class="button-label">
                Evaluate Performance ↗
            </span>
        </button>
    </section>

    <!-- 3. 3D Spline Centerpiece with 4 Translucent Liquid Glass Cards -->
    <div class="spline-stage">
        <spline-viewer id="splineViewer" url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
        
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

    <!-- Scripts for Spotlight, Origin Button & Watermark removal -->
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

        // Origin Button calculation logic
        const originBtn = document.getElementById('originBtn');
        const originRipple = document.getElementById('originRipple');

        if (originBtn && originRipple) {
            originBtn.addEventListener('mouseenter', (e) => {
                const rect = originBtn.getBoundingClientRect();
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

                originRipple.style.left = `${x}px`;
                originRipple.style.top = `${y}px`;
                originRipple.style.width = `${diameter}px`;
                originRipple.style.height = `${diameter}px`;
                originBtn.classList.add('active');
            });

            originBtn.addEventListener('mouseleave', () => {
                originBtn.classList.remove('active');
            });
        }

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