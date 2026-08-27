"""
S.A.P.P.M - High-End Modern Landing Page
Main entrypoint for the Student Academic Performance Prediction System.
Features an ultra-sleek hero section, interactive showcase, bento grid,
and navigation routes.
"""

import streamlit as st
from src.ui.styles import apply_global_styles

st.set_page_config(
    page_title="S.A.P.P.M - Student Academic Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply global design system
apply_global_styles()

# Top Institutional Badge Header
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0 1.5rem 0;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="font-size: 1.5rem;">🎓</span>
            <span style="font-size: 1.15rem; font-weight: 800; letter-spacing: -0.02em; color: #FFFFFF;">S.A.P.P.M</span>
            <span style="font-size: 0.75rem; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #818CF8; padding: 2px 8px; border-radius: 9999px; font-weight: 600;">v2.0 PRO</span>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="width: 8px; height: 8px; background: #10B981; border-radius: 50%; display: inline-block; box-shadow: 0 0 10px #10B981;"></span>
            <span style="font-size: 0.82rem; color: #94A3B8; font-weight: 600;">ML Engine Online</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <span class="hero-badge">✨ Next-Generation Academic Intelligence</span>
        <h1 class="hero-title">Predict Student Performance.<br>Intervene Before It's Too Late.</h1>
        <p class="hero-subtitle">
            An institutional decision-support system powered by Extreme Gradient Boosting (XGBoost) and Explainable AI (SHAP).
            Forecast student grade outcomes with 99.81% accuracy and understand the driving factors behind every prediction.
        </p>
    </div>
""", unsafe_allow_html=True)

# Dual Hero Action Buttons
bcol1, bcol2, bcol3 = st.columns([1, 1.2, 1])
with bcol2:
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("🔮 Launch Predictor", use_container_width=True, type="primary"):
            st.switch_page("pages/2_🔮_Predict.py")
    with btn2:
        if st.button("🔐 Staff Portal", use_container_width=True):
            st.switch_page("pages/1_🔐_Staff_Portal.py")

st.markdown("<br>", unsafe_allow_html=True)

# Interactive Live Forecast Preview Teaser
st.markdown("""
    <div class="glass-card" style="border-color: rgba(99, 102, 241, 0.35); background: linear-gradient(135deg, rgba(18, 26, 48, 0.8) 0%, rgba(10, 15, 29, 0.9) 100%);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem;">
            <div>
                <span style="font-size: 0.78rem; font-weight: 700; color: #818CF8; letter-spacing: 0.08em; text-transform: uppercase;">Real-Time AI Output Preview</span>
                <h3 style="margin: 0.2rem 0; color: #FFFFFF; font-size: 1.3rem;">Predictive Assessment Engine</h3>
            </div>
            <span class="risk-badge-low">LOW RISK</span>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                <div style="font-size: 0.78rem; color: #94A3B8; text-transform: uppercase; font-weight: 600;">Predicted Grade</div>
                <div style="font-size: 1.8rem; font-weight: 900; color: #34D399; font-family: 'JetBrains Mono', monospace;">Grade A</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                <div style="font-size: 0.78rem; color: #94A3B8; text-transform: uppercase; font-weight: 600;">Model Certainty</div>
                <div style="font-size: 1.8rem; font-weight: 900; color: #60A5FA; font-family: 'JetBrains Mono', monospace;">98.4%</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                <div style="font-size: 0.78rem; color: #94A3B8; text-transform: uppercase; font-weight: 600;">Dominant Driver</div>
                <div style="font-size: 1.4rem; font-weight: 800; color: #F8FAFC; margin-top: 0.2rem;">Attendance (+42%)</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                <div style="font-size: 0.78rem; color: #94A3B8; text-transform: uppercase; font-weight: 600;">Cloud Sync</div>
                <div style="font-size: 1.4rem; font-weight: 800; color: #FBBF24; margin-top: 0.2rem;">Supabase Active</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# System Metric Highlights
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #60A5FA;">1,000,000</div>
            <div class="stat-label">Training Records</div>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #34D399;">99.81%</div>
            <div class="stat-label">XGBoost Accuracy</div>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #A78BFA;">4 Core Factors</div>
            <div class="stat-label">Study, Attendance, Score</div>
        </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #FBBF24;">&lt; 15 ms</div>
            <div class="stat-label">Inference Latency</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Feature Bento Grid Showcase
st.subheader("Architectural & Predictive Pillars")

fcol1, fcol2 = st.columns(2, gap="medium")

with fcol1:
    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                <span style="font-size: 1.5rem;">🔮</span>
                <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem;">Multiclass Performance Forecast</h3>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Trained across 800,000 training instances using Extreme Gradient Boosting (XGBoost) with multiclass softmax loss.
                Outputs precise probabilistic distributions across five academic tiers: <strong>Grade A, B, C, D, and F</strong>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                <span style="font-size: 1.5rem;">🛡️</span>
                <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem;">Early Warning & Risk Stratification</h3>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Replaces traditional reactive assessments with proactive risk categorisation:
                <br>• <strong style="color: #34D399;">Low Risk</strong>: Stable high performers (Grades A/B).
                <br>• <strong style="color: #FBBF24;">Medium Risk</strong>: Borderline students needing guidance (Grade C).
                <br>• <strong style="color: #F87171;">High Risk</strong>: Critical academic danger (Grades D/F).
            </p>
        </div>
    """, unsafe_allow_html=True)

with fcol2:
    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                <span style="font-size: 1.5rem;">📊</span>
                <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem;">Explainable AI (SHAP Interpretability)</h3>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Eliminates "black-box" decision opacity. Integrated with <code>shap.TreeExplainer</code> to calculate exact
                cooperative game-theory Shapley values, showing exactly how each hour of study or attendance boosted or lowered the final outcome.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 0.75rem;">
                <span style="font-size: 1.5rem;">🗄️</span>
                <h3 style="margin: 0; color: #FFFFFF; font-size: 1.25rem;">Cloud Persistence & Audit Trail</h3>
            </div>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
                Backed by <strong>Supabase PostgreSQL</strong> with Row Level Security (RLS).
                Automatically archives all staff predictions, student profiles, and historical trends for institutional reporting and CSV exports.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Methodology & Architecture Overview
st.markdown("""
    <div class="glass-card" style="background: linear-gradient(135deg, rgba(16, 23, 41, 0.9) 0%, rgba(10, 14, 26, 0.95) 100%);">
        <h3 style="color: #FFFFFF; font-size: 1.3rem; margin-top: 0;">📐 3-Tier System Architecture & CRISP-DM Framework</h3>
        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65;">
            Developed according to the <strong>Agile Scrum (4 Sprints)</strong> methodology and the <strong>CRISP-DM</strong> data mining lifecycle:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 1rem;">
                <strong style="color: #60A5FA;">Tier 1: Presentation Layer</strong>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.3rem;">Streamlit Web Studio with custom glassmorphism design tokens.</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 1rem;">
                <strong style="color: #34D399;">Tier 2: Application Layer</strong>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.3rem;">Python 3.14 ML engine loading XGBoost + SHAP TreeExplainer.</div>
            </div>
            <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 1rem;">
                <strong style="color: #A78BFA;">Tier 3: Data Layer</strong>
                <div style="font-size: 0.85rem; color: #94A3B8; margin-top: 0.3rem;">Supabase PostgreSQL (Staff Profiles, Student Data, Prediction Output).</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Footer Call to Action
st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h2 style="font-size: 1.8rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.5rem;">Ready to evaluate student academic performance?</h2>
        <p style="color: #94A3B8; margin-bottom: 1.5rem;">Launch the prediction studio or sign into the staff portal to begin.</p>
    </div>
""", unsafe_allow_html=True)

fcol1, fcol2, fcol3 = st.columns([1.2, 1, 1.2])
with fcol2:
    if st.button("🚀 Start Evaluating Students", use_container_width=True, type="primary"):
        st.switch_page("pages/2_🔮_Predict.py")