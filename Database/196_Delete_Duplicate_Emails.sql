-- 方法一
delete p1
from Person as p1 join Person as p2 on p1.email = p2.email
where p1.id > p2.id;

-- 方法二
delete from Person
where Id not in 
                   ( select Id  
                     from 
                               (
                                select min(Id) as Id
                                from Person
                                group by Email
                                ) as tab  ) ;
