
import streamlit as st

st.set_page_config(page_title="StratDesign x CUSD 95", layout="wide")

st.title("StratDesign Solutions + CUSD 95: Community Schools Prototype")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Community Dashboard", "Early Warning", "Family Engagement",
    "Evaluation Metrics", "Digital Literacy", "AI Tutor (K–8)"
])

with tab1:
    st.header("Community Needs Dashboard")
    st.write("Visualizes zip-code level indicators like food insecurity, housing instability, and internet access.")

with tab2:
    st.header("Early Warning System")
    st.write("Predictive student risk score based on attendance, behavior, and neighborhood data.")

with tab3:
    st.header("Family Engagement Tracker")
    st.write("Tracks family participation, language accessibility, and community events.")

with tab4:
    st.header("Evaluation & Performance")
    st.write("Shows impact metrics aligned to Community Schools goals.")

with tab5:
    st.header("Digital Literacy & Workforce Toolkit")
    st.write("Monitors student/family digital skills, job readiness, and career pathways.")

with tab6:
    st.header("AI Tutor (K–8 Subjects)")
    st.write("Supports Algebra, Geometry, Sciences, and Social Sciences with chatbot lessons and quizzes.")
