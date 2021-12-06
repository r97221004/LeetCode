select p.session_id
from Playback as p left join Ads as a on p.customer_id = a.customer_id and 
              a.timestamp between p.start_time and p.end_time
where a.ad_id is null;
