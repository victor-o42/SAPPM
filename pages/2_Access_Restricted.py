"""
Clean, Minimalist 404 Error Page for S.A.P.P.M
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="404 - Page Not Found",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Global Scrollbar Killer & Full Viewport Lock
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap');

    ::-webkit-scrollbar { display: none !important; }
    * { scrollbar-width: none !important; -ms-overflow-style: none !important; }

    [data-testid="stSidebar"] { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu, footer { visibility: hidden !important; }

    html, body, [class*="css"], .stApp {
        background-color: #05070E !important;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
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
    </style>
""", unsafe_allow_html=True)

error_html = """
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
            text-align: center;
        }

        /* Ambient Glow */
        .ambient-glow {
            position: absolute;
            top: 40%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 600px;
            height: 400px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(56, 189, 248, 0.08) 50%, transparent 75%);
            filter: blur(80px);
            pointer-events: none;
            z-index: 1;
        }

        .content-box {
            position: relative;
            z-index: 10;
            max-width: 480px;
            padding: 0 20px;
        }

        .error-code {
            font-family: 'JetBrains Mono', monospace;
            font-size: 6.5rem;
            font-weight: 900;
            letter-spacing: -0.06em;
            line-height: 1;
            background: linear-gradient(180deg, #FFFFFF 0%, #64748B 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        .error-title {
            font-size: 1.6rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: #FFFFFF;
            margin-bottom: 0.6rem;
        }

        .error-desc {
            font-size: 0.95rem;
            color: #94A3B8;
            line-height: 1.55;
            margin-bottom: 2rem;
        }

        .back-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 30px;
            border-radius: 9999px;
            background: #FFFFFF;
            color: #05070E;
            font-size: 0.92rem;
            font-weight: 800;
            cursor: pointer;
            text-decoration: none;
            box-shadow: 0 4px 20px rgba(255, 255, 255, 0.25);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .back-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(255, 255, 255, 0.4);
        }
    </style>
</head>
<body>
    <div class="ambient-glow"></div>

    <div class="content-box">
        <div class="error-code">404</div>
        <h1 class="error-title">Page Not Found</h1>
        <p class="error-desc">
            The page or module you are looking for doesn't exist or is currently unavailable.
        </p>
        <div class="back-btn" onclick="navTo('/')">
            <span>← Back to Home</span>
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
