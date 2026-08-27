"""
Model Benchmarks & Comparison Page
Displays live model registry data from Supabase, comparative charts,
and evaluation metrics across candidate algorithms.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.ui.styles import apply_global_styles
from src.services.prediction_service import fetch_model_registry

st.set_page_config(
    page_title="Model Analytics - S.A.P.P.M",
    page_icon="📈",
    layout="wide"
)

apply_global_styles()

st.title("📈 Machine Learning Model Benchmarks")
st.markdown("Comparative performance evaluation across the candidate algorithms trained on the student performance dataset.")

# Fetch live registry from Supabase
with st.spinner("Fetching model benchmarks from Supabase..."):
    models = fetch_model_registry()

if models:
    df_models = pd.DataFrame(models)
    
    # Leaderboard Cards
    m1, m2, m3 = st.columns(3)
    
    if len(models) >= 1:
        with m1:
            st.markdown(f"""
                <div class="glass-card" style="border-color: rgba(59, 130, 246, 0.4);">
                    <div style="font-size: 0.8rem; color: #60A5FA; font-weight: 700; text-transform: uppercase;">🏆 Champion Model</div>
                    <h3 style="margin: 0.4rem 0; color: #F8FAFC;">{models[0]['model_name']}</h3>
                    <div style="font-size: 2rem; font-weight: 800; color: #34D399; font-family: 'JetBrains Mono', monospace;">{models[0]['accuracy']:.2f}%</div>
                    <div style="font-size: 0.85rem; color: #94A3B8;">F1-Score: {models[0]['f1_score']:.2f}%</div>
                </div>
            """, unsafe_allow_html=True)
            
    if len(models) >= 2:
        with m2:
            st.markdown(f"""
                <div class="glass-card">
                    <div style="font-size: 0.8rem; color: #94A3B8; font-weight: 700; text-transform: uppercase;">Runner-Up</div>
                    <h3 style="margin: 0.4rem 0; color: #F8FAFC;">{models[1]['model_name']}</h3>
                    <div style="font-size: 2rem; font-weight: 800; color: #60A5FA; font-family: 'JetBrains Mono', monospace;">{models[1]['accuracy']:.2f}%</div>
                    <div style="font-size: 0.85rem; color: #94A3B8;">F1-Score: {models[1]['f1_score']:.2f}%</div>
                </div>
            """, unsafe_allow_html=True)
            
    if len(models) >= 3:
        with m3:
            st.markdown(f"""
                <div class="glass-card">
                    <div style="font-size: 0.8rem; color: #94A3B8; font-weight: 700; text-transform: uppercase;">Baseline</div>
                    <h3 style="margin: 0.4rem 0; color: #F8FAFC;">{models[2]['model_name']}</h3>
                    <div style="font-size: 2rem; font-weight: 800; color: #A78BFA; font-family: 'JetBrains Mono', monospace;">{models[2]['accuracy']:.2f}%</div>
                    <div style="font-size: 0.85rem; color: #94A3B8;">F1-Score: {models[2]['f1_score']:.2f}%</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Comparative Metric Bar Chart
    st.subheader("Multi-Metric Algorithm Comparison")
    
    model_names = [m['model_name'].split(' (')[0] for m in models]
    accuracies = [m['accuracy'] for m in models]
    precisions = [m['precision'] for m in models]
    recalls = [m['recall'] for m in models]
    f1s = [m['f1_score'] for m in models]

    fig = go.Figure(data=[
        go.Bar(name='Accuracy', x=model_names, y=accuracies, marker_color='#3B82F6'),
        go.Bar(name='Precision', x=model_names, y=precisions, marker_color='#10B981'),
        go.Bar(name='Recall', x=model_names, y=recalls, marker_color='#F59E0B'),
        go.Bar(name='F1-Score', x=model_names, y=f1s, marker_color='#8B5CF6')
    ])

    fig.update_layout(
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=30, b=20),
        font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
        yaxis=dict(title="Score (%)", range=[85, 102], showgrid=True, gridcolor='rgba(255, 255, 255, 0.06)'),
        height=380,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Detailed Table
    st.subheader("Model Evaluation Summary Table")
    display_df = df_models[['model_name', 'accuracy', 'precision', 'recall', 'f1_score', 'training_date']].copy()
    display_df.columns = ['Algorithm', 'Accuracy (%)', 'Precision (%)', 'Recall (%)', 'F1-Score (%)', 'Trained At']
    st.dataframe(display_df, use_container_width=True, hide_index=True)

else:
    st.info("No model records found in Supabase. Please ensure the schema has been executed.")
