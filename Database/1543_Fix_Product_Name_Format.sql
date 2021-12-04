with cte as (

     select trim(lower(product_name)) as product_name, date_format(sale_date, '%Y-%m') as sale_date from Sales
)


select product_name, sale_date, count(*) as total
from cte
group by product_name, sale_date
order by product_name, sale_date;