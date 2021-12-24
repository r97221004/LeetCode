with cte as (
   select caller_id as id, duration from Calls
   
   union all
    
   select callee_id as id, duration from Calls
)


select c1.name as country
from Country as c1 left join Person as p on c1.country_code = substring(p.phone_number, 1, 3)
                        join cte as c2 on p.id = c2.id
group by c1.name
having avg(c2.duration) > (select avg(duration) from cte);