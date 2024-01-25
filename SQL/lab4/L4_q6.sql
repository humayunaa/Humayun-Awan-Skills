select *
from actor
where actor_id in (select actor_id from film_actor
where film_id in (select film_id from film
where title like "%pirates%"));

## or

select *
from actor a, film f, film_actor fa
where a.actor_id = fa.actor_id and
f.film_id = fa.film_id and
title like "%pirate%";

#6) Return the actors’ full name in any movie containing the word ‘pirates’ in the title