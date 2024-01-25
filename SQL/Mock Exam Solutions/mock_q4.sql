select Language, sum((Population * (Percentage / 100))) as population, count(c.Name) as countries
from country c
join countrylanguage cl on c.Code = cl.CountryCode
group by Language
order by population desc
limit 10;


#b) List the top 10 most used languages, the number of countries which speak the language
#and total amount of people who speak this language (not the percent). Order the results
#by the total number of people who speak these languages from highest to lowest.
#20 marks