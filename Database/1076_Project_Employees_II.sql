select project_id
from Project
group by project_id
having count(*) =

                (
                    select count(*)
                    from Project
                    group by project_id
                    order by count(*) desc
                    limit 1);