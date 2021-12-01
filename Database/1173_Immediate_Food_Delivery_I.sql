select round(ifnull(count(*)/(select count(*) from Delivery), 0)*100, 2) as immediate_percentage
from Delivery
where order_date = customer_pref_delivery_date;