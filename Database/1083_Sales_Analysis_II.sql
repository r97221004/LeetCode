select distinct s.buyer_id
from Sales as s join  Product as p on s.product_id = p.product_id
where p.product_name = 'S8' and s.buyer_id not in 

                        (
                        select s.buyer_id
                        from Sales as s join  Product as p on s.product_id = p.product_id
                        where p.product_name = 'iPhone');