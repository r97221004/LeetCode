select problem_id
from  Problems 
where ifnull(likes/(likes + dislikes)*100, 0 ) < 60
order by problem_id;