select title, description, length
from film
where length > 119 and description like "%wrestler%" and title like "%agent%";



#sakila
#Return the title and the description of the movie having length of at least 2 hours and
#containing the word ‘wrestler’ in the description and ‘agent’ in the title 