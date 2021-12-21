with cte as (

  select activity, count(*) as total
  from Friends
  group by activity

)


select activity
from cte
where total !=  (select max(total) from cte ) and 
      total != (select min(total) from cte);