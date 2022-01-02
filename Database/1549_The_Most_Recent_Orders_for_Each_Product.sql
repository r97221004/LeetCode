select p.product_name,
       p.product_id,
       o.order_id,
       o.order_date
from Products as p join Orders as o on p.product_id = o.product_id
where (p.product_id, o.order_date) in 

                (
                   select p.product_id, max(o.order_date) as maxDate
                   from Products as p join Orders as o on p.product_id = o.product_id
                   group by p.product_id 
                )
order by p.product_name, p.product_id, o.order_id;              
