select id - 1 as id, student 
from Seat
where id%2 = 0

union

select case when id !=(select max(id) from Seat) then id + 1
            else id
       end as id,
       student
from Seat
where id%2 = 1 
order by id;
