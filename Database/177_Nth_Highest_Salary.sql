-- 方法一
-- 注意 limit n - 1, 1 會出錯
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set n = N - 1;
  RETURN (
              select salary
              from Employee
              group by salary
              order by salary desc
              limit n, 1 
      
  );
END

-- 方法二
-- 待補
