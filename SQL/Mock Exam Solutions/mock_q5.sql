select c.Name, count(Language) as languages
from country c
join countrylanguage cl on c.Code = cl.CountryCode
where Code in (select CountryCode from city
where Population >= 8000000)
group by c.Name
order by languages;

#c) Using a nested select query expression:
#Find all countries that have a city with over 8 million people and from those countries, find
#the number of languages spoken in each and order the results by the number of languages
#spoken.
#25 Marks