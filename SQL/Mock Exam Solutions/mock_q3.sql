select Name, Population
from city
where Name like "%re%" and CountryCode in (select Code from country
where Continent = "Asia")
order by Population desc;

#world
#a) Using a nested query, list the name and population of all cites in Asia with “re’” in their
#name, and order the results by population from highest to lowest.
#15 Marks