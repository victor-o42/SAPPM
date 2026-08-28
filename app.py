"""
S.A.P.P.M - Next-Generation AI Intelligence Platform
Integrates Interactive 3D Spline WebGL Scene, Spotlight Cursor Physics,
Double-Bezel Architecture, and Real-Time ML Decision Workflows.
"""

import streamlit as st
import streamlit.components.v1 as components
from src.ui.styles import apply_global_styles
from src.ui.icons import icon

st.set_page_config(
    page_title="S.A.P.P.M - Academic Performance Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global agency design system
apply_global_styles()

# Floating Institutional Top Header
st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0 1.5rem 0;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #4F46E5, #3B82F6); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);">
                {icon("academic", size=22, color="#FFFFFF")}
            </div>
            <div>
                <div style="font-size: 1.2rem; font-weight: 900; letter-spacing: -0.03em; color: #FFFFFF; line-height: 1.1;">S.A.P.P.M</div>
                <div style="font-size: 0.72rem; color: #818CF8; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;">Decision Support System</div>
            </div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); padding: 6px 16px; border-radius: 9999px;">
            <span style="width: 8px; height: 8px; background: #34D399; border-radius: 50%; display: inline-block; box-shadow: 0 0 12px #34D399;"></span>
            <span style="font-size: 0.8rem; color: #E2E8F0; font-weight: 600; font-family: 'JetBrains Mono', monospace;">XGBoost 3.4 Active</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 3D Interactive Spline Hero with Dynamic Spotlight
spline_hero_html = """
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
        }

        body {
            background: transparent;
            overflow: hidden;
        }

        /* Outer Double-Bezel Shell */
        .hero-card {
            position: relative;
            width: 100%;
            height: 520px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(6, 9, 20, 0.98) 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), inset 0 1px 1px 0 rgba(255, 255, 255, 0.15);
            display: flex;
        }

        /* Dynamic Mouse Spotlight */
        .spotlight {
            position: absolute;
            width: 450px;
            height: 450px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(56, 189, 248, 0.08) 40%, transparent 70%);
            pointer-events: none;
            transform: translate(-50%, -50%);
            transition: opacity 0.3s ease;
            filter: blur(25px);
            z-index: 1;
        }

        /* Left Hero Content */
        .hero-left {
            flex: 1.15;
            padding: 3.5rem 3rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            z-index: 2;
            position: relative;
        }

        .eyebrow-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            width: fit-content;
            padding: 0.4rem 1.1rem;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.4);
            border-radius: 9999px;
            color: #A5B4FC;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 1.25rem;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
        }

        .title-gradient {
            font-size: 3rem;
            font-weight: 900;
            line-height: 1.12;
            letter-spacing: -0.04em;
            background: linear-gradient(135deg, #FFFFFF 20%, #CBD5E1 70%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .desc-text {
            color: #94A3B8;
            font-size: 1.05rem;
            line-height: 1.65;
            max-width: 500px;
            margin-bottom: 2rem;
        }

        .stats-badge-row {
            display: flex;
            gap: 1.5rem;
        }

        .stat-mini-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 0.75rem 1.25rem;
        }

        .stat-mini-num {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.5rem;
            font-weight: 800;
            color: #34D399;
            line-height: 1.1;
        }

        .stat-mini-label {
            font-size: 0.72rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 700;
            margin-top: 0.2rem;
        }

        /* Right 3D Spline Canvas */
        .hero-right {
            flex: 1.25;
            position: relative;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        spline-viewer {
            width: 100%;
            height: 100%;
            pointer-events: auto;
        }

        /* Responsive */
        @media (max-width: 900px) {
            .hero-card {
                flex-direction: column;
                height: 750px;
            }
            .hero-left {
                padding: 2rem;
            }
            .hero-right {
                height: 380px;
            }
            .title-gradient {
                font-size: 2.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="hero-card" id="heroCard">
        <div class="spotlight" id="spotlight"></div>
        
        <div class="hero-left">
            <div class="eyebrow-pill">
                <span>✦</span> Interactive 3D Decision Support
            </div>
            <h1 class="title-gradient">
                Predict Student Trajectories.
            </h1>
            <p class="desc-text">
                Extreme Gradient Boosting (XGBoost) and SHAP Explainable AI for proactive institutional guidance and grade forecasting.
            </p>
            
            <div class="stats-badge-row">
                <div class="stat-mini-card">
                    <div class="stat-mini-num">99.81%</div>
                    <div class="stat-mini-label">Model Accuracy</div>
                </div>
                <div class="stat-mini-card">
                    <div class="stat-mini-num" style="color: #60A5FA;">1M</div>
                    <div class="stat-mini-label">Dataset Records</div>
                </div>
                <div class="stat-mini-card">
                    <div class="stat-mini-num" style="color: #A78BFA;">&lt;15ms</div>
                    <div class="stat-mini-label">Latency</div>
                </div>
            </div>
        </div>

        <div class="hero-right">
            <spline-viewer url="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"></spline-viewer>
        </div>
    </div>

    <script>
        const card = document.getElementById('heroCard');
        const spotlight = document.getElementById('spotlight');

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            spotlight.style.left = `${x}px`;
            spotlight.style.top = `${y}px`;
            spotlight.style.opacity = '1';
        });

        card.addEventListener('mouseleave', () => {
            spotlight.style.opacity = '0';
        });
    </script>
</body>
</html>
"""

