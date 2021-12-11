-- 方法一
with cte as (
    select followee
    from Follow
    where followee in 
             (
                 select distinct follower from Follow
             )
)


select followee as follower,
       count(*) as num
from cte
group by followee
order by follower;

-- 方法二
select  f1.follower , count(distinct f2.follower) as num 
from Follow as f1  join Follow as f2  on f1.follower = f2.followee 
group by f1.follower 
order by f1.follower;
