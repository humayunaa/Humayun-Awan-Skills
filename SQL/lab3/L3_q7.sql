select (select Name from country where Code = CountryCode) AS Country, count(*) AS cities
from city
where CountryCode in (select Code from country
where continent = "Europe" and Population > 90000000)
group by Country;

#7) Count how many cities are located in a European country with more than 90 million
#inhabitants? (Hint: Group By required)