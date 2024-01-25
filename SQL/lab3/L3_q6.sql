SELECT playerID, tmID, minutes
from players_teams
where year = 1998 and minutes > 1200 and tmID in (select tmID from teams
where name like "%Miami%")


#6) Print the players of the Miami 1998 team with over 1200 minutes played. Use a nested
#query in your answer.