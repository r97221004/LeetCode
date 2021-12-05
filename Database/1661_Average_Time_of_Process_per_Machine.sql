with cte  as (

    select machine_id, 
           process_id,
           sum(case when activity_type = "start" then -timestamp else timestamp end) as total                         from Activity
    group by machine_id, process_id

)

select machine_id, round(avg(total), 3) as processing_time
from cte
group by machine_id;