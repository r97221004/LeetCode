with cte as (
  select user_id, min(activity_date) as first
  from Traffic
  where activity = "login"
  group by user_id

)


select first as login_date,
       count(*) as user_count
from cte
where adddate(first, interval 90 day) >= "2019-06-30" 
group by first;
