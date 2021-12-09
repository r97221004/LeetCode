with cte as (

            select player_id, min(event_date) as minDate
            from Activity 
            group by player_id
)

select round(count(c.player_id)/(select count(distinct player_id) from Activity), 2) as fraction
from cte as c join Activity as a on c.player_id = a.player_id 
            and adddate(c.minDate, interval 1 day) = a.event_date;