-- 可以藉由這題了解 條件寫在 where 與 on 的差別
select s.seller_name as seller_name
from Seller as s left join Orders as o on s.seller_id = o.seller_id
     and sale_date between "2020-01-01" and "2020-12-31" 

where o.order_id is null
order by s.seller_name;