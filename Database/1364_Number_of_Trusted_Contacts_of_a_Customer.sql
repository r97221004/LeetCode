select i.invoice_id,
       c1.customer_name,
       i.price,
       count(c2.contact_name) as  contacts_cnt,
       sum(case when c2.contact_name in (select customer_name from Customers) then 1 else 0 end) as trusted_contacts_cnt
from Invoices as i join Customers as c1 on i.user_id = c1.customer_id
                   left join  Contacts as c2 on i.user_id = c2.user_id
group by i.invoice_id
order by i.invoice_id;