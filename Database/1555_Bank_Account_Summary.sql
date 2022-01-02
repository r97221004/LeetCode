with cte as (
   
    select user_id, credit from Users
    
    union all
    
    select paid_by as user_id, -amount as credit from Transactions
    
    union all
    
    select paid_to as user_ud, amount as credit from Transactions

)

select u.user_id,
       u.user_name,
       sum(c.credit) as credit,
       if(sum(c.credit)<0, "Yes", "No") as credit_limit_breached
from Users as u left join cte as c on u.user_id = c.user_id
group by u.user_id;