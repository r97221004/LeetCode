select '[0-5>' as bin,
       sum(case when duration/60 < 5 then 1 else 0 end) as total
from Sessions

union

select '[5-10>' as bin,
       sum(case when duration/60>=5 and duration/60 < 10 then 1 else 0 end) as total
from Sessions

union

select '[10-15>' as bin,
       sum(case when duration/60>=10 and duration/60 < 15 then 1 else 0 end) as total
from Sessions

union

select '15 or more' as bin,
       sum(case when duration/60>= 15 then 1 else 0 end) as total
from Sessions;