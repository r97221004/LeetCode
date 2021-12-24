with cte as (

   select company_id,
          case when max(salary) < 1000 then 0
               when max(salary) >= 1000 and max(salary) <= 10000 then 0.24
               else 0.49
          end as taxes
   from Salaries
   group by company_id 

)

select s.company_id,
       s.employee_id,
       s.employee_name,
       round(s.salary*(1 - c.taxes)) as salary
from Salaries as s join cte as c on s.company_id = c.company_id;
