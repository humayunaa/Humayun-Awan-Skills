select a.first_name, a.last_name, count(title) as movies
from actor a, film f, film_actor fa
where a.actor_id = fa.actor_id and
fa.film_id = f.film_id
group by a.actor_id
order by movies desc
limit 1;

### NOT AS A NESTED QUERY

#8) Return the count and the last name of the actor starring in the most number of films. Use a
#nested query.