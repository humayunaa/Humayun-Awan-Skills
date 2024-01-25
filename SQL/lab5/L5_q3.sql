select count(*)
from payment
where amount >= (select (max(amount) - min(amount)) as differnece from payment);

#sakila
#3) Count the number of payment greater than or equal to the difference between the
#maximum payment and the minimum. Use a nested query.