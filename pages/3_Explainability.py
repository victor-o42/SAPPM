"""
Explainable AI (SHAP) Module Page
Explains the internal decision reasoning of the predictive model,
showing how each feature pushes student outcomes towards specific grades.
"""

import streamlit as st
import plotly.graph_objects as go
from src.ui.styles import apply_global_styles
from src.ui.icons import icon
from src.services.prediction_service import get_model_assets

st.set_page_config(
    page_title="SHAP Explainability - S.A.P.P.M",
    layout="wide"
)

apply_global_styles()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
        <div style="background: rgba(244, 114, 182, 0.15); padding: 8px; border-radius: 10px; display: flex;">
            {icon("chart", size=24, color="#F472B6")}
        </div>
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em;">Explainable AI (SHAP) Attribution</h1>
    </div>
    <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 1.5rem;">Demystifying machine learning decisions through cooperative game-theory Shapley values.</p>
""", unsafe_allow_html=True)

has_prediction = "last_prediction" in st.session_state

tab_instance, tab_global = st.tabs(["Individual Student Attribution", "Dataset Global Importance"])

with tab_instance:
    if has_prediction:
        pred = st.session_state["last_prediction"]
        shap_data = pred.get("shap_breakdown", {})
        
        st.markdown(f"""
            <div class="bezel-shell">
                <div class="bezel-core">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <div>
                            <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Feature Attribution Breakdown</div>
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
            xaxis=dict(title="SHAP Impact (Positive = Improved Outcome Likelihood, Negative = Reduced)", showgrid=True, gridcolor='rgba(255,255,255,0.06)'),
            yaxis=dict(showgrid=False),
            height=300
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""
                    <div style="margin-top: 1rem; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 12px; padding: 1rem;">
                        <strong style="color: #818CF8; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em;">Interpretation Key:</strong>
                        <ul style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; margin: 0.4rem 0 0 0;">
                            <li><strong style="color: #34D399;">Positive Impact (+):</strong> Behaviors and metrics that positively drove the model towards this predicted grade.</li>
                            <li><strong style="color: #F87171;">Negative Impact (-):</strong> Deficits that reduced student performance or lowered the final outcome.</li>
                        </ul>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.info("No student evaluation in current memory. Go to the **Predict** page first to generate a forecast, then return here to inspect its SHAP breakdown.")

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
