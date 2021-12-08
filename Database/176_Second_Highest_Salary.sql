select
        (
            select salary
            from Employee 
            group by salary
            order by salary desc
            limit 1, 1) as SecondHighestSalary;