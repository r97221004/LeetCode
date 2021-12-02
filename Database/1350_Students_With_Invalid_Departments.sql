select s.id, s.name
from Students as s left join Departments as d on s.department_id = d.id
where d.name is null;
