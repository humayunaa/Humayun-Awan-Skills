SELECT pt.points, p.lastName, pt.year
FROM players_teams pt, players p
WHERE pt.playerID = p.playerID and p.lastName LIKE '%ire%' and year = 1998
and points > (select avg(points) from players_teams where year = 1998);

#basketball
#4) Return the points and last name of the player containing ‘ire’ who scored higher points than the
#average in 1998. Use a nested query.