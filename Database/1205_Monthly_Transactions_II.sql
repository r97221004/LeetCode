with cte as (

select * from Transactions

union all
    
select c.trans_id as id,
       t.country,
       "chargebacked" as stat,
       t.amount,
       c.trans_date
from Chargebacks as c join Transactions as t on c.trans_id = t.id 

)

select date_format(trans_date, '%Y-%m') as month,
       country,
       sum(state = "approved") as approved_count,
       sum((state = "approved")*amount) as approved_amount,
       sum(state = "chargebacked") as chargeback_count,
       sum((state = "chargebacked")*amount) as chargeback_amount 
from cte
group by date_format(trans_date, '%Y-%m'), country
having approved_count != 0 or
       approved_amount != 0 or
       chargeback_count != 0 or
       chargeback_amount!= 0 ;