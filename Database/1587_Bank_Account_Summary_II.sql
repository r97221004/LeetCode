select u.name, sum(amount) as balance
from Transactions as t join Users as u on t.account = u.account
group by t.account
having sum(amount) > 10000;
