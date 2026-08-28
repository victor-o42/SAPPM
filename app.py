"""
S.A.P.P.M - Next-Generation AI Intelligence Platform
Engineered to match Blendr.ai & Roobinium Agency Standards:
- Floating glass island navbar
- Interactive 3D robot centerpiece with dynamic spotlight physics
- Minimalist metric counters (Finomac style)
- Large cinematic feature showcases with eyebrow chips (Blendr style)
- Minimalist closing CTA and footer
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
    </style>
""", unsafe_allow_html=True)

# Complete Blendr.ai + Roobinium + Finomac Experience
complete_landing_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.72/build/spline-viewer.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&display=swap');

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
        }

        /* 1. Dynamic Cursor-Tracking Spotlight Glow */
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

        /* Ambient Lighting */
        .ambient-glow-top {
            position: absolute;
            top: 15%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 900px;
            height: 550px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, rgba(56, 189, 248, 0.04) 50%, transparent 80%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 1;
        }

        /* 2. Sleek Floating Island Navbar */
        .navbar-container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 28px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: relative;
            z-index: 50;
        }

        .nav-logo {
            font-size: 1.3rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            color: #FFFFFF;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .nav-logo-badge {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            color: #818CF8;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.35);
            padding: 2px 8px;
            border-radius: 9999px;
            text-transform: uppercase;
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
            font-size: 4rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            line-height: 1.12;
            color: #FFFFFF;
            margin-bottom: 1.25rem;
        }

        .hero-subtitle {
            font-size: 1.15rem;
            color: #94A3B8;
            font-weight: 400;
            max-width: 600px;
            margin: 0 auto 2.25rem auto;
            line-height: 1.65;
        }

        .hero-cta {
            background: #FFFFFF;
            color: #05070E;
            border: none;
            border-radius: 9999px;
            padding: 15px 38px;
            font-size: 0.98rem;
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

        /* 6. Finomac-Style Minimalist Stat Ticker */
        .stats-strip-container {
            max-width: 1100px;
            margin: 4rem auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            padding: 0 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding: 3rem 1rem;
        }

        .stat-strip-item {
            text-align: center;
        }

        .stat-strip-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 3rem;
            font-weight: 900;
            letter-spacing: -0.04em;
            color: #FFFFFF;
            line-height: 1.1;
        }

        .stat-strip-label {
            font-size: 0.85rem;
            color: #94A3B8;
            font-weight: 600;
            margin-top: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }

        /* 7. Blendr.ai Cinematic Feature Showcase */
        .features-container {
            max-width: 1140px;
            margin: 6rem auto;
            padding: 0 2rem;
        }

        .section-header {
            text-align: center;
            max-width: 700px;
            margin: 0 auto 4rem auto;
        }

        .section-eyebrow {
            font-size: 0.78rem;
            font-weight: 800;
            color: #818CF8;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
            display: inline-block;
        }

        .section-heading {
            font-size: 2.8rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            line-height: 1.2;
            color: #FFFFFF;
        }

        .feature-cinematic-card {
            background: linear-gradient(135deg, rgba(16, 22, 38, 0.75) 0%, rgba(9, 13, 25, 0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 28px;
            padding: 3.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 3rem;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .feature-cinematic-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            transform: translateY(-4px);
            box-shadow: 0 35px 70px -15px rgba(99, 102, 241, 0.2);
        }

        .feature-card-content {
            flex: 1.2;
        }

        .feature-chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 14px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 700;
            color: #CBD5E1;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            margin-bottom: 1.25rem;
        }

        .feature-card-title {
            font-size: 2rem;
            font-weight: 800;
            color: #FFFFFF;
            letter-spacing: -0.03em;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .feature-card-desc {
            color: #94A3B8;
            font-size: 1.05rem;
            line-height: 1.7;
            margin-bottom: 1.75rem;
        }

        .feature-card-cta {
            color: #818CF8;
            font-size: 0.95rem;
            font-weight: 700;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: gap 0.2s ease;
        }
        .feature-card-cta:hover {
            gap: 10px;
            color: #A5B4FC;
        }

        .feature-card-visual {
            flex: 1;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 2.5rem;
            text-align: center;
        }

        /* 8. Blendr.ai Minimalist Closing Section & Footer */
        .closing-section {
            text-align: center;
            padding: 8rem 2rem 5rem 2rem;
            position: relative;
        }

        .closing-title {
            font-size: 3.2rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            color: #FFFFFF;
            margin-bottom: 1rem;
        }

        .closing-subtitle {
            font-size: 1.1rem;
            color: #94A3B8;
            margin-bottom: 2.5rem;
        }

        .footer-strip {
            max-width: 1140px;
            margin: 4rem auto 2rem auto;
            padding-top: 2rem;
            border-top: 1px solid rgba(255, 255, 255, 0.06);
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #64748B;
            font-size: 0.85rem;
        }

        @media (max-width: 950px) {
            .hero-title { font-size: 2.6rem; }
            .card-floating-left, .card-floating-right { display: none; }
            .spline-stage { height: 400px; }
            .nav-menu { display: none; }
            .stats-strip-container { grid-template-columns: 1fr; gap: 2rem; }
            .feature-cinematic-card { flex-direction: column; padding: 2rem; }
            .section-heading { font-size: 2.2rem; }
            .closing-title { font-size: 2.3rem; }
        }
    </style>
</head>
<body>
    <!-- Spotlight mouse-follower -->
    <div class="cursor-spotlight" id="spotlight"></div>
    <div class="ambient-glow-top"></div>

    <!-- 1. Sleek Floating Navbar -->
    <nav class="navbar-container">
        <div class="nav-logo">
            <span>SAPPM</span>
            <span class="nav-logo-badge">Decision Support</span>
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
            <button class="btn-pill-white" onclick="window.parent.location.href='/Predict'">Evaluate Now</button>
        </div>
    </nav>

    <!-- 2. Centered Minimalist Hero Header -->
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

    <!-- 4. Finomac Minimalist Stat Strip -->
    <div class="stats-strip-container">
        <div class="stat-strip-item">
            <div class="stat-strip-num">1,000,000</div>
            <div class="stat-strip-label">Trained Dataset Records</div>
        </div>
        <div class="stat-strip-item">
            <div class="stat-strip-num" style="color: #34D399;">99.81%</div>
            <div class="stat-strip-label">XGBoost Test Accuracy</div>
        </div>
        <div class="stat-strip-item">
            <div class="stat-strip-num" style="color: #60A5FA;">&lt; 15 ms</div>
            <div class="stat-strip-label">Real-Time Inference</div>
        </div>
    </div>

    <!-- 5. Blendr.ai Cinematic Feature Showcases -->
    <div class="features-container">
        <div class="section-header">
            <span class="section-eyebrow">Institutional Architecture</span>
            <h2 class="section-heading">Everything You Need to Guide Student Success</h2>
        </div>

        <!-- Feature Card 1 -->
        <div class="feature-cinematic-card">
            <div class="feature-card-content">
                <div class="feature-chip">✦ Predictive Intelligence</div>
                <h3 class="feature-card-title">Multiclass Performance Forecasting</h3>
                <p class="feature-card-desc">
                    Trained across 800,000 records to generate fine-grained probability distributions across grades A, B, C, D, and F with 99.81% precision.
                </p>
                <a class="feature-card-cta" onclick="window.parent.location.href='/Predict'">Launch Predictor ↗</a>
            </div>
            <div class="feature-card-visual">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 2.4rem; font-weight: 900; color: #34D399;">Grade A</div>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px; text-transform: uppercase; font-weight: 700;">99.81% Certainty</div>
            </div>
        </div>

        <!-- Feature Card 2 -->
        <div class="feature-cinematic-card">
            <div class="feature-card-content">
                <div class="feature-chip">✦ Explainable AI</div>
                <h3 class="feature-card-title">Demystified SHAP Attribution</h3>
                <p class="feature-card-desc">
                    Eliminates black-box opacity. Quantifies exact Shapley factor contributions for attendance, study hours, and continuous assessments.
                </p>
                <a class="feature-card-cta" onclick="window.parent.location.href='/Explainability'">Inspect Attribution ↗</a>
            </div>
            <div class="feature-card-visual">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.8rem; font-weight: 900; color: #818CF8;">SHAP +0.42</div>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 4px; text-transform: uppercase; font-weight: 700;">Dominant Positive Driver</div>
            </div>
        </div>

        <!-- Feature Card 3 -->
        <div class="feature-cinematic-card">
            <div class="feature-card-content">
                <div class="feature-chip">✦ Proactive Guidance</div>
                <h3 class="feature-card-title">3-Tier Early Warning Stratification</h3>
                <p class="feature-card-desc">
                    Automatically tags learners into Low, Medium, and High Risk tiers to trigger early mentoring before final examinations.
                </p>
                <a class="feature-card-cta" onclick="window.parent.location.href='/Student_Records'">View Database Records ↗</a>
            </div>
            <div class="feature-card-visual">
                <div style="display: inline-block; padding: 6px 18px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.5); border-radius: 9999px; color: #34D399; font-weight: 800; font-size: 1.1rem;">● LOW RISK</div>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 8px; text-transform: uppercase; font-weight: 700;">Proactive Categorisation</div>
            </div>
        </div>
    </div>

    <!-- 6. Closing CTA Section -->
    <section class="closing-section">
        <h2 class="closing-title">Ready to evaluate student performance?</h2>
        <p class="closing-subtitle">Launch the predictor or access the staff portal to begin data-driven guidance.</p>
        <button class="hero-cta" onclick="window.parent.location.href='/Predict'">
            Evaluate Performance ↗
        </button>

        <div class="footer-strip">
            <div>S.A.P.P.M — Academic Performance Intelligence</div>
            <div>Powered by XGBoost, SHAP & Supabase</div>
        </div>
    </section>

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

# Render Full-Page Blendr / Roobinium Experience
components.html(complete_landing_html, height=2650, scrolling=False)