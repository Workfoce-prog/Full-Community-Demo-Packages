
import streamlit as st
import pandas as pd

st.set_page_config(page_title="StratDesign x CUSD 95", layout="wide")

st.title("StratDesign Solutions + CUSD 95: Community Schools Prototype")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Community Dashboard", "Early Warning", "Family Engagement",
    "Evaluation Metrics", "Digital Literacy", "AI Tutor (K–8)"
])

# Community Dashboard
with tab1:
    st.header("Community Needs Dashboard")
    try:
        df = pd.read_csv("data/community_needs.csv")
        st.dataframe(df)
        st.subheader("Food Insecurity Chart")
        st.image("assets/food_insecurity_chart.png")
    except Exception as e:
        st.error(f"Error loading community data: {e}")

# Early Warning
with tab2:
    st.header("Early Warning System")
    try:
        df = pd.read_csv("data/early_warning.csv")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading early warning data: {e}")

# Family Engagement
with tab3:
    st.header("Family Engagement Tracker")
    try:
        df = pd.read_csv("data/family_engagement.csv")
        st.dataframe(df)
        st.image("assets/family_engagement_chart.png")
    except Exception as e:
        st.error(f"Error loading family engagement data: {e}")

# Evaluation Metrics
with tab4:
    st.header("Evaluation Metrics Dashboard")
    try:
        df = pd.read_csv("data/evaluation_metrics.csv")
        st.dataframe(df)
        st.image("assets/evaluation_comparison_chart.png")
    except Exception as e:
        st.error(f"Error loading evaluation data: {e}")

# Digital Literacy
with tab5:
    st.header("Digital Literacy & Workforce Toolkit")
    try:
        df = pd.read_csv("data/digital_literacy.csv")
        st.dataframe(df)
        st.image("assets/digital_literacy_chart.png")
    except Exception as e:
        st.error(f"Error loading digital literacy data: {e}")

# AI Tutor (K–8)
with tab6:
    st.header("AI Tutor Usage (K–8 Subjects)")
    try:
        df = pd.read_csv("data/ai_tutor_usage.csv")
        st.dataframe(df)
        st.image("assets/ai_tutor_scores_chart.png")
    except Exception as e:
        st.error(f"Error loading AI tutor usage data: {e}")
