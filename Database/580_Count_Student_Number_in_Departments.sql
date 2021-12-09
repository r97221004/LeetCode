select d.dept_name, count(s.dept_id) as student_number
from Department as d left join Student as s on d.dept_id = s.dept_id
group by d.dept_id
order by student_number desc, d.dept_name;
