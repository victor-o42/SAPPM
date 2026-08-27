"""
Student Performance Prediction Page
Provides intuitive input controls, 1-click test presets, real-time predictions,
interactive probability distributions, and Supabase synchronization.
"""

import streamlit as st
import plotly.graph_objects as go
from src.ui.styles import apply_global_styles
from src.services.prediction_service import predict_student_grade

st.set_page_config(
    page_title="Predict Performance - S.A.P.P.M",
    page_icon="🔮",
    layout="wide"
)

apply_global_styles()

st.title("🔮 Student Grade Prediction & Risk Assessment")
st.markdown("Enter the student's study metrics and continuous assessment scores to generate an AI performance forecast.")

# Quick Test Presets
pcol1, pcol2, pcol3, pcol4 = st.columns([1.2, 1, 1, 1])
with pcol1:
    st.markdown("<div style='padding-top: 8px; font-size: 0.8rem; color: #94A3B8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;'>Test Presets:</div>", unsafe_allow_html=True)
with pcol2:
    if st.button("🌟 Top Student (Grade A)", use_container_width=True):
        st.session_state["p_hours"] = 22.0
        st.session_state["p_att"] = 96.0
        st.session_state["p_part"] = 9.0
        st.session_state["p_score"] = 92.0
        st.session_state["p_name"] = "Alex Johnson"
        st.session_state["p_matric"] = "CSC/2026/001"
with pcol3:
    if st.button("⚖️ Average (Grade C)", use_container_width=True):
        st.session_state["p_hours"] = 10.0
        st.session_state["p_att"] = 75.0
        st.session_state["p_part"] = 5.0
        st.session_state["p_score"] = 62.0
        st.session_state["p_name"] = "Jordan Taylor"
        st.session_state["p_matric"] = "CSC/2026/045"
with pcol4:
    if st.button("⚠️ At Risk (Grade D/F)", use_container_width=True):
        st.session_state["p_hours"] = 3.0
        st.session_state["p_att"] = 50.0
        st.session_state["p_part"] = 2.5
        st.session_state["p_score"] = 42.0
        st.session_state["p_name"] = "Morgan Lee"
        st.session_state["p_matric"] = "CSC/2026/089"

st.markdown("<br>", unsafe_allow_html=True)

col_input, col_output = st.columns([1.1, 1.4], gap="large")

