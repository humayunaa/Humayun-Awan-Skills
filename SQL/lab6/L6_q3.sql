select c.Name, count(film_id) as films
from film_category fc
join category c on fc.category_id = c.category_id
group by name
order by films desc
limit 3;

#3) Find the top three categories by highest number of films