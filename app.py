"""
S.A.P.P.M - Awwwards-Tier 3D Interactive AI Intelligence Platform
Full-viewport 3D Spline interactive robot canvas with cursor tracking physics,
cinematic background typography, floating glass island navbar, and live decision support.
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="S.A.P.P.M - Student Academic Performance Prediction",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject full-viewport CSS to remove default Streamlit spacing and create an immersive dark canvas
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    /* Reset Streamlit App Margins for Full-Bleed 3D Experience */
    html, body, [class*="css"], .stApp {
        background-color: #030712 !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #F8FAFC !important;
        overflow-x: hidden !important;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
        z-index: 100 !important;
    }

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Floating Top Navbar */
    .nav-wrapper {
        position: fixed;
        top: 20px;
        left: 0;
        right: 0;
        display: flex;
        justify-content: center;
        z-index: 999;
        pointer-events: none;
    }

    .floating-nav {
        pointer-events: auto;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 9999px;
        padding: 6px 14px;
        box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.15);
    }

    .nav-brand {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 14px;
        font-weight: 900;
        font-size: 0.95rem;
        letter-spacing: -0.02em;
        color: #FFFFFF;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    .nav-item {
        color: #94A3B8;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 6px 14px;
        border-radius: 9999px;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .nav-item:hover, .nav-item.active {
        color: #FFFFFF;
        background: rgba(99, 102, 241, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.4);
    }

    /* Container for bottom content */
    .content-container {
        max-width: 1240px;
        margin: 0 auto;
        padding: 3rem 1.5rem 6rem 1.5rem;
    }

    /* Double Bezel Bento Cards */
    .bezel-shell {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 6px;
        margin-bottom: 1.5rem;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .bezel-shell:hover {
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.25);
        transform: translateY(-3px);
    }
    .bezel-core {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(9, 14, 28, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 19px;
        padding: 1.75rem;
        box-shadow: inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);
    }

    /* Primary Action Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: 9999px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        padding: 0.75rem 1.75rem !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 8px 24px -4px rgba(79, 70, 229, 0.45) !important;
    }
    .stButton > button:hover {
        box-shadow: 0 14px 35px -4px rgba(79, 70, 229, 0.7) !important;
        transform: translateY(-3px) !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3D Interactive Spline Hero Viewport (Full Screen Width with Centered Cursor-Tracking Robot)
spline_viewport_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script type="module" src="https://unpkg.com/@splinetool/viewer@1.9.72/build/spline-viewer.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            user-select: none;
        }

        body {
            background-color: #030712;
            overflow: hidden;
            width: 100vw;
            height: 680px;
            position: relative;
        }

        /* Ambient Lighting Grid */
        .ambient-glow-left {
            position: absolute;
            top: 20%;
            left: 5%;
            width: 450px;
            height: 450px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
            filter: blur(50px);
            pointer-events: none;
            z-index: 1;
        }

        .ambient-glow-right {
            position: absolute;
            top: 20%;
            right: 5%;
            width: 450px;
            height: 450px;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.12) 0%, transparent 70%);
            filter: blur(50px);
            pointer-events: none;
            z-index: 1;
        }

        /* Massive Background Architectural Typography */
        .bg-typography {
            position: absolute;
            top: 48%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 13.5vw;
            font-weight: 900;
            letter-spacing: 0.12em;
            color: rgba(255, 255, 255, 0.03);
            text-transform: uppercase;
            pointer-events: none;
            z-index: 2;
            white-space: nowrap;
            text-shadow: 0 0 80px rgba(99, 102, 241, 0.05);
        }

        /* 3D Spline Interactive Canvas (Center Stage) */
        .spline-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 3;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        spline-viewer {
            width: 100%;
            height: 100%;
            pointer-events: auto;
        }

        /* Left Floating Overlay Card */
        .overlay-left {
            position: absolute;
            bottom: 40px;
            left: 48px;
            z-index: 10;
            max-width: 400px;
            pointer-events: none;
        }

        .eyebrow-chip {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 5px 14px;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.35);
            border-radius: 9999px;
            color: #A5B4FC;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 12px;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.25);
        }

        .hero-title {
            font-size: 2.3rem;
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.03em;
            background: linear-gradient(135deg, #FFFFFF 30%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            font-size: 0.95rem;
            color: #94A3B8;
            line-height: 1.6;
        }

        /* Right Floating Live Intelligence Scorecard */
        .overlay-right {
            position: absolute;
            bottom: 40px;
            right: 48px;
            z-index: 10;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(9, 14, 28, 0.9) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 20px 24px;
            width: 320px;
            box-shadow: 0 25px 50px -10px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.15);
            pointer-events: none;
        }

        .score-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .score-title {
            font-size: 0.72rem;
            color: #818CF8;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }

        .risk-pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 3px 10px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.45);
            border-radius: 9999px;
            color: #34D399;
            font-weight: 800;
            font-size: 0.75rem;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        .metric-cell {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 10px;
            text-align: center;
        }

        .metric-val {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.4rem;
            font-weight: 900;
            color: #FFFFFF;
        }

        .metric-lbl {
            font-size: 0.68rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 700;
            margin-top: 2px;
        }

        @media (max-width: 900px) {
            body {
                height: 780px;
            }
            .overlay-left {
                top: 40px;
                left: 20px;
                right: 20px;
                max-width: 100%;
            }
            .overlay-right {
                bottom: 20px;
                left: 20px;
                right: 20px;
                width: auto;
            }
            .bg-typography {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="ambient-glow-left"></div>
    <div class="ambient-glow-right"></div>
    
    <div class="bg-typography">P R E D I C T</div>

    <div class="spline-container">
        <spline-viewer url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
    </div>

    <div class="overlay-left">
        <div class="eyebrow-chip">✦ Institutional Intelligence</div>
        <h1 class="hero-title">Predict Student Trajectories.</h1>
        <p class="hero-subtitle">
            Multiclass XGBoost & SHAP Explainable AI for proactive early guidance and academic trajectory forecasting.
        </p>
    </div>

    <div class="overlay-right">
        <div class="score-header">
            <span class="score-title">Live Inference Preview</span>
            <span class="risk-pill">● LOW RISK</span>
        </div>
        <div class="metrics-grid">
            <div class="metric-cell">
                <div class="metric-val" style="color: #34D399;">Grade A</div>
                <div class="metric-lbl">Prediction</div>
            </div>
            <div class="metric-cell">
                <div class="metric-val" style="color: #60A5FA;">99.81%</div>
                <div class="metric-lbl">Confidence</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render Full-Width 3D Hero
components.html(spline_viewport_html, height=690)

# Quick Action Bar
st.markdown('<div class="content-container">', unsafe_allow_html=True)

acol1, acol2, acol3 = st.columns([1, 1.4, 1])
with acol2:
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("🔮 Launch Prediction Studio", use_container_width=True, type="primary"):
            st.switch_page("pages/2_Predict.py")
    with btn2:
        if st.button("🔐 Staff Portal", use_container_width=True):
            st.switch_page("pages/1_Staff_Portal.py")

st.markdown("<hr style='border: none; height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent); margin: 3rem 0;'>", unsafe_allow_html=True)

# 4 Key Stat Tickers
s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core" style="text-align: center;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #60A5FA; font-family: 'JetBrains Mono', monospace;">1,000,000</div>
                <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-top: 0.2rem;">Dataset Records</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core" style="text-align: center;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #34D399; font-family: 'JetBrains Mono', monospace;">99.81%</div>
                <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-top: 0.2rem;">XGBoost Accuracy</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core" style="text-align: center;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #A78BFA; font-family: 'JetBrains Mono', monospace;">4 Factors</div>
                <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-top: 0.2rem;">Predictor Matrix</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core" style="text-align: center;">
                <div style="font-size: 2.2rem; font-weight: 900; color: #FBBF24; font-family: 'JetBrains Mono', monospace;">&lt; 15 ms</div>
                <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-top: 0.2rem;">Inference Speed</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Asymmetrical Bento Grid Showcase
st.subheader("Architectural & Predictive Pillars")

fcol1, fcol2 = st.columns(2, gap="large")

with fcol1:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 10px; padding: 6px 10px; color: #818CF8; font-weight: 800; font-size: 0.8rem;">01</div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; font-weight: 800;">Multiclass Performance Forecast</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Trained across 800,000 training records using Extreme Gradient Boosting (XGBoost) with multiclass softmax loss.
                    Generates fine-grained probability distributions across five grade categories: <strong>A, B, C, D, and F</strong>.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 6px 10px; color: #34D399; font-weight: 800; font-size: 0.8rem;">02</div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; font-weight: 800;">Early Warning Risk Stratification</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Transitions academic advising from reactive measures to proactive early intervention:
                    <br>• <strong style="color: #34D399;">Low Risk</strong>: Stable high-performing learners (Grades A/B).
                    <br>• <strong style="color: #FBBF24;">Medium Risk</strong>: Average tier students needing guidance (Grade C).
                    <br>• <strong style="color: #F87171;">High Risk</strong>: Critical academic danger requiring immediate tutoring (Grades D/F).
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with fcol2:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(244, 114, 182, 0.15); border: 1px solid rgba(244, 114, 182, 0.3); border-radius: 10px; padding: 6px 10px; color: #F472B6; font-weight: 800; font-size: 0.8rem;">03</div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; font-weight: 800;">Explainable AI (SHAP Interpretability)</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Eliminates opaque "black-box" decision making. Integrated with <code>shap.TreeExplainer</code> to calculate exact
                    cooperative game-theory Shapley values, showing how attendance, study hours, and exam scores influenced the outcome.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(251, 191, 36, 0.15); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: 10px; padding: 6px 10px; color: #FBBF24; font-weight: 800; font-size: 0.8rem;">04</div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem; font-weight: 800;">Cloud Persistence & Audit Trail</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Powered by <strong>Supabase PostgreSQL</strong> with Row Level Security (RLS).
                    Automatically archives evaluation records, student metrics, and prediction timestamps for institutional analytics and reporting.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 3-Tier System Architecture Card
st.markdown("""
    <div class="bezel-shell">
        <div class="bezel-core" style="background: linear-gradient(135deg, rgba(17, 24, 46, 0.95) 0%, rgba(9, 13, 26, 0.98) 100%);">
            <h3 style="color: #FFFFFF; font-size: 1.35rem; font-weight: 800; margin: 0 0 0.5rem 0;">📐 3-Tier System Architecture & CRISP-DM Framework</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Engineered according to the <strong>Agile Software Development Lifecycle (4 Sprints)</strong> and the <strong>CRISP-DM</strong> process model:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.2rem; margin-top: 1.25rem;">
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #60A5FA; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">Tier 1: Presentation</div>
                    <div style="font-size: 0.9rem; color: #CBD5E1; margin-top: 0.35rem; line-height: 1.5;">Streamlit Web Studio with interactive 3D WebGL Spline scenes and Double-Bezel cards.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #34D399; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">Tier 2: Application</div>
                    <div style="font-size: 0.9rem; color: #CBD5E1; margin-top: 0.35rem; line-height: 1.5;">Python 3.14 inference engine loading serialized XGBoost and SHAP TreeExplainer.</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #A78BFA; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">Tier 3: Data Layer</div>
                    <div style="font-size: 0.9rem; color: #CBD5E1; margin-top: 0.35rem; line-height: 1.5;">Supabase PostgreSQL hosting staff auth profiles, student metrics, and prediction logs.</div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)