with col_input:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="font-size: 0.75rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.2rem;">Input Parameters</div>
                <h3 style="margin: 0 0 1.25rem 0; color: #FFFFFF; font-size: 1.25rem;">Student Details & Indicators</h3>
    """, unsafe_allow_html=True)
    
    student_name = st.text_input(
        "Student Full Name (Optional)", 
        value=st.session_state.get("p_name", "Student Candidate"),
        placeholder="e.g. Victor Okafor"
    )
    matric_number = st.text_input(
        "Matriculation / ID Number", 
        value=st.session_state.get("p_matric", "U/2026/CSC/104"),
        placeholder="e.g. U/2026/CSC/104"
    )
    
    st.markdown("<hr style='margin: 1.2rem 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 0.85rem; font-weight: 700; color: #CBD5E1; margin-bottom: 0.5rem;'>ACADEMIC & BEHAVIORAL INDICATORS</div>", unsafe_allow_html=True)

    study_hours = st.slider(
        "Weekly Self Study Hours",
        min_value=0.0,
        max_value=40.0,
        value=st.session_state.get("p_hours", 15.0),
        step=0.5,
        help="Average hours the student spends on independent study each week."
    )

    attendance = st.slider(
        "Attendance Percentage (%)",
        min_value=0.0,
        max_value=100.0,
        value=st.session_state.get("p_att", 85.0),
        step=1.0,
        help="Percentage of scheduled lectures and practicals attended."
    )

    participation = st.slider(
        "Class Participation Score (0 - 10)",
        min_value=0.0,
        max_value=10.0,
        value=st.session_state.get("p_part", 7.0),
        step=0.5,
        help="Engagement score in questions, discussions, and laboratory sessions."
    )

    total_score = st.slider(
        "Total Assessment & Quiz Score (0 - 100)",
        min_value=0.0,
        max_value=100.0,
        value=st.session_state.get("p_score", 75.0),
        step=0.5,
        help="Cumulative score from assignments, tests, and quizzes."
    )

    predict_btn = st.button("🚀 Generate Performance Forecast", use_container_width=True, type="primary")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_output:
    if predict_btn or "last_prediction" in st.session_state:
        if predict_btn:
            with st.spinner("Evaluating student metrics with XGBoost..."):
                user_id = st.session_state.get("user", {}).id if hasattr(st.session_state.get("user"), "id") else None
                result = predict_student_grade(
                    study_hours=study_hours,
                    attendance=attendance,
                    participation=participation,
                    total_score=total_score,
                    student_name=student_name,
                    matric_number=matric_number,
                    user_id=user_id
                )
                st.session_state["last_prediction"] = result
        else:
            result = st.session_state["last_prediction"]

        # Double-Bezel Results Summary Card
        badge_pill = (
            "risk-pill-low" if "LOW" in result["risk_level"]
            else "risk-pill-medium" if "MEDIUM" in result["risk_level"]
            else "risk-pill-high"
        )

        st.markdown(f"""
            <div class="bezel-shell">
                <div class="bezel-core">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div>
                            <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Evaluation Output</div>
                            <h3 style="margin: 0.2rem 0 0 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">{result.get('student_name', 'Student Candidate')}</h3>
                        </div>
                        <span class="{badge_pill}">● {result['risk_level']}</span>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem;">
                        <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem; text-align: center;">
                            <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Predicted Grade</div>
                            <div style="font-size: 2.5rem; font-weight: 900; color: #34D399; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin-top: 0.25rem;">Grade {result['predicted_grade']}</div>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 14px; padding: 1.25rem; text-align: center;">
                            <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase; font-weight: 700; letter-spacing: 0.08em;">Confidence Score</div>
                            <div style="font-size: 2.5rem; font-weight: 900; color: #60A5FA; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin-top: 0.25rem;">{result['confidence_score']:.1f}%</div>
                        </div>
                    </div>
                    <div style="margin-top: 1.25rem; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                        <div style="font-size: 0.88rem; color: #E2E8F0; line-height: 1.6;"><strong>📌 Advisory Recommendation:</strong> {result['recommendation']}</div>
                        <div style="font-size: 0.75rem; color: #34D399; margin-top: 0.4rem; font-weight: 600;">✓ Synced to Supabase Cloud Database</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Plotly Probability Distribution Chart in Double Bezel
        st.markdown("""
            <div class="bezel-shell">
                <div class="bezel-core">
                    <h4 style="margin: 0 0 1rem 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 800;">Grade Probability Distribution</h4>
        """, unsafe_allow_html=True)
        
        grades = list(result["grade_distribution"].keys())
        probs = list(result["grade_distribution"].values())
        
        bar_colors = [
            "#4F46E5" if g == result["predicted_grade"] else "rgba(148, 163, 184, 0.25)"
            for g in grades
        ]

        fig = go.Figure(data=[
            go.Bar(
                x=grades,
                y=probs,
                marker=dict(color=bar_colors, line=dict(color='rgba(255, 255, 255, 0.25)', width=1)),
                text=[f"{p:.1f}%" for p in probs],
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
            xaxis=dict(title="Academic Grades", showgrid=False),
            yaxis=dict(title="Probability (%)", showgrid=True, gridcolor='rgba(255, 255, 255, 0.06)', range=[0, 105]),
            height=260
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

    else:
        st.info("👈 Adjust student metrics on the left or select a **Quick Test Preset** above to generate an evaluation.")
