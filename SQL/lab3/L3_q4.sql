SELECT year, avg(won) AS awon
FROM teams
group by year
having awon > 40;

#4) Return the year and the average wins of the NBA teams from the 1990 only when this
#average is greater than 40 Hint: Group By required