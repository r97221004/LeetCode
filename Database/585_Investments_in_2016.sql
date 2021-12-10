select round(sum(tiv_2016), 2) as tiv_2016
from Insurance
where pid in 

            (
                select pid
                from Insurance
                group by lat, lon
                having count(*) = 1 )
      and pid in 
      
               (
                 select distinct i1.pid
                 from Insurance as i1 join Insurance as i2 on i1.pid != i2.pid 
                                                  and i1.tiv_2015 = i2.tiv_2015            
               );