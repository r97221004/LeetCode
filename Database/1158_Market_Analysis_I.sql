select u.user_id as buyer_id,
       u.join_date,
       count(o.order_id) as orders_in_2019
from Users as u left join Orders as o on u.user_id = o.buyer_id and date_format(o.order_date, "%Y") = "2019"
group by u.user_id, u.join_date;