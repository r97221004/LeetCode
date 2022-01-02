with cte as (
  
     select customer_id,
            product_id,
            count(*) as cnt
     from Orders
     group by customer_id, product_id
    
)


select o.customer_id,
       o.product_id,
       p.product_name
from Orders as o join Products as p on o.product_id = p.product_id
group by o.customer_id, o.product_id
having (o.customer_id, count(*)) in 

              (select customer_id, max(cnt) from cte group by customer_id);
