select e.employee_id
from Employees as e left join Salaries as s on e.employee_id = s.employee_id
where s.employee_id is null

union 

select s.employee_id
from Salaries as s left join Employees as e on e.employee_id = s.employee_id
where e.employee_id is null

order by employee_id;