with cte as (
     
     select log_id,
            log_id - dense_rank() over(order by log_id) as rnk
     from Logs
     
)

select min(log_id) as start_id,
       max(log_id) as end_id
from cte
group by rnk
order by start_id;