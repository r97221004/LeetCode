select c.country_name,
       case when avg(w.weather_state) <= 15 then 'Cold'
            when avg(w.weather_state) >= 25 then 'Hot'
            else 'Warm'
            end as weather_type 
from Weather as w join Countries as c on w.country_id = c.country_id
where w.day between "2019-11-1" and '2019-11-30'
group by c.country_name;
