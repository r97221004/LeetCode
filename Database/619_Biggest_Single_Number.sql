select max(num) as num
from 
  (
    select num
    from Mynumbers
    group by num
    having count(*) = 1 ) as tab;