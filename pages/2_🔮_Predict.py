"""
Student Performance Prediction Page
Provides input controls for academic indicators, generates real-time predictions,
renders probability distribution charts, and syncs records to Supabase.
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

col_input, col_output = st.columns([1.1, 1.4], gap="large")

with col_input:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Student Details & Metrics")
    
    student_name = st.text_input("Student Full Name (Optional)", placeholder="e.g. Victor Okafor", value="Student Candidate")
    matric_number = st.text_input("Matriculation / ID Number", placeholder="e.g. U/2026/CSC/104")
    
    st.markdown("<hr style='margin: 1rem 0;'>", unsafe_allow_html=True)
    st.markdown("#### Academic & Behavioral Indicators")

    study_hours = st.slider(
        "Weekly Self Study Hours",
        min_value=0.0,
        max_value=40.0,
        value=15.0,
        step=0.5,
        help="Average hours the student spends on independent study each week."
    )

    attendance = st.slider(
        "Attendance Percentage (%)",
        min_value=0.0,
        max_value=100.0,
        value=85.0,
        step=1.0,
        help="Percentage of scheduled lectures and practicals attended."
    )

    participation = st.slider(
        "Class Participation Score (0 - 10)",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.5,
        help="Engagement score in questions, discussions, and laboratory sessions."
    )

    total_score = st.slider(
        "Total Assessment & Quiz Score (0 - 100)",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.5,
        help="Cumulative score from assignments, tests, and quizzes."
    )

    predict_btn = st.button("Generate Performance Forecast", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col_output:
    if predict_btn or "last_prediction" in st.session_state:
        if predict_btn:
            with st.spinner("Analyzing student metrics with XGBoost..."):
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

        # Results Summary Card
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        rcol1, rcol2, rcol3 = st.columns(3)
        with rcol1:
            st.metric("Predicted Grade", f"Grade {result['predicted_grade']}")
        with rcol2:
            st.metric("Certainty / Confidence", f"{result['confidence_score']:.1f}%")
        with rcol3:
            badge_class = (
                "risk-badge-low" if "LOW" in result["risk_level"]
                else "risk-badge-medium" if "MEDIUM" in result["risk_level"]
                else "risk-badge-high"
            )
            st.markdown(f"""
                <div style="text-align: center; margin-top: 0.5rem;">
                    <div style="font-size: 0.8rem; color: #94A3B8; margin-bottom: 0.25rem;">ASSESSED RISK</div>
                    <span class="{badge_class}">{result['risk_level']}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<hr style='margin: 1.2rem 0;'>", unsafe_allow_html=True)
        
        # Actionable Recommendation
        st.markdown(f"**Academic Advisor Note:** {result['recommendation']}")
        st.caption("✅ Record automatically synchronized with Supabase database.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Plotly Probability Distribution Chart
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Grade Probability Distribution")
        
        grades = list(result["grade_distribution"].keys())
        probs = list(result["grade_distribution"].values())
        
        # Color the bars nicely with the predicted grade highlighted
        bar_colors = [
            "#3B82F6" if g == result["predicted_grade"] else "rgba(148, 163, 184, 0.4)"
            for g in grades
        ]

        fig = go.Figure(data=[
            go.Bar(
                x=grades,
                y=probs,
                marker=dict(color=bar_colors, line=dict(color='rgba(255, 255, 255, 0.2)', width=1)),
                text=[f"{p:.1f}%" for p in probs],
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=30, b=20),
            font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
            xaxis=dict(title="Academic Grades", showgrid=False),
            yaxis=dict(title="Probability (%)", showgrid=True, gridcolor='rgba(255, 255, 255, 0.06)', range=[0, 105]),
            height=280
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.info("👈 Adjust student metrics on the left and click **'Generate Performance Forecast'** to view prediction results.")
