-- 方法一
update Salary
set sex = case when sex = 'm' then 'f'
         else 'm'
         end;
         
-- 方法二
update Salary
set sex = if(sex='m', 'f', 'm');

