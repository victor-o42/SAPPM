"""
Model Benchmarks & Comparison Page
Displays live model registry data from Supabase, comparative charts,
and evaluation metrics across candidate algorithms.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.ui.styles import apply_global_styles
from src.ui.icons import icon
from src.services.prediction_service import fetch_model_registry

st.set_page_config(
    page_title="Model Analytics - S.A.P.P.M",
    layout="wide"
)

apply_global_styles()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
        <div style="background: rgba(59, 130, 246, 0.15); padding: 8px; border-radius: 10px; display: flex;">
            {icon("trending_up", size=24, color="#60A5FA")}
        </div>
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em;">Machine Learning Model Benchmarks</h1>
    </div>
    <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 1.5rem;">Comparative performance evaluation across candidate algorithms trained on the student performance dataset.</p>
""", unsafe_allow_html=True)

with st.spinner("Fetching model benchmarks from Supabase..."):
    models = fetch_model_registry()

if models:
    df_models = pd.DataFrame(models)
    
    # Leaderboard Cards in Double-Bezel
    m1, m2, m3 = st.columns(3)
    
    if len(models) >= 1:
        with m1:
            st.markdown(f"""
                <div class="bezel-shell" style="border-color: rgba(99, 102, 241, 0.45);">
                    <div class="bezel-core">
                        <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Champion Algorithm</div>
                        <h3 style="margin: 0.4rem 0 0.2rem 0; color: #FFFFFF; font-size: 1.2rem; font-weight: 800;">{models[0]['model_name']}</h3>
                        <div style="font-size: 2.5rem; font-weight: 900; color: #34D399; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin: 0.5rem 0;">{models[0]['accuracy']:.2f}%</div>
                        <div style="font-size: 0.82rem; color: #94A3B8;">F1-Score: <strong style="color:#F8FAFC;">{models[0]['f1_score']:.2f}%</strong></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    if len(models) >= 2:
        with m2:
            st.markdown(f"""
                <div class="bezel-shell">
                    <div class="bezel-core">
                        <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Runner-Up</div>
                        <h3 style="margin: 0.4rem 0 0.2rem 0; color: #FFFFFF; font-size: 1.2rem; font-weight: 800;">{models[1]['model_name']}</h3>
                        <div style="font-size: 2.5rem; font-weight: 900; color: #60A5FA; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin: 0.5rem 0;">{models[1]['accuracy']:.2f}%</div>
                        <div style="font-size: 0.82rem; color: #94A3B8;">F1-Score: <strong style="color:#F8FAFC;">{models[1]['f1_score']:.2f}%</strong></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    if len(models) >= 3:
        with m3:
            st.markdown(f"""
                <div class="bezel-shell">
                    <div class="bezel-core">
                        <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Baseline Model</div>
                        <h3 style="margin: 0.4rem 0 0.2rem 0; color: #FFFFFF; font-size: 1.2rem; font-weight: 800;">{models[2]['model_name']}</h3>
                        <div style="font-size: 2.5rem; font-weight: 900; color: #A78BFA; font-family: 'JetBrains Mono', monospace; line-height: 1.1; margin: 0.5rem 0;">{models[2]['accuracy']:.2f}%</div>
                        <div style="font-size: 0.82rem; color: #94A3B8;">F1-Score: <strong style="color:#F8FAFC;">{models[2]['f1_score']:.2f}%</strong></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Comparative Multi-Metric Bar Chart
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Comparative Benchmarking</div>
                <h3 style="margin: 0.2rem 0 1rem 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Multi-Metric Algorithm Comparison</h3>
    """, unsafe_allow_html=True)
    
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
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(color='#F8FAFC', family='Plus Jakarta Sans'),
        yaxis=dict(title="Score (%)", range=[85, 102], showgrid=True, gridcolor='rgba(255, 255, 255, 0.06)'),
        height=340,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    # Detailed Table
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Audit Trail</div>
                <h3 style="margin: 0.2rem 0 1rem 0; color: #FFFFFF; font-size: 1.3rem; font-weight: 800;">Model Evaluation Registry</h3>
    """, unsafe_allow_html=True)
    
    display_df = df_models[['model_name', 'accuracy', 'precision', 'recall', 'f1_score', 'training_date']].copy()
    display_df.columns = ['Algorithm', 'Accuracy (%)', 'Precision (%)', 'Recall (%)', 'F1-Score (%)', 'Trained At']
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

else:
    st.info("No model records found in Supabase. Please ensure the schema has been executed.")
