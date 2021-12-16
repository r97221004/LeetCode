with cte as (
    select q1.person_name,
           sum(q2.weight) as TotalWeight
    from Queue as q1 join Queue as q2 on q1.turn >= q2.turn
    group by q1.person_name

)


select person_name
from cte
where TotalWeight <= 1000
order by TotalWeight desc
limit 1;