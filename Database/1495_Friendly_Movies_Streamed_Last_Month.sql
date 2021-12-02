select distinct c.title
from TVProgram as t join Content as c on t.content_id = c.content_id
where c.Kids_content = 'Y' and 
      t.program_date between '2020-06-01' and '2020-06-30' and
      c.content_type = 'Movies';