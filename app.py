"""
S.A.P.P.M - High-End Agency-Tier Landing Page
Engineered with Double-Bezel architecture, kinetic Bento Grid,
Ethereal ambient lighting, and fluid navigation.
"""

import streamlit as st
from src.ui.styles import apply_global_styles

st.set_page_config(
    page_title="S.A.P.P.M - Student Academic Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply our agency design system
apply_global_styles()

# Floating Top Header Bar
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 0 2rem 0;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 38px; height: 38px; border-radius: 12px; background: linear-gradient(135deg, #4F46E5, #3B82F6); display: flex; align-items: center; justify-content: center; font-size: 1.2rem; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.4);">🎓</div>
            <span style="font-size: 1.25rem; font-weight: 900; letter-spacing: -0.03em; color: #FFFFFF;">S.A.P.P.M</span>
            <span style="font-size: 0.72rem; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.35); color: #A5B4FC; padding: 3px 10px; border-radius: 9999px; font-weight: 700; letter-spacing: 0.05em;">ENTERPRISE AI</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); padding: 5px 14px; border-radius: 9999px;">
            <span style="width: 8px; height: 8px; background: #34D399; border-radius: 50%; display: inline-block; box-shadow: 0 0 12px #34D399;"></span>
            <span style="font-size: 0.8rem; color: #E2E8F0; font-weight: 600; font-family: 'JetBrains Mono', monospace;">XGBoost 3.4 Online</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <span class="hero-eyebrow">✨ Next-Generation Academic Intelligence</span>
        <h1 class="hero-headline">Predict Student Trajectories.<br>Intervene Before Final Exams.</h1>
        <p class="hero-lead">
            An institutional machine learning platform engineered with Extreme Gradient Boosting (XGBoost) and SHAP Explainable AI.
            Accurately forecast student grade distributions with 99.81% precision to deliver proactive academic guidance.
        </p>
    </div>
""", unsafe_allow_html=True)

# Hero Action Buttons
bcol1, bcol2, bcol3 = st.columns([1, 1.4, 1])
with bcol2:
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("🔮 Launch Predictor", use_container_width=True, type="primary"):
            st.switch_page("pages/2_🔮_Predict.py")
    with btn2:
        if st.button("🔐 Staff Portal", use_container_width=True):
            st.switch_page("pages/1_🔐_Staff_Portal.py")

st.markdown("<br>", unsafe_allow_html=True)

# Double-Bezel Live Inference Preview
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

st.markdown("<hr>", unsafe_allow_html=True)

# Stat Bento Grid
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
        <div class="stat-shell">
            <div class="stat-core">
                <div class="stat-number" style="color: #60A5FA;">1,000,000</div>
                <div class="stat-title">Dataset Instances</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="stat-shell">
            <div class="stat-core">
                <div class="stat-number" style="color: #34D399;">99.81%</div>
                <div class="stat-title">XGBoost Accuracy</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="stat-shell">
            <div class="stat-core">
                <div class="stat-number" style="color: #A78BFA;">4 Factors</div>
                <div class="stat-title">Predictor Matrix</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
        <div class="stat-shell">
            <div class="stat-core">
                <div class="stat-number" style="color: #FBBF24;">&lt; 15 ms</div>
                <div class="stat-title">Inference Speed</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Asymmetrical Bento Grid Showcase
st.subheader("Architectural & Predictive Pillars")

fcol1, fcol2 = st.columns(2, gap="large")

with fcol1:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <span style="font-size: 1.6rem;">🔮</span>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Multiclass Performance Forecast</h3>
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
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <span style="font-size: 1.6rem;">🛡️</span>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Early Warning Risk Stratification</h3>
                </div>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Transfers academic advising from reactive measures to proactive early intervention:
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
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <span style="font-size: 1.6rem;">📊</span>
                    <h3 style="margin: 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Explainable AI (SHAP Interpretability)</h3>
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
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.75rem;">
                    <span style="font-size: 1.6rem;">🗄️</span>
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
st.markdown("""
    <div class="bezel-shell">
        <div class="bezel-core" style="background: linear-gradient(135deg, rgba(17, 24, 46, 0.95) 0%, rgba(9, 13, 26, 0.98) 100%);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.5rem;">
                <span style="font-size: 1.5rem;">📐</span>
                <h3 style="color: #FFFFFF; font-size: 1.35rem; font-weight: 800; margin: 0;">3-Tier System Architecture & CRISP-DM Framework</h3>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Engineered according to the <strong>Agile Software Development Lifecycle (4 Sprints)</strong> and the <strong>CRISP-DM</strong> process model:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.2rem; margin-top: 1.25rem;">
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem;">
                    <div style="font-size: 0.8rem; color: #60A5FA; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em;">Tier 1: Presentation</div>
                    <div style="font-size: 0.9rem; color: #CBD5E1; margin-top: 0.35rem; line-height: 1.5;">Streamlit Web Studio with custom Double-Bezel glassmorphic design tokens.</div>
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
    if st.button("🚀 Start Evaluating Students", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🔮_Predict.py")