# Render 3D Spline Canvas Component
components.html(spline_hero_html, height=540)

st.markdown("<br>", unsafe_allow_html=True)

# Navigation Action Triggers
bcol1, bcol2, bcol3 = st.columns([1, 1.4, 1])
with bcol2:
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("Launch Prediction Studio", use_container_width=True, type="primary"):
            st.switch_page("pages/2_Predict.py")
    with btn2:
        if st.button("Staff Management Portal", use_container_width=True):
            st.switch_page("pages/1_Staff_Portal.py")

st.markdown("<hr>", unsafe_allow_html=True)

# Live Output Preview in Double-Bezel
st.markdown("""
    <div class="bezel-shell">
        <div class="bezel-core">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                <div>
                    <span style="font-size: 0.72rem; font-weight: 800; color: #818CF8; letter-spacing: 0.12em; text-transform: uppercase;">Real-Time Inference Engine</span>
                    <h3 style="margin: 0.2rem 0 0 0; color: #FFFFFF; font-size: 1.35rem; font-weight: 800;">Academic Performance Assessment</h3>
                </div>
                <span class="risk-pill-low">● LOW RISK</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.2rem;">
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Predicted Outcome</div>
                    <div style="font-size: 2.1rem; font-weight: 900; color: #34D399; font-family: 'JetBrains Mono', monospace; margin-top: 0.2rem;">Grade A</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Confidence Score</div>
                    <div style="font-size: 2.1rem; font-weight: 900; color: #60A5FA; font-family: 'JetBrains Mono', monospace; margin-top: 0.2rem;">98.4%</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Primary Driver</div>
                    <div style="font-size: 1.35rem; font-weight: 800; color: #F8FAFC; margin-top: 0.4rem;">Attendance (+42%)</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Database Audit</div>
                    <div style="font-size: 1.35rem; font-weight: 800; color: #FBBF24; margin-top: 0.4rem;">Supabase Synced</div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Asymmetrical Bento Grid Showcase
st.subheader("System Architecture & Capabilities")

fcol1, fcol2 = st.columns(2, gap="large")

with fcol1:
    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(99, 102, 241, 0.15); padding: 8px; border-radius: 10px; display: flex;">
                        {icon("cpu", size=22, color="#818CF8")}
                    </div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Multiclass Performance Forecast</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Trained across 800,000 training records using Extreme Gradient Boosting (XGBoost) with multiclass softmax loss.
                    Generates probability distributions across five grade categories: <strong>A, B, C, D, and F</strong>.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(16, 185, 129, 0.15); padding: 8px; border-radius: 10px; display: flex;">
                        {icon("shield", size=22, color="#34D399")}
                    </div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Early Warning Risk Stratification</h3>
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
    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(244, 114, 182, 0.15); padding: 8px; border-radius: 10px; display: flex;">
                        {icon("chart", size=22, color="#F472B6")}
                    </div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Explainable AI (SHAP Interpretability)</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Eliminates opaque "black-box" decision making. Integrated with <code>shap.TreeExplainer</code> to calculate exact
                    cooperative game-theory Shapley values, showing how attendance, study hours, and exam scores influenced the outcome.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <div style="background: rgba(251, 191, 36, 0.15); padding: 8px; border-radius: 10px; display: flex;">
                        {icon("database", size=22, color="#FBBF24")}
                    </div>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Cloud Persistence & Audit Trail</h3>
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
st.markdown(f"""
    <div class="bezel-shell">
        <div class="bezel-core" style="background: linear-gradient(135deg, rgba(17, 24, 46, 0.95) 0%, rgba(9, 13, 26, 0.98) 100%);">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
                <div style="background: rgba(99, 102, 241, 0.15); padding: 8px; border-radius: 10px; display: flex;">
                    {icon("layers", size=22, color="#818CF8")}
                </div>
                <h3 style="color: #FFFFFF; font-size: 1.35rem; font-weight: 800; margin: 0;">3-Tier System Architecture & CRISP-DM Framework</h3>
            </div>
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

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer Action Banner
st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="font-size: 2.2rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em; margin-bottom: 0.5rem;">Ready to evaluate student academic performance?</h2>
        <p style="color: #94A3B8; font-size: 1.05rem; margin-bottom: 2rem;">Launch the prediction studio or sign into the staff portal to begin.</p>
    </div>
""", unsafe_allow_html=True)

fcol1, fcol2, fcol3 = st.columns([1.2, 1, 1.2])
with fcol2:
    if st.button("Start Evaluating Students", use_container_width=True, type="primary"):
        st.switch_page("pages/2_Predict.py")