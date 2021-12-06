select distinct c2.user_id
from Confirmations as c1 join Confirmations as c2 on c1.user_id = c2.user_id and c1.time_stamp < c2.time_stamp
where adddate(c1.time_stamp, interval 1 day) >= c2.time_stamp;