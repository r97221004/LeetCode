with cte as (
        select distinct sub_id
        from Submissions
        where parent_id is Null
        
)

select c.sub_id as post_id,
       count(distinct s.sub_id) as number_of_comments 
from cte as c left join Submissions as s on c.sub_id = s.parent_id
group by c.sub_id;