select c.Name, c.Population, co.Name
from city c, country co
where c.CountryCode = co.Code and co.Name = "Italy"
order by c.Population desc
limit 3

#WORLD
#1) Return the three Italian cities with the highest population.
#(Hint: There are different ways to obtain this result, try in this way: join -> order by
#population -> limit the results to the first three cities. Use the column name = ‘Italy’ in the
#table Country for the join operation instead directly countryCode = ‘ITA’ in the table City.)
