select f.title, f.film_id, fc.category_id, c.name as category, f.rating
from film f, film_category fc, category c
where f.film_id = fc.film_id and c.category_id = fc.category_id and
c.name = "Action" and f.title like "%Amadeus%";

#V2 BELOW
#4) Among the Action films, return the one containing the word ‘Amadeus’ in the title.
#Hint: You need more than one join.

#v2
#SELECT f.title, f.film_id
#FROM film f
#JOIN film_category fc ON f.film_id = fc.film_id
#JOIN category c ON fc.category_id = c.category_id
#WHERE c.name = 'Action'
#AND f.title LIKE '%Amadeus%';

#v2 using JOIN INSTEAD OF WHERE  __ = __