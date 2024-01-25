select email, c.customer_id, sum(amount) as total
from customer c, payment p
where c.customer_id = p.customer_id
group by c.customer_id
having total > 220


#7) Return the email of the customer who has spent in total more than 220 euro.