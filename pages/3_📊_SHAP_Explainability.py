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

has_prediction = "last_prediction" in st.session_state

tab_instance, tab_global = st.tabs(["🎯 Individual Prediction Explanation", "🌐 Global Feature Importance"])

with tab_instance:
    if has_prediction:
        pred = st.session_state["last_prediction"]
        shap_data = pred.get("shap_breakdown", {})
        
        st.markdown(f"""
            <div class="bezel-shell">
                <div class="bezel-core">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div>
                            <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Attribution Analysis</div>
                            <h3 style="margin: 0.2rem 0 0 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">{pred.get('student_name', 'Student Candidate')} (Grade {pred['predicted_grade']})</h3>
                        </div>
                    </div>
        """, unsafe_allow_html=True)

        feature_names = ["Study Hours", "Attendance", "Participation", "Total Score"]
        feature_keys = ["weekly_self_study_hours", "attendance_percentage", "class_participation", "total_score"]
        contributions = [shap_data.get(k, 0) for k in feature_keys]

        colors = ["#10B981" if v >= 0 else "#EF4444" for v in contributions]

        fig = go.Figure(go.Bar(
            x=contributions,
            y=feature_names,
            orientation='h',
            marker=dict(color=colors, line=dict(color='rgba(255,255,255,0.25)', width=1)),
            text=[f"{v:+.3f}" for v in contributions],
            textposition='outside'
        ))

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=10, r=10, t=10, b=10),
            font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
            xaxis=dict(title="SHAP Impact (Positive = Improved Grade Probability, Negative = Decreased)", showgrid=True, gridcolor='rgba(255,255,255,0.06)'),
            yaxis=dict(showgrid=False),
            height=300
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
                    <div style="margin-top: 1rem; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                        <strong style="color: #818CF8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em;">Interpretation Key:</strong>
                        <ul style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; margin: 0.4rem 0 0 0;">
                            <li><strong style="color: #34D399;">Green bars (+):</strong> Behaviors that increased the likelihood of achieving the predicted grade.</li>
                            <li><strong style="color: #F87171;">Red bars (-):</strong> Deficits that reduced student score or lowered the final grade.</li>
                        </ul>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.info("💡 No student evaluation in current memory. Go to the **Predict** page first to generate a student forecast, then return here to inspect its SHAP breakdown.")

with tab_global:
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Dataset-Wide Feature Weighting</div>
                <h3 style="margin: 0.2rem 0 1rem 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Global Feature Importance (1,000,000 Students)</h3>
    """, unsafe_allow_html=True)

    model, _, _ = get_model_assets()
    importances = model.feature_importances_
    features = ["Study Hours", "Attendance", "Participation", "Total Score"]

    fig_global = go.Figure(go.Bar(
        x=features,
        y=importances,
        marker=dict(
            color=['#4F46E5', '#6366F1', '#818CF8', '#3B82F6'],
            line=dict(color='rgba(255,255,255,0.25)', width=1)
        ),
        text=[f"{imp*100:.1f}%" for imp in importances],
        textposition='auto'
    ))

    fig_global.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
        xaxis=dict(title="Predictor Attributes", showgrid=False),
        yaxis=dict(title="Relative Importance Weight", showgrid=True, gridcolor='rgba(255,255,255,0.06)'),
        height=320
    )

    st.plotly_chart(fig_global, use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
