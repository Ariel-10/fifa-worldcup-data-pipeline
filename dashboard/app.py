import streamlit as st
from db.queries import load_matches
from components.metrics import render_metrics
from components.charts import render_titles_and_goals, render_wins_and_stages
from components.explorer import render_match_explorer

# page config
st.set_page_config(page_title="FIFA World Cup Dashboard", page_icon="🏆", layout="wide")

# load CSS — global styles
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# load data — cached
@st.cache_data
def load_data():
    return load_matches()

df = load_data()

# header — hero section
st.markdown("""
    <div class="hero">
        <h1>FIFA World Cup Historical Dashboard</h1>
        <p>Historical analysis of FIFA World Cups — 1930 to 2018</p>
    </div>
""", unsafe_allow_html=True)

# sections
st.divider()
render_metrics(df)

st.divider()
render_titles_and_goals(df)

st.divider()
render_wins_and_stages(df)

st.divider()
render_match_explorer(df)