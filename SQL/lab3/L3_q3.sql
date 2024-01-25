select title, film_id, rating
from film
where film_id in (select film_id from film_category
where category_id = (select category_id from category
where name = "Children"))


#3) Select the title and rating of suitable films from the ‘Children’ category using a nested query.