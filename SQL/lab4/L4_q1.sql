select max(c.Population), min(c.Population)
from city c, country co
where CountryCode = Code and co.Name = "Italy";

#sakila
#1) Find the average, the min and the max value of the population of the Italian cities. Use a join
#operation.