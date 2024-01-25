select co.HeadOfState, count(c.Name) as cities
from city c, country co
where c.CountryCode = co.Code and GovernmentForm like "%monarch%"
group by HeadOfState
order by count(*) desc
limit 3;

#2) What monarch (of any type) is the head of state over the greatest number of cities? Return
#the top three results