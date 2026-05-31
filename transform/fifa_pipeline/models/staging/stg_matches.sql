with source as (
    select * from {{ source('fifa', 'raw_matches') }}
)

select
    year,
    country                         as host_country,
    city,
    stage,
    home_team,
    away_team,
    home_score,
    away_score,
    home_score + away_score         as total_goals,
    outcome,
    win_conditions,
    -- Normalize draws (NaN) + West Germany → Germany
    case
        when outcome = 'D' then 'Draw'
        when winning_team = 'West Germany' then 'Germany'
        else winning_team
    end as winning_team,
    losing_team,
    date,
    month,
    dayofweek
from source
where home_score is not null
  and away_score is not null