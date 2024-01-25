select email, sum(amount) as total, count(payment_id) as transactions, avg(amount) as avg_spend
from customer c
join payment p on c.customer_id = p.customer_id
group by email
having total > 120 and transactions > 28 and transactions < 35 and avg_spend > 5
order by total desc;


#4) Return the email of the customers who have spent in total an amount bigger than 120 euro,
#with an average spend greater than 5 euro and a transaction count between 28 and 35 (i.e.
#29-34).