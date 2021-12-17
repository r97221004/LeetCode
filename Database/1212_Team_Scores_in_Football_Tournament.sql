with cte as (
    
    select host_team as id,
           case when host_goals > guest_goals then 3
                when host_goals = guest_goals then 1
           else 0
           end as points
    from Matches
    
    union all
    
    select guest_team as id,
           case when host_goals < guest_goals then 3
                when host_goals = guest_goals then 1
           else 0
           end as points
    from Matches

)


select t.team_id as team_id,
       t.team_name,
       ifnull(sum(c.points), 0) as num_points
from Teams as t left join cte as c on t.team_id = c.id
group by t.team_id
order by num_points desc, t.team_id asc;