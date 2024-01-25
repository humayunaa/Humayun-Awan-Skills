select c.coachID, award, c.year, won
from coaches c, awards_coaches ac
where c.coachID = ac.coachID and ac.year = 1995 and c.year = 1995 and award = "NBA Coach of the Year"




#5) Find the NBA Coach of the Year IN 1995 and the number of games won.