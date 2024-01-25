select c.first_name, c.last_name, c.email, c.customer_id, a.phone, c.store_id
from customer c
join address a on a.address_id = c.customer_id
where c.store_id = 1
order by first_name asc;


#b) Using a Join statement, list the full name, email and phone number for all customers
#who have rented a movie from store 1, and order the results by first name in
#alphabetical order.
#10 Marks