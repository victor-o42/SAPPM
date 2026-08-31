"""
Custom Access Restricted / 403 Error Page for S.A.P.P.M
Displayed when unauthenticated users attempt to access internal modules from the landing page.
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Access Restricted - S.A.P.P.M",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Global Scrollbar & Layout Styling: Complete Sidebar & Chrome Hiding + Glass Back Button
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    /* Kill all scrollbars */
    ::-webkit-scrollbar {
        display: none !important;
        width: 0 !important;
        height: 0 !important;
    }
    * {
        scrollbar-width: none !important;
        -ms-overflow-style: none !important;
    }

    [data-testid="stSidebar"] { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { visibility: hidden !important; }

    html, body, [class*="css"], .stApp {
        background-color: #05070E !important;
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: #FFFFFF !important;
        overflow: hidden !important;
        height: 100vh !important;
        width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .main .block-container {
        max-width: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    iframe {
        width: 100% !important;
        border: none !important;
    }

    /* Double-Bezel Native Back to Home Pill */
    [data-testid="stPageLink"] {
        position: fixed !important;
        top: 24px !important;
        left: 36px !important;
        z-index: 999999 !important;
    }

    [data-testid="stPageLink"] a {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        padding: 10px 22px !important;
        border-radius: 9999px !important;
        background: rgba(15, 23, 42, 0.65) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.2) !important;
        color: #CBD5E1 !important;
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        cursor: pointer !important;
    }

    [data-testid="stPageLink"] a:hover {
        color: #FFFFFF !important;
        border-color: rgba(255, 255, 255, 0.4) !important;
        background: rgba(15, 23, 42, 0.9) !important;
        box-shadow: 0 12px 30px -2px rgba(99, 102, 241, 0.3), inset 0 1px 1px 0 rgba(255, 255, 255, 0.4) !important;
        transform: translateX(-4px) !important;
    }

    [data-testid="stPageLink"] a p {
        font-size: 0.82rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        margin: 0 !important;
        color: inherit !important;
    }
    </style>
""", unsafe_allow_html=True)

# Native Root Page Link
st.page_link("app.py", label="← Back to Home")

module_name = st.query_params.get("module", "Internal System Module")

error_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            user-select: none;
        }

        body {
            background-color: #05070E;
            color: #FFFFFF;
            width: 100%;
            height: 100vh;
            overflow: hidden;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        /* Ambient Glow Backgrounds */
        .ambient-top {
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
            width: 700px;
            height: 450px;
            background: radial-gradient(circle, rgba(239, 68, 68, 0.18) 0%, rgba(139, 92, 246, 0.1) 45%, transparent 75%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 1;
        }

        /* Error Card */
        .error-card {
            position: relative;
            z-index: 10;
            max-width: 520px;
            width: 90%;
            text-align: center;
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 28px;
            padding: 42px 36px;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8), 0 0 35px rgba(239, 68, 68, 0.15);
            animation: fadeInScale 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: scale(0.95) translateY(12px);
            }
            to {
                opacity: 1;
                transform: scale(1) translateY(0);
            }
        }

        .icon-shield-wrap {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            background: rgba(239, 68, 68, 0.12);
            border: 1px solid rgba(239, 68, 68, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
            color: #EF4444;
            box-shadow: 0 0 25px rgba(239, 68, 68, 0.3);
        }

        .error-badge {
            display: inline-block;
            padding: 4px 14px;
            border-radius: 9999px;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: #F87171;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 12px;
            font-family: 'JetBrains Mono', monospace;
        }

        .error-title {
            font-size: 1.85rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            color: #FFFFFF;
            margin-bottom: 10px;
        }

        .error-desc {
            font-size: 0.95rem;
            color: #94A3B8;
            line-height: 1.6;
            margin-bottom: 30px;
        }

        .action-group {
            display: flex;
            gap: 14px;
            justify-content: center;
            flex-wrap: wrap;
        }

        .btn-primary {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 26px;
            border-radius: 9999px;
            background: #FFFFFF;
            color: #05070E;
            font-size: 0.9rem;
            font-weight: 800;
            text-decoration: none;
            border: 1px solid rgba(255, 255, 255, 0.5);
            cursor: pointer;
            box-shadow: 0 4px 20px rgba(255, 255, 255, 0.25);
            transition: all 0.25s ease;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(255, 255, 255, 0.4);
        }

        .btn-secondary {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            border-radius: 9999px;
            background: rgba(255, 255, 255, 0.05);
            color: #CBD5E1;
            font-size: 0.9rem;
            font-weight: 700;
            text-decoration: none;
            border: 1px solid rgba(255, 255, 255, 0.12);
            cursor: pointer;
            transition: all 0.25s ease;
        }
        .btn-secondary:hover {
            color: #FFFFFF;
            border-color: rgba(255, 255, 255, 0.3);
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="ambient-top"></div>

    <div class="error-card">
        <div class="icon-shield-wrap">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
        </div>

        <div class="error-badge">403 &bull; Authorization Required</div>
        <h1 class="error-title">Staff Portal Access Only</h1>
        <p class="error-desc">
            The <strong>{module_name}</strong> requires verified institutional credentials. Please sign in via the Staff Portal to access model prediction analytics and student diagnostics.
        </p>

        <div class="action-group">
            <div class="btn-primary" onclick="navTo('/Staff_Portal')">
                <span>Sign In to Portal ↗</span>
            </div>
            <div class="btn-secondary" onclick="navTo('/')">
                <span>← Return to Home</span>
            </div>
        </div>
    </div>

    <script>
        function navTo(url) {
            try {
                if (window.parent && window.parent.location) {
                    window.parent.location.assign(url);
                    return;
                }
            } catch(e) {}
            try {
                if (window.top && window.top.location) {
                    window.top.location.assign(url);
                    return;
                }
            } catch(e) {}
            window.location.assign(url);
        }
    </script>
</body>
</html>
"""

components.html(error_html, height=880, scrolling=False)
