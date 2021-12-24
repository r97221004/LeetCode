with cte as (
    select c.name,
           c.customer_id,
           o.order_id,
           o.order_date,
           dense_rank() over(partition by c.customer_id order by o.order_date desc) as rnk
    from Customers as c join Orders as o on c.customer_id = o.customer_id

)

select name as customer_name,
       customer_id,
       order_id,
       order_date
from cte
where rnk <=3
order by customer_name, customer_id, order_date desc;

-- 小心名字是有可能會重複的
