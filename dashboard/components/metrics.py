import streamlit as st

# kpi cards — top of dashboard
def render_metrics(df):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("World Cups", df["year"].nunique())
    col2.metric("Matches", len(df))
    col3.metric("Total Goals", int(df["total_goals"].sum()))
    col4.metric("Unique Champions", df["champion"].nunique())