"""
Explainable AI (SHAP) Module Page
Explains the internal decision reasoning of the predictive model,
showing how each feature pushes student outcomes towards specific grades.
"""

import streamlit as st
import plotly.graph_objects as go
from src.ui.styles import apply_global_styles
from src.services.prediction_service import get_model_assets

st.set_page_config(
    page_title="SHAP Explainability - S.A.P.P.M",
    page_icon="📊",
    layout="wide"
)

apply_global_styles()

st.title("📊 Explainable AI (SHAP) Analysis")
st.markdown("""
This section demystifies the predictive model using **Shapley Additive exPlanations (SHAP)**.
Rather than treating predictions as a black box, SHAP quantifies the exact contribution of each academic feature.
""")

# Check if there is an active prediction session
has_prediction = "last_prediction" in st.session_state

tab_instance, tab_global = st.tabs(["🎯 Individual Prediction Explanation", "🌐 Global Feature Importance"])

with tab_instance:
    if has_prediction:
        pred = st.session_state["last_prediction"]
        shap_data = pred.get("shap_breakdown", {})
        
        st.subheader(f"Explanation for: {pred.get('student_name', 'Student Candidate')} (Predicted Grade {pred['predicted_grade']})")

        feature_names = ["Study Hours", "Attendance", "Participation", "Total Score"]
        feature_keys = ["weekly_self_study_hours", "attendance_percentage", "class_participation", "total_score"]
        contributions = [shap_data.get(k, 0) for k in feature_keys]

        # Determine colors (positive impact vs negative pull)
        colors = ["#10B981" if v >= 0 else "#EF4444" for v in contributions]

        fig = go.Figure(go.Bar(
            x=contributions,
            y=feature_names,
            orientation='h',
            marker=dict(color=colors, line=dict(color='rgba(255,255,255,0.2)', width=1)),
            text=[f"{v:+.3f}" for v in contributions],
            textposition='outside'
        ))

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=20, r=20, t=30, b=20),
            font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
            xaxis=dict(title="SHAP Contribution (Positive = Improved Grade, Negative = Lowered Grade)", showgrid=True, gridcolor='rgba(255,255,255,0.06)'),
            yaxis=dict(showgrid=False),
            height=320
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
            <div class="glass-card">
                <h4 style="margin-top:0; color:#60A5FA;">Interpretation Guide:</h4>
                <ul style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6; margin-bottom: 0;">
                    <li><strong style="color: #34D399;">Green bars:</strong> Factors that positively increased the probability of receiving the predicted grade.</li>
                    <li><strong style="color: #F87171;">Red bars:</strong> Factors that reduced the student's score or pulled the predicted grade down.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.info("💡 No student evaluation in current memory. Go to the **Predict** page first to generate a student forecast, then return here to inspect its SHAP breakdown.")

with tab_global:
    st.subheader("Global Feature Importance (Across 1,000,000 Students)")
    st.markdown("Relative ranking of how much each variable influences final grades across the entire dataset:")

    model, _, _ = get_model_assets()
    importances = model.feature_importances_
    features = ["Study Hours", "Attendance", "Participation", "Total Score"]

    fig_global = go.Figure(go.Bar(
        x=features,
        y=importances,
        marker=dict(
            color=['#3B82F6', '#60A5FA', '#93C5FD', '#2563EB'],
            line=dict(color='rgba(255,255,255,0.2)', width=1)
        ),
        text=[f"{imp*100:.1f}%" for imp in importances],
        textposition='auto'
    ))

    fig_global.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
        xaxis=dict(title="Predictor Attributes", showgrid=False),
        yaxis=dict(title="Relative Importance Weight", showgrid=True, gridcolor='rgba(255,255,255,0.06)'),
        height=340
    )

    st.plotly_chart(fig_global, use_container_width=True)
