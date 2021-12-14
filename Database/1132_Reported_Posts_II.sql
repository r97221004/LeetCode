with cte as (

   select distinct post_id, action_date, action, extra
   from Actions 
   where action = 'report' and extra = 'spam'

)

select round(avg(Aver)*100 ,2) as  average_daily_percent
from

(
    
    select c.action_date,
           sum(r.post_id is not null)/count(*) as Aver
    from cte as c left join Removals as r on c.post_id = r.post_id
    group by c.action_date) as tab;