"""
Ultra-Modern Design System for S.A.P.P.M
Enforces high-end agency aesthetics: ambient glow meshes, frosted glassmorphism,
refined typography, glowing badges, and fluid interactive components.
"""

import streamlit as st

def apply_global_styles():
    """
    Applies custom CSS variables, ambient glow backgrounds, sleek bento cards,
    and ultra-modern typography across the application.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap');

        /* Root Canvas & Ambient Lighting */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            background-color: #070B14 !important;
            background-image: 
                radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(56, 189, 248, 0.10) 0px, transparent 50%),
                radial-gradient(at 50% 100%, rgba(139, 92, 246, 0.08) 0px, transparent 50%) !important;
            background-attachment: fixed !important;
            color: #F8FAFC !important;
            letter-spacing: -0.018em;
        }

        /* Container Margins & Fluid Padding */
        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 5rem !important;
            max-width: 1240px;
        }

        /* Modern Sidebar Navigation */
        section[data-testid="stSidebar"] {
            background: rgba(10, 15, 29, 0.85) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem !important;
        }
        [data-testid="stSidebarNav"] {
            padding-top: 1rem !important;
        }
        [data-testid="stSidebarNav"] span {
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            color: #CBD5E1 !important;
            transition: all 0.2s ease;
        }
        [data-testid="stSidebarNav"] a:hover span {
            color: #818CF8 !important;
        }

        /* High-End Bento Glass Cards */
        .glass-card {
            background: linear-gradient(135deg, rgba(17, 24, 43, 0.7) 0%, rgba(11, 17, 32, 0.85) 100%);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 18px;
            padding: 1.85rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5), inset 0 1px 0 0 rgba(255, 255, 255, 0.08);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 20px 45px -10px rgba(99, 102, 241, 0.25), inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            transform: translateY(-2px);
        }

        /* Hero Header Typography */
        .hero-container {
            padding: 2.5rem 1rem 2rem 1rem;
            text-align: center;
            position: relative;
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 0.45rem 1.2rem;
            background: rgba(99, 102, 241, 0.12);
            border: 1px solid rgba(99, 102, 241, 0.35);
            border-radius: 9999px;
            color: #818CF8;
            font-size: 0.82rem;
            font-weight: 700;
            margin-bottom: 1.25rem;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
        }
        .hero-title {
            font-size: 3rem !important;
            font-weight: 900 !important;
            background: linear-gradient(135deg, #FFFFFF 30%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.12;
            margin-bottom: 0.9rem;
            letter-spacing: -0.035em;
        }
        .hero-subtitle {
            font-size: 1.12rem;
            color: #94A3B8;
            max-width: 760px;
            margin: 0 auto 1.75rem auto;
            line-height: 1.7;
            font-weight: 400;
        }

        /* Stat Counter Cards */
        .stat-card {
            background: linear-gradient(135deg, rgba(20, 29, 51, 0.6) 0%, rgba(13, 19, 36, 0.8) 100%);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 16px;
            padding: 1.5rem 1.2rem;
            text-align: center;
            box-shadow: 0 8px 24px -5px rgba(0, 0, 0, 0.4);
            transition: all 0.2s ease;
        }
        .stat-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            transform: translateY(-2px);
        }
        .stat-value {
            font-size: 2.2rem;
            font-weight: 900;
            color: #FFFFFF;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: -0.03em;
        }
        .stat-label {
            font-size: 0.78rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 700;
            margin-top: 0.4rem;
        }

        /* Glowing Risk Level Badges */
        .risk-badge-low {
            display: inline-block;
            padding: 7px 20px;
            background: rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.5);
            border-radius: 10px;
            color: #34D399;
            font-weight: 800;
            font-size: 1rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.2);
        }
        .risk-badge-medium {
            display: inline-block;
            padding: 7px 20px;
            background: rgba(245, 158, 11, 0.15);
            border: 1px solid rgba(245, 158, 11, 0.5);
            border-radius: 10px;
            color: #FBBF24;
            font-weight: 800;
            font-size: 1rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.2);
        }
        .risk-badge-high {
            display: inline-block;
            padding: 7px 20px;
            background: rgba(239, 68, 68, 0.15);
            border: 1px solid rgba(239, 68, 68, 0.5);
            border-radius: 10px;
            color: #F87171;
            font-weight: 800;
            font-size: 1rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.2);
        }

        /* Premium Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            padding: 0.65rem 1.4rem !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-shadow: 0 4px 18px 0 rgba(79, 70, 229, 0.35) !important;
        }
        .stButton > button:hover {
            box-shadow: 0 8px 25px 0 rgba(79, 70, 229, 0.6) !important;
            transform: translateY(-2px) !important;
            border-color: rgba(255, 255, 255, 0.4) !important;
        }

        /* Tab Navigation Bar */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px !important;
            background: rgba(15, 23, 42, 0.6) !important;
            padding: 6px !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px !important;
            color: #94A3B8 !important;
            font-weight: 600 !important;
            padding: 8px 16px !important;
            border: none !important;
        }
        .stTabs [aria-selected="true"] {
            background: rgba(99, 102, 241, 0.2) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(99, 102, 241, 0.4) !important;
        }

        /* Custom Form Input Polish */
        input[type="text"], input[type="password"], textarea, select {
            background-color: #0A0F1E !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 10px !important;
            color: #F8FAFC !important;
            font-size: 0.95rem !important;
            padding: 0.65rem 1rem !important;
        }
        input:focus {
            border-color: #6366F1 !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25) !important;
        }

        /* Streamlit Metrics */
        div[data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 900 !important;
            color: #FFFFFF !important;
            font-size: 2.1rem !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.85rem !important;
            color: #94A3B8 !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        /* Custom Dividers */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.1) 50%, transparent 100%);
            margin: 2.5rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
