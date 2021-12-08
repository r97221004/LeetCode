select distinct l1.num as ConsecutiveNums
from Logs as l1 join Logs as l2 on l1.id + 1 = l2.id
                join Logs as l3 on l2.id + 1 = l3.id
where l1.num = l2.num and l2.num = l3.num;