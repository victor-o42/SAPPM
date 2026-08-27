"""
About & System Documentation Page for S.A.P.P.M
Presents background details, methodology, CRISP-DM lifecycle, and research scope.
"""

import streamlit as st
from src.ui.styles import apply_global_styles

st.set_page_config(
    page_title="About & Documentation - S.A.P.P.M",
    page_icon="ℹ️",
    layout="wide"
)

apply_global_styles()

st.title("ℹ️ About the S.A.P.P.M System")
st.markdown("Comprehensive overview of project objectives, machine learning methodology, and academic scope.")

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #60A5FA; margin-top:0;">Project Motivation & Aim</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">
                Many institutions rely on reactive evaluation systems (noticing academic challenges only after exams are graded).
                <strong>S.A.P.P.M</strong> enables proactive, data-driven intervention by predicting expected grade performance
                from continuous assessments and learning habits.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #34D399; margin-top:0;">Development Methodology</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6;">
                The project follows the <strong>Agile Software Development Lifecycle</strong> across 4 iterative sprints, paired with the <strong>CRISP-DM (Cross-Industry Standard Process for Data Mining)</strong> framework:
            </p>
            <ol style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.7;">
                <li><strong>Sprint 1:</strong> Requirements Gathering & Dataset Acquisition (Qureshi 2025 Dataset).</li>
                <li><strong>Sprint 2:</strong> Data Cleaning, Label Encoding, and Multi-Algorithm Training.</li>
                <li><strong>Sprint 3:</strong> Evaluation, Benchmarking & Model Selection (XGBoost Champion).</li>
                <li><strong>Sprint 4:</strong> Web Application Integration, Supabase Cloud Storage, & SHAP XAI.</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #A78BFA; margin-top:0;">Technology Stack</h3>
            <ul style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.8;">
                <li><strong>Language:</strong> Python 3.14</li>
                <li><strong>Web Framework:</strong> Streamlit</li>
                <li><strong>Database:</strong> Supabase (PostgreSQL with RLS)</li>
                <li><strong>Machine Learning:</strong> Scikit-Learn & XGBoost</li>
                <li><strong>Explainability (XAI):</strong> SHAP (TreeExplainer)</li>
                <li><strong>Visualization:</strong> Plotly Graph Objects</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #FBBF24; margin-top:0;">Scope & Limitations</h3>
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6;">
                The model uses 4 core behavioral and academic predictors (Study Hours, Attendance, Participation, Total Score).
                It acts as an early decision-support tool for academic advisors and lecturers to provide timely student mentoring.
            </p>
        </div>
    """, unsafe_allow_html=True)
