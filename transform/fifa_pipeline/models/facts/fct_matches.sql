with matches as (
    select * from {{ ref('stg_matches') }}
),

worldcups as (
    select * from {{ ref('stg_worldcups') }}
)

select
    m.year,
    w.host_country,
    w.champion,
    m.stage,
    m.home_team,
    m.away_team,
    m.home_score,
    m.away_score,
    m.total_goals,
    m.outcome,
    m.winning_team,
    m.losing_team,
    m.city,
    m.date,
    m.month,
    m.dayofweek
from matches m
left join worldcups w on m.year = w.year