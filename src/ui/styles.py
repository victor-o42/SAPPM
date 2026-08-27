"""
Premium Design System for S.A.P.P.M
Injects modern dark theme tokens, glassmorphic bento cards, curated gradients,
and refined typography inspired by taste-skill guidelines.
"""

import streamlit as st

def apply_global_styles():
    """
    Applies custom CSS variables, refined typography, glowing glassmorphic cards,
    and polished UI components across all Streamlit pages.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

        /* Global Typography & Palette */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            letter-spacing: -0.015em;
            color: #F8FAFC;
        }

        /* Top Header & Main Padding */
        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 4rem !important;
            max-width: 1200px;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #0E1424 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2.5rem !important;
        }

        /* Glassmorphic Bento Cards */
        .glass-card {
            background: linear-gradient(135deg, rgba(18, 26, 45, 0.75) 0%, rgba(13, 19, 33, 0.85) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.75rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.35);
            box-shadow: 0 12px 40px -10px rgba(99, 102, 241, 0.2);
            transform: translateY(-2px);
        }

        /* Hero Section */
        .hero-container {
            padding: 2.5rem 1rem 2rem 1rem;
            text-align: center;
            position: relative;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 0.4rem 1.1rem;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 9999px;
            color: #818CF8;
            font-size: 0.82rem;
            font-weight: 600;
            margin-bottom: 1.25rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }
        .hero-title {
            font-size: 2.75rem !important;
            font-weight: 800 !important;
            background: linear-gradient(135deg, #FFFFFF 20%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.15;
            margin-bottom: 0.85rem;
            letter-spacing: -0.03em;
        }
        .hero-subtitle {
            font-size: 1.08rem;
            color: #94A3B8;
            max-width: 720px;
            margin: 0 auto 1.5rem auto;
            line-height: 1.65;
            font-weight: 400;
        }

        /* Stat Counter Cards */
        .stat-card {
            background: linear-gradient(135deg, rgba(22, 32, 54, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 14px;
            padding: 1.4rem 1rem;
            text-align: center;
            transition: all 0.2s ease;
        }
        .stat-card:hover {
            border-color: rgba(99, 102, 241, 0.3);
        }
        .stat-value {
            font-size: 2rem;
            font-weight: 800;
            color: #F8FAFC;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: -0.02em;
        }
        .stat-label {
            font-size: 0.8rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            font-weight: 600;
            margin-top: 0.35rem;
        }

        /* Risk Badges */
        .risk-badge-low {
            display: inline-block;
            padding: 6px 18px;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.35);
            border-radius: 8px;
            color: #34D399;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.02em;
        }
        .risk-badge-medium {
            display: inline-block;
            padding: 6px 18px;
            background: rgba(245, 158, 11, 0.12);
            border: 1px solid rgba(245, 158, 11, 0.35);
            border-radius: 8px;
            color: #FBBF24;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.02em;
        }
        .risk-badge-high {
            display: inline-block;
            padding: 6px 18px;
            background: rgba(239, 68, 68, 0.12);
            border: 1px solid rgba(239, 68, 68, 0.35);
            border-radius: 8px;
            color: #F87171;
            font-weight: 700;
            font-size: 0.95rem;
            letter-spacing: 0.02em;
        }

        /* Button Styling */
        .stButton > button {
            background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            padding: 0.6rem 1.25rem !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.3) !important;
        }
        .stButton > button:hover {
            box-shadow: 0 6px 20px 0 rgba(79, 70, 229, 0.5) !important;
            transform: translateY(-1px) !important;
            border-color: rgba(255, 255, 255, 0.3) !important;
        }
        .stButton > button:active {
            transform: translateY(0) !important;
        }

        /* Form & Input Enhancements */
        input[type="text"], input[type="password"], textarea, select {
            background-color: #0E1424 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 8px !important;
            color: #F8FAFC !important;
            font-size: 0.92rem !important;
        }
        input:focus {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
        }

        /* Streamlit Metrics */
        div[data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 800 !important;
            color: #F8FAFC !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.85rem !important;
            color: #94A3B8 !important;
            font-weight: 500 !important;
        }

        /* Custom Dividers */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, rgba(255, 255, 255, 0.02) 0%, rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.02) 100%);
            margin: 2rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
