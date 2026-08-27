"""
Global Design System & Styles for S.A.P.P.M
Injects modern dark theme styling, glassmorphism tokens, custom metric cards,
and typography improvements.
"""

import streamlit as st

def apply_global_styles():
    """
    Applies custom CSS variables, fonts, glassmorphic cards, and refined UI styling.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        /* Base Typography & Background */
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            letter-spacing: -0.01em;
        }

        /* Glassmorphic Card Containers */
        .glass-card {
            background: rgba(18, 24, 38, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 14px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.2s ease-in-out;
        }
        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.3);
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
        }

        /* Hero Header */
        .hero-container {
            padding: 2.5rem 1rem 1.5rem 1rem;
            text-align: center;
        }
        .hero-badge {
            display: inline-block;
            padding: 0.35rem 1rem;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 9999px;
            color: #818CF8;
            font-size: 0.8rem;
            font-weight: 600;
            margin-bottom: 1rem;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        .hero-title {
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(135deg, #FFFFFF 30%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.15;
            margin-bottom: 0.75rem;
        }
        .hero-subtitle {
            font-size: 1.05rem;
            color: #94A3B8;
            max-width: 680px;
            margin: 0 auto 1.5rem auto;
            line-height: 1.6;
        }

        /* Metric Pill & Stat Badges */
        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }
        .stat-card {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 12px;
            padding: 1.25rem;
            text-align: center;
        }
        .stat-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: #F8FAFC;
            font-family: 'JetBrains Mono', monospace;
        }
        .stat-label {
            font-size: 0.82rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-top: 0.25rem;
        }

        /* Risk Badges */
        .risk-badge-low {
            display: inline-block;
            padding: 6px 16px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.4);
            border-radius: 8px;
            color: #34D399;
            font-weight: 700;
            font-size: 0.95rem;
        }
        .risk-badge-medium {
            display: inline-block;
            padding: 6px 16px;
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.4);
            border-radius: 8px;
            color: #FBBF24;
            font-weight: 700;
            font-size: 0.95rem;
        }
        .risk-badge-high {
            display: inline-block;
            padding: 6px 16px;
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid rgba(239, 68, 68, 0.4);
            border-radius: 8px;
            color: #F87171;
            font-weight: 700;
            font-size: 0.95rem;
        }

        /* Streamlit Input & Slider Refinements */
        div[data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
        }
        
        /* Subtle divider */
        hr {
            border: none;
            height: 1px;
            background: rgba(255, 255, 255, 0.06);
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
