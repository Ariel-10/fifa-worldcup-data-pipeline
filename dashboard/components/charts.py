import streamlit as st
import plotly.express as px

# transparent background — consistent dark theme
LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#ffffff",
    autosize=True,
    margin=dict(l=10, r=10, t=40, b=10) # tight margins - better fit
)


# brand palette — consistent in all charts
PALETTE = [
    "#1b4338", "#1b4332", "#2d6a4f", "#40916c",
    "#52b788", "#74c69d", "#95d5b2", "#b7e4c7",
    "#d8f3dc", "#1a472a", "#2d6a4f", "#3a7d5e",
    "#4a9b75", "#5cb88a", "#6fd4a0", "#82e8b5",
    "#95d5b2", "#a8f0cc"
]

# charts row 1 — titles per country + goals per tournament
def render_titles_and_goals(df):
    col_left, col_right = st.columns(2)

    with col_left:
        # bar chart — titles per country
        st.subheader("🏆 Titles by Country")
        champions = (
            df.drop_duplicates(subset="year")[["year", "champion"]]
            .groupby("champion")
            .count()
            .reset_index()
            .rename(columns={"year": "titles"})
            .sort_values("titles", ascending=True)
        )
        fig1 = px.bar(
            champions,
            x="titles",
            y="champion",
            orientation="h",        # horizontal bars
            color="titles",
            color_continuous_scale=PALETTE,
            labels={"titles": "Titles", "champion": "Country"}
        )
        fig1.update_layout(**LAYOUT, showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig1, use_container_width=True)

    with col_right:
        # line chart — total goals per tournament
        st.subheader("🥅 Goals per World Cup")
        goals_per_year = (
            df.groupby("year")["total_goals"]
            .sum()
            .reset_index()
            .rename(columns={"total_goals": "goals"})
        )
        fig2 = px.line(
            goals_per_year,
            x="year",
            y="goals",
            markers=True,           # dots on each year
            labels={"year": "Year", "goals": "Total Goals"},
            color_discrete_sequence=["#2ecc71"]
        )
        fig2.update_layout(**LAYOUT)
        st.plotly_chart(fig2, use_container_width=True)

# charts row 2 — top 10 wins + matches per stage
def render_wins_and_stages(df):
    col_left2, col_right2 = st.columns(2)

    with col_left2:
        # bar chart — top 10 teams by wins
        st.subheader("🥇 Top 10 Teams by Wins")
        top_teams = (
            df[df["winning_team"].notna() & (df["winning_team"] != "Draw")]
            .groupby("winning_team")
            .size()
            .reset_index(name="wins")
            .sort_values("wins", ascending=False)
            .head(10)
        )
        fig3 = px.bar(
            top_teams,
            x="winning_team",
            y="wins",
            color="wins",
            color_continuous_scale=PALETTE,
            labels={"winning_team": "Team", "wins": "Wins"}
        )
        fig3.update_layout(**LAYOUT, coloraxis_showscale=False)
        st.plotly_chart(fig3, use_container_width=True)

    with col_right2:
        # pie chart — matches per stage
        st.subheader("📊 Matches by Stage")
        stages = (
            df.groupby("stage")
            .size()
            .reset_index(name="matches")
            .sort_values("matches", ascending=False)
        )
        fig4 = px.pie(
            stages,
            names="stage",
            values="matches",
            hole=0.4,               # donut style
            color_discrete_sequence=PALETTE
        )
        fig4.update_layout(**LAYOUT)
        st.plotly_chart(fig4, use_container_width=True)