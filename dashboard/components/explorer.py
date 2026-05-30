import streamlit as st

# match explorer — filter by year
def render_match_explorer(df):
    st.subheader("🔍 Match Explorer")

    years = sorted(df["year"].unique(), reverse=True)
    selected_year = st.selectbox("Select a World Cup year", years)

    filtered = df[df["year"] == selected_year]

    # tournament summary — same card style as metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("🌍 Host Country", filtered["host_country"].iloc[0])
    col2.metric("🏆 Champion", filtered["champion"].iloc[0])
    col3.metric("⚽ Total Goals", int(filtered["total_goals"].sum()))

    st.markdown("<br>", unsafe_allow_html=True)

    # matches table — renamed columns
    st.dataframe(
        filtered[[
            "stage", "home_team", "home_score",
            "away_score", "away_team", "winning_team", "city"
        ]]
        .rename(columns={
            "stage": "Stage",
            "home_team": "Home Team",
            "home_score": "Home Score",
            "away_score": "Away Score",
            "away_team": "Away Team",
            "winning_team": "Winner",
            "city": "City"
        })
        .reset_index(drop=True),
        use_container_width=True,
        hide_index=True        # cleaner look
    )