"""
Landing Page (Home) for S.A.P.P.M
Presents the executive summary, system statistics, architecture highlights,
and quick navigation shortcuts.
"""

import streamlit as st
from src.ui.styles import apply_global_styles

st.set_page_config(
    page_title="S.A.P.P.M - Student Academic Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

apply_global_styles()

# Hero Section
st.markdown("""
    <div class="hero-container">
        <span class="hero-badge">Machine Learning & Explainable AI</span>
        <h1 class="hero-title">Student Academic Performance<br>Prediction Model</h1>
        <p class="hero-subtitle">
            An intelligent academic decision-support system designed to forecast student grade outcomes,
            detect at-risk learners early, and provide transparent insights using Explainable AI (SHAP).
        </p>
    </div>
""", unsafe_allow_html=True)

# System Metric Highlights
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #60A5FA;">1,000,000</div>
            <div class="stat-label">Training Records</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #34D399;">99.81%</div>
            <div class="stat-label">Model Accuracy (XGBoost)</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #A78BFA;">4 Key Features</div>
            <div class="stat-label">Behavioral & Academic</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="stat-card">
            <div class="stat-value" style="color: #FBBF24;">Cloud Synced</div>
            <div class="stat-label">Supabase Database</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Core System Pillars
st.subheader("Core System Capabilities")

card1, card2, card3 = st.columns(3)

with card1:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #60A5FA; margin-top:0;">🔮 Predictive Classification</h3>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                Multiclass gradient boosted trees (XGBoost) evaluate study hours, attendance, class participation, and total scores to predict final grades (A, B, C, D, F) with high precision.
            </p>
        </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #34D399; margin-top:0;">🛡️ Early Risk Warning</h3>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                Automatically stratifies students into <strong>Low</strong>, <strong>Medium</strong>, and <strong>High Risk</strong> tiers so academic advisors can initiate targeted counseling before semester exams.
            </p>
        </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #F472B6; margin-top:0;">📊 Explainable AI (SHAP)</h3>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                Deconstructs the "black box" by calculating exact Shapley contribution values for each student factor, explaining why a specific grade outcome was determined.
            </p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Quick Navigation Shortcuts
st.subheader("Quick Actions")
qcol1, qcol2, qcol3 = st.columns(3)

with qcol1:
    if st.button("🔮 Run Student Prediction", use_container_width=True):
        st.switch_page("pages/2_🔮_Predict.py")

with qcol2:
    if st.button("📈 View Model Benchmarks", use_container_width=True):
        st.switch_page("pages/4_📈_Model_Analytics.py")

with qcol3:
    if st.button("🗄️ Browse Student Records", use_container_width=True):
        st.switch_page("pages/5_🗄️_Student_Records.py")
