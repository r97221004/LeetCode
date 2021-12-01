with cte as (

    select st.student_id, st.student_name, su.subject_name
    from Students as st join Subjects as su
)


select  c.student_id,
        c.student_name,
        c.subject_name,
        count(e.subject_name) as attended_exams
from cte as c left join Examinations as e on c.student_id = e.student_id and c.subject_name = e.subject_name
group by c.student_id, c.subject_name
order by c.student_id, c.subject_name ;