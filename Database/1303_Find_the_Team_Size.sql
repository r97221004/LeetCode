with cte as (

    select team_id, count(*) as num
    from Employee
    group by team_id

)


select e.employee_id, c.num as team_size
from Employee as e join cte as c on e.team_id = c.team_id;