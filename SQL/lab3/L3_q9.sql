select sum(population) as total
from country
where Code in (select CountryCode from countrylanguage
where Language = "Spanish" and IsOfficial = "T");

#9) Count the number of people in the world whose official language is Spanish. Used a nested
#query.