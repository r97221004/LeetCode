with cte as (
   select *
   from Books
   where available_from < "2019-05-23"

)

-- 注意這裡要用 and 跟別忘了 ifnull
select c.book_id, c.name
from cte as c left join Orders as o on c.book_id = o.book_id
and o.dispatch_date > "2018-6-23"
group by c.book_id
having sum(ifnull(o.quantity, 0)) < 10