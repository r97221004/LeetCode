select w.name as warehouse_name,
       sum(w.units*p.Width*p.Length*p.Height) as volume
from Warehouse as w join Products as p on w.product_id = p.product_id
group by w.name;
