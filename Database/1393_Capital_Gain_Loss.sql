select stock_name,
       sum(-(operation = "Buy")*price + (operation = "Sell")*price) as capital_gain_loss
from Stocks
group by stock_name;
