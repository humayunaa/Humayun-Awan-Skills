select t.name, c.coachID, t.won, t.year, t.tmID
from teams t
join coaches c on t.tmID = c.tmID and t.year = c.year
where t.year = 2000 and t.won > (select max(won) from coaches
where year = 1950)
order by t.name asc
limit 3;

#b) Return the ID and name of the team who in the year 2000 have won a higher number of
#games than the max number of games won by any coach in the year 1950. Order the result
#in ascending order for the team and show only the first three results.
#Hint: join and a nested query for selecting the max number of games won by a coach in the year
#1950. Note that the year in coaches and the year in teams must be the same.
#15 marks