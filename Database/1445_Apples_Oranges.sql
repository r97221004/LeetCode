select sale_date, 
       sum((fruit="apples")*sold_num - (fruit="oranges")*sold_num) as diff
from Sales
group by sale_date
order by sale_date;