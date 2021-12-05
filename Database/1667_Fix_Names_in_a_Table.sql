# substring(str, pos, length)，即：substring(被擷取字串，從第幾位開始擷取，擷取長度)

select user_id,
       concat(upper(substring(name, 1, 1)), lower(substring(name, 2))) as name
from Users
order by user_id;