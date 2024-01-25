select p.playerID, p.height, pt.points, pt.year
from players p
join players_teams pt on p.playerID = pt.playerID
where height > (select height from players
where firstName = "Alaa" and lastName = "Abdelnaby") and year = 2011
order by points desc
limit 1;

#bball
#6) Find the player who has scored the maximum points in the year 1998, having height more
#than the height of the player called Alaa Abdelnaby.
#Hint: You could use a join and two nested queries.