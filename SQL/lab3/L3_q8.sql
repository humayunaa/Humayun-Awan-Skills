SELECT Continent, Count(*), avg(LifeExpectancy)
FROM country
where continent in (select continent from country
group by continent
having avg(LifeExpectancy) > 45)
group by Continent
having avg(LifeExpectancy) > 45;


#8) Return the count and average life expectancy of the countries grouped by continent of origin
#with an average life expectancy greater than 45 years. Use a nested query