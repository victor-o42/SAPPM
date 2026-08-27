"""
Student Records & Prediction History Page
Fetches logged predictions from Supabase, provides real-time search & filters,
and allows CSV data export for academic reporting.
"""

import streamlit as st
import pandas as pd
from src.ui.styles import apply_global_styles
from src.ui.icons import icon
from src.services.prediction_service import fetch_prediction_history

st.set_page_config(
    page_title="Student Records - S.A.P.P.M",
    layout="wide"
)

apply_global_styles()

st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
        <div style="background: rgba(251, 191, 36, 0.15); padding: 8px; border-radius: 10px; display: flex;">
            {icon("database", size=24, color="#FBBF24")}
        </div>
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: 900; color: #FFFFFF; letter-spacing: -0.03em;">Student Evaluation Records & Database Logs</h1>
    </div>
    <p style="color: #94A3B8; font-size: 1rem; margin-bottom: 1.5rem;">Historical student evaluation logs synchronized with Supabase PostgreSQL cloud storage.</p>
""", unsafe_allow_html=True)

with st.spinner("Loading records from Supabase database..."):
    records = fetch_prediction_history(limit=100)

if records:
    flattened = []
    for r in records:
        s_data = r.get("student_data") or {}
        m_info = r.get("model_info") or {}
        flattened.append({
            "Prediction ID": r.get("prediction_id"),
            "Student Name": s_data.get("student_name", "N/A"),
            "Matric No": s_data.get("matric_number", "N/A"),
            "Study Hours": s_data.get("weekly_self_study_hours", 0),
            "Attendance (%)": s_data.get("attendance_percentage", 0),
            "Participation": s_data.get("class_participation", 0),
            "Total Score": s_data.get("total_score", 0),
            "Predicted Grade": r.get("predicted_grade"),
            "Risk Level": r.get("risk_level"),
            "Confidence (%)": r.get("confidence_score"),
            "Model": m_info.get("model_name", "XGBoost"),
            "Date": r.get("prediction_date", "")[:19].replace("T", " ")
        })
    
    df = pd.DataFrame(flattened)

    # Filter Toolbar in Double-Bezel
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="font-size: 0.72rem; color: #818CF8; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em;">Search & Filter Matrix</div>
                <h4 style="margin: 0.2rem 0 1rem 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 800;">Query Student Database</h4>
    """, unsafe_allow_html=True)

    fcol1, fcol2, fcol3 = st.columns([2, 1, 1])
    with fcol1:
        search_query = st.text_input("Search Student Name or Matric No", placeholder="e.g. Victor or U/2026")
    with fcol2:
        grade_filter = st.selectbox("Filter by Grade", ["All Grades", "A", "B", "C", "D", "F"])
    with fcol3:
        risk_filter = st.selectbox("Filter by Risk Level", ["All Risk Tiers", "LOW RISK", "MEDIUM RISK", "HIGH RISK"])

    st.markdown('</div></div>', unsafe_allow_html=True)

    # Apply filters
    filtered_df = df.copy()
    if search_query:
        filtered_df = filtered_df[
            filtered_df["Student Name"].str.contains(search_query, case=False, na=False) |
            filtered_df["Matric No"].str.contains(search_query, case=False, na=False)
        ]
    if grade_filter != "All Grades":
        filtered_df = filtered_df[filtered_df["Predicted Grade"] == grade_filter]
    if risk_filter != "All Risk Tiers":
        filtered_df = filtered_df[filtered_df["Risk Level"] == risk_filter]

    # Summary Stat Grid
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        st.markdown(f"""
            <div class="stat-shell">
                <div class="stat-core">
                    <div class="stat-number" style="color: #60A5FA;">{len(filtered_df)}</div>
                    <div class="stat-title">Records Found</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with mcol2:
        high_risk_count = (filtered_df["Risk Level"] == "HIGH RISK").sum()
        st.markdown(f"""
            <div class="stat-shell">
                <div class="stat-core">
                    <div class="stat-number" style="color: #F87171;">{high_risk_count}</div>
                    <div class="stat-title">High Risk Tiers</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with mcol3:
        avg_score = filtered_df["Total Score"].mean() if len(filtered_df) > 0 else 0
        st.markdown(f"""
            <div class="stat-shell">
                <div class="stat-core">
                    <div class="stat-number" style="color: #34D399;">{avg_score:.1f}</div>
                    <div class="stat-title">Average Score</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with mcol4:
        avg_conf = filtered_df["Confidence (%)"].mean() if len(filtered_df) > 0 else 0
        st.markdown(f"""
            <div class="stat-shell">
                <div class="stat-core">
                    <div class="stat-number" style="color: #A78BFA;">{avg_conf:.1f}%</div>
                    <div class="stat-title">Avg Confidence</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Table in Double-Bezel
    st.markdown("""
        <div class="bezel-shell">
            <div class="bezel-core">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h4 style="margin: 0; color: #FFFFFF; font-size: 1.15rem; font-weight: 800;">Evaluation Records</h4>
                </div>
    """, unsafe_allow_html=True)
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Export Filtered Records (CSV)",
        data=csv_data,
        file_name="student_evaluation_records.csv",
        mime="text/csv"
    )
    st.markdown('</div></div>', unsafe_allow_html=True)

else:
    st.info("No prediction logs recorded yet. Visit the **Predict** page to generate and store your first student evaluation.")
