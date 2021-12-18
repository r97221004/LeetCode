with cte as (

  select visited_on, sum(amount) as amount
  from Customer
  group by visited_on
)


select c1.visited_on,
       sum(c2.amount) as amount,
       round(sum(c2.amount)/7, 2) as average_amount
from Cte as c1 join Cte as c2 on 0 <= datediff(c1.visited_on, c2.visited_on) 
                                             and datediff(c1.visited_on, c2.visited_on) <=6
group by c1.visited_on
having count(*) >= 7
order by c1.visited_on;
