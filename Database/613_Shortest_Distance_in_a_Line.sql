select min(p2.x - p1.x) as shortest
from Point as p1 join Point as p2
where p1.x < p2.x;
