select ad_id,
       round(ifnull(sum(action = 'Clicked')/(sum(action = 'Clicked') + sum(action = 'Viewed'))*100, 0), 2) as ctr
from Ads 
group by ad_id
order by ctr desc, ad_id;