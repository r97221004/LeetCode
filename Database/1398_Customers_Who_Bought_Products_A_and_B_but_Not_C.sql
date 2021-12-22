select customer_id, customer_name
from Customers
where customer_id in 
                (
                select customer_id
                from Orders
                where product_name = 'A' or product_name = "B"
                group by customer_id
                having count(distinct product_name) = 2)
and customer_id not in 

                   (select distinct customer_id from Orders where product_name = "C")
order by customer_id;