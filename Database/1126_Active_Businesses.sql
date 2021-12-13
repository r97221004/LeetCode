with cte as (
   select event_type, avg(occurences) as avgOcc
   from Events
   group by event_type

)

select e.business_id
from Events as e join cte as c on e.event_type = c.event_type
group by e.business_id
having sum(e.occurences > c.avgOcc) > 1;
