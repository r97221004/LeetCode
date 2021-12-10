select min(round(sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2)), 2)) as shortest
from Point2D as p1 join Point2D as p2 on p1.x != p2.x or p1.y != p2.y;
