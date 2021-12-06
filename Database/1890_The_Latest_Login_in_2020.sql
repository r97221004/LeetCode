select user_id, max(time_stamp) as last_stamp
from Logins
where date_format(time_stamp, '%Y') = '2020'
group by user_id;