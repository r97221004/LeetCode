select e1.employee_id 
from Employees as e1 left join Employees as e2 on e1.manager_id = e2.employee_id
where e1.salary < 30000 and e1.manager_id is not null and e2.employee_id is null
order by e1.employee_id;
