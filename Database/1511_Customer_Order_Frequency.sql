select o.customer_id, c.name
from Orders as o join Product as p on o.product_id = p.product_id 
                 join Customers as c on o.customer_id = c.customer_id
group by o.customer_id
having sum(case when order_date between '2020-06-01' and '2020-06-30' then o.quantity*p.price else 0 end) >=100 and
       sum(case when order_date between '2020-07-01' and '2020-07-31' then o.quantity*p.price else 0 end) >=100;

       