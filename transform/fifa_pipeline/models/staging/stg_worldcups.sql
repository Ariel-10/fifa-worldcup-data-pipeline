with source as (
    select * from {{ source('fifa', 'raw_worldcups') }}
)

select
    year,
    host                            as host_country,
    -- Normalize West Germany → Germany
    case
        when winner = 'West Germany' then 'Germany'
        else winner
    end                             as champion,
    second                          as runner_up,
    third                           as third_place,
    fourth                          as fourth_place,
    goals_scored,
    teams                           as qualified_teams,
    games                           as matches_played,
    attendance
from source