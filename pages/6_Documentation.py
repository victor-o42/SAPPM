"""
About & System Documentation Page for S.A.P.P.M
Presents background details, methodology, CRISP-DM lifecycle, and research scope.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.ui.styles import apply_global_styles
from src.ui.icons import icon

st.set_page_config(
    page_title="Documentation - S.A.P.P.M",
    layout="wide"
)

apply_global_styles()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
        <div style="background: rgba(99, 102, 241, 0.15); padding: 8px; border-radius: 10px; display: flex;">
            {icon("file_text", size=24, color="#818CF8")}
        </div>
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em;">System Documentation & Methodology</h1>
    </div>
    <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 1.5rem;">Comprehensive overview of project objectives, machine learning methodology, and academic scope.</p>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.4rem;">
                    {icon("target", size=18, color="#818CF8")}
                    <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Background</div>
                </div>
                <h3 style="color: #FFFFFF; font-size: 1.3rem; font-weight: 800; margin: 0.2rem 0 0.75rem 0;">Project Motivation & Aim</h3>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    Many institutions rely on reactive evaluation systems (noticing academic challenges only after exams are graded).
                    <strong>S.A.P.P.M</strong> enables proactive, data-driven intervention by predicting expected grade performance
                    from continuous assessments and learning habits.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.4rem;">
                    {icon("layers", size=18, color="#34D399")}
                    <div style="font-size: 0.72rem; color: #34D399; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Process Model</div>
                </div>
                <h3 style="color: #FFFFFF; font-size: 1.3rem; font-weight: 800; margin: 0.2rem 0 0.75rem 0;">Development Methodology</h3>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
                    The project follows the <strong>Agile Software Development Lifecycle (4 Sprints)</strong> paired with the <strong>CRISP-DM (Cross-Industry Standard Process for Data Mining)</strong> framework:
                </p>
                <ol style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.8; margin-bottom: 0;">
                    <li><strong>Sprint 1:</strong> Requirements Gathering & Dataset Acquisition (Qureshi 2025 Dataset).</li>
                    <li><strong>Sprint 2:</strong> Data Cleaning, Label Encoding, and Multi-Algorithm Training.</li>
                    <li><strong>Sprint 3:</strong> Evaluation, Benchmarking & Model Selection (XGBoost Champion).</li>
                    <li><strong>Sprint 4:</strong> Web Application Integration, Supabase Cloud Storage, & SHAP XAI.</li>
                </ol>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.4rem;">
                    {icon("cpu", size=18, color="#A78BFA")}
                    <div style="font-size: 0.72rem; color: #A78BFA; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Architecture</div>
                </div>
                <h3 style="color: #FFFFFF; font-size: 1.3rem; font-weight: 800; margin: 0.2rem 0 0.75rem 0;">Technology Stack</h3>
                <ul style="color: #CBD5E1; font-size: 0.92rem; line-height: 1.9; margin-bottom: 0;">
                    <li><strong>Language:</strong> Python 3.14</li>
                    <li><strong>Web Framework:</strong> Streamlit (Double-Bezel Design System)</li>
                    <li><strong>Database:</strong> Supabase (PostgreSQL with RLS)</li>
                    <li><strong>Machine Learning:</strong> Scikit-Learn & XGBoost</li>
                    <li><strong>Explainability (XAI):</strong> SHAP (TreeExplainer)</li>
                    <li><strong>Visualization:</strong> Plotly Graph Objects</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.4rem;">
                    {icon("shield", size=18, color="#FBBF24")}
                    <div style="font-size: 0.72rem; color: #FBBF24; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Boundary</div>
                </div>
                <h3 style="color: #FFFFFF; font-size: 1.3rem; font-weight: 800; margin: 0.2rem 0 0.75rem 0;">Scope & Limitations</h3>
                <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7; margin-bottom: 0;">
                    The model uses 4 core behavioral and academic predictors (Study Hours, Attendance, Participation, Total Score).
                    It serves as an early decision-support tool for academic advisors and lecturers to provide timely student mentoring.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
