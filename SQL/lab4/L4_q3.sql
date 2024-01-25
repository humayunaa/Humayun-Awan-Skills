select Name, Population, (select Name from country where country.Code = city.CountryCode) AS country,
(select Region from country where Country.Code = city.CountryCode) AS region
from city
order by Population desc limit 1


#3) Find the city with the highest population and where it is located (country, region). Use nested
#queries.