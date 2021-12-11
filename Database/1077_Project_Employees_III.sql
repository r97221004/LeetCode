with cte as (
   select p.project_id, p.employee_id, e.experience_years 
   from Project as p join Employee as e on p.employee_id = e.employee_id

)


select project_id, employee_id
from cte
where (project_id, experience_years) in

        (
            select project_id, max(experience_years) 
            from cte
            group by project_id);