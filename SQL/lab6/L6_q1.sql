select c.Name, c.Population, cl.Language, co.Name
from city c, country co, countrylanguage cl
where c.CountryCode = co.Code and co.Code = cl.CountryCode and cl.IsOfficial = "T" and
co.Continent = "North America" and c.ID = co.Capital
order by c.Population desc;


#WORLD
#1) For each country in North America show the name of the capital, the population of the
#capital, the name of the country and the official language(s).
#Hint: it is possible to obtain more than one row for each city