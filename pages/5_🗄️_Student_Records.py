"""
Student Records & Prediction History Page
Fetches logged predictions from Supabase, provides real-time search & filters,
and allows CSV data export for academic reporting.
"""

import streamlit as st
import pandas as pd
from src.ui.styles import apply_global_styles
from src.services.prediction_service import fetch_prediction_history

st.set_page_config(
    page_title="Student Records - S.A.P.P.M",
    page_icon="🗄️",
    layout="wide"
)

apply_global_styles()

st.title("🗄️ Student Evaluation Records & Prediction Logs")
st.markdown("Historical student evaluation logs stored in Supabase PostgreSQL.")

# Fetch records from Supabase
with st.spinner("Loading records from Supabase database..."):
    records = fetch_prediction_history(limit=100)

if records:
    # Flatten records for DataFrame
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

    # Search and Filter Toolbar
    fcol1, fcol2, fcol3 = st.columns([2, 1, 1])
    with fcol1:
        search_query = st.text_input("🔍 Search Student Name or Matric No", placeholder="e.g. Victor or U/2026")
    with fcol2:
        grade_filter = st.selectbox("Filter by Grade", ["All Grades", "A", "B", "C", "D", "F"])
    with fcol3:
        risk_filter = st.selectbox("Filter by Risk Level", ["All Risk Tiers", "LOW RISK", "MEDIUM RISK", "HIGH RISK"])

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

    # Summary metric pills
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        st.metric("Total Records Found", len(filtered_df))
    with mcol2:
        high_risk_count = (filtered_df["Risk Level"] == "HIGH RISK").sum()
        st.metric("High Risk Count", high_risk_count)
    with mcol3:
        avg_score = filtered_df["Total Score"].mean() if len(filtered_df) > 0 else 0
        st.metric("Average Score", f"{avg_score:.1f}")
    with mcol4:
        avg_conf = filtered_df["Confidence (%)"].mean() if len(filtered_df) > 0 else 0
        st.metric("Average Confidence", f"{avg_conf:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Table Display
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    # Export to CSV
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Export Filtered Records (CSV)",
        data=csv_data,
        file_name="student_evaluation_records.csv",
        mime="text/csv"
    )

else:
    st.info("No prediction logs recorded yet. Visit the **Predict** page to generate and store your first student evaluation.")
