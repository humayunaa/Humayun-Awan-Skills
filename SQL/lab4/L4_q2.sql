select sum(co.Population) as total
from countrylanguage cl, country co
where CountryCode = Code and cl.Language = "Spanish" and cl.IsOfficial = "T";

#2) Count the number of people in the world whose official language is Spanish. Use an inner
#(normal) join