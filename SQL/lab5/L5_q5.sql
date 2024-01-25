select c.customer_id, email, amount
from customer c
join payment p on c.customer_id = p.customer_id
where amount = (select max(amount) from payment)
order by customer_id asc
limit 3

#lab5
#5) Return the three customers id, and email who have made the highest payment (in a single
#order), order by customer id ascending.
#Hint: join + nested query + order by + limit