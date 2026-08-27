"""
Awwwards-Tier Design System for S.A.P.P.M
Engineered using high-end agency design directives:
- Ethereal Glass OLED Canvas with Ambient Radial Lighting
- Double-Bezel (Doppelrand) Nested Component Architecture
- Button-in-Button Island Interactions
- Plus Jakarta Sans + JetBrains Mono Typography
"""

import streamlit as st

def apply_global_styles():
    """
    Injects the complete agency design system across all Streamlit pages.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap');

        /* 1. Root Canvas & Ambient Lighting */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
            background-color: #05070E !important;
            background-image: 
                radial-gradient(circle at 50% -10%, rgba(99, 102, 241, 0.18) 0%, transparent 60%),
                radial-gradient(circle at 100% 20%, rgba(56, 189, 248, 0.12) 0%, transparent 50%),
                radial-gradient(circle at 0% 80%, rgba(139, 92, 246, 0.10) 0%, transparent 60%) !important;
            background-attachment: fixed !important;
            color: #F8FAFC !important;
            letter-spacing: -0.02em;
        }

        /* 2. Layout & Spacing Rhythm */
        .main .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 6rem !important;
            max-width: 1260px;
        }

        /* 3. Sleek Floating Sidebar */
        section[data-testid="stSidebar"] {
            background: rgba(7, 11, 22, 0.85) !important;
            backdrop-filter: blur(25px) !important;
            -webkit-backdrop-filter: blur(25px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.07) !important;
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem !important;
        }
        [data-testid="stSidebarNav"] span {
            font-size: 0.92rem !important;
            font-weight: 600 !important;
            color: #94A3B8 !important;
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }
        [data-testid="stSidebarNav"] a:hover span, [data-testid="stSidebarNav"] a[aria-current="page"] span {
            color: #818CF8 !important;
        }

        /* 4. Double-Bezel (Doppelrand) Card Architecture */
        .bezel-shell {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 6px;
            margin-bottom: 1.5rem;
            box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .bezel-shell:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 25px 50px -12px rgba(99, 102, 241, 0.25);
            transform: translateY(-3px);
        }
        .bezel-core {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(9, 14, 28, 0.95) 100%);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 19px;
            padding: 1.75rem;
            box-shadow: inset 0 1px 1px 0 rgba(255, 255, 255, 0.12);
        }

        /* 5. Eyebrow Tags & Hero Typography */
        .hero-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 0.35rem 1.1rem;
            background: rgba(99, 102, 241, 0.1);
            border: 1px solid rgba(99, 102, 241, 0.35);
            border-radius: 9999px;
            color: #A5B4FC;
            font-size: 0.76rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            box-shadow: 0 0 25px -5px rgba(99, 102, 241, 0.4);
        }
        .hero-headline {
            font-size: 3.4rem !important;
            font-weight: 900 !important;
            background: linear-gradient(135deg, #FFFFFF 20%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            margin-bottom: 1.25rem;
            letter-spacing: -0.04em;
        }
        .hero-lead {
            font-size: 1.15rem;
            color: #94A3B8;
            max-width: 780px;
            margin: 0 auto 2.25rem auto;
            line-height: 1.7;
            font-weight: 400;
        }

        /* 6. Kinetic Stat Bento Cards */
        .stat-shell {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 4px;
            transition: all 0.25s ease;
        }
        .stat-shell:hover {
            border-color: rgba(99, 102, 241, 0.35);
            transform: translateY(-2px);
        }
        .stat-core {
            background: linear-gradient(135deg, rgba(16, 24, 44, 0.7) 0%, rgba(10, 15, 30, 0.85) 100%);
            border-radius: 16px;
            padding: 1.5rem 1rem;
            text-align: center;
            box-shadow: inset 0 1px 1px 0 rgba(255, 255, 255, 0.08);
        }
        .stat-number {
            font-size: 2.3rem;
            font-weight: 900;
            color: #FFFFFF;
            font-family: 'JetBrains Mono', monospace;
            letter-spacing: -0.04em;
        }
        .stat-title {
            font-size: 0.75rem;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-weight: 700;
            margin-top: 0.35rem;
        }

        /* 7. High-Gloss Risk Badges */
        .risk-pill-low {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 18px;
            background: rgba(16, 185, 129, 0.12);
            border: 1px solid rgba(16, 185, 129, 0.45);
            border-radius: 9999px;
            color: #34D399;
            font-weight: 800;
            font-size: 0.9rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(16, 185, 129, 0.25);
        }
        .risk-pill-medium {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 18px;
            background: rgba(245, 158, 11, 0.12);
            border: 1px solid rgba(245, 158, 11, 0.45);
            border-radius: 9999px;
            color: #FBBF24;
            font-weight: 800;
            font-size: 0.9rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(245, 158, 11, 0.25);
        }
        .risk-pill-high {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 18px;
            background: rgba(239, 68, 68, 0.12);
            border: 1px solid rgba(239, 68, 68, 0.45);
            border-radius: 9999px;
            color: #F87171;
            font-weight: 800;
            font-size: 0.9rem;
            letter-spacing: 0.04em;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.25);
        }

        /* 8. Kinetic Island Button Styling */
        .stButton > button {
            background: linear-gradient(135deg, #4F46E5 0%, #3B82F6 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.25) !important;
            border-radius: 9999px !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            padding: 0.75rem 1.75rem !important;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
            box-shadow: 0 8px 24px -4px rgba(79, 70, 229, 0.45), inset 0 1px 1px 0 rgba(255, 255, 255, 0.3) !important;
        }
        .stButton > button:hover {
            box-shadow: 0 14px 35px -4px rgba(79, 70, 229, 0.7), inset 0 1px 1px 0 rgba(255, 255, 255, 0.5) !important;
            transform: translateY(-3px) scale(1.01) !important;
            border-color: rgba(255, 255, 255, 0.5) !important;
        }
        .stButton > button:active {
            transform: translateY(0) scale(0.98) !important;
        }

        /* 9. Premium Floating Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px !important;
            background: rgba(12, 18, 35, 0.7) !important;
            backdrop-filter: blur(16px) !important;
            padding: 6px !important;
            border-radius: 9999px !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5) !important;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 9999px !important;
            color: #94A3B8 !important;
            font-weight: 700 !important;
            font-size: 0.9rem !important;
            padding: 8px 20px !important;
            border: none !important;
            transition: all 0.2s ease !important;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.3) 0%, rgba(59, 130, 246, 0.2) 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(99, 102, 241, 0.5) !important;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.3) !important;
        }

        /* 10. Machined Inputs & Sliders */
        input[type="text"], input[type="password"], textarea, select {
            background-color: #080D1A !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 12px !important;
            color: #F8FAFC !important;
            font-size: 0.95rem !important;
            padding: 0.75rem 1.1rem !important;
            box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
        }
        input:focus {
            border-color: #818CF8 !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.3), inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
        }

        /* 11. Streamlit Metrics Hierarchy */
        div[data-testid="stMetricValue"] {
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 900 !important;
            color: #FFFFFF !important;
            font-size: 2.2rem !important;
            letter-spacing: -0.03em !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.8rem !important;
            color: #94A3B8 !important;
            font-weight: 700 !important;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        /* 12. Fine Hairline Dividers */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.12) 50%, transparent 100%);
            margin: 3rem 0;
        }
        </style>
    """, unsafe_allow_html=True)
