select ac.ID, ac.coachID, ac.award, ac.year, c.won
from awards_coaches ac
join coaches c on ac.coachID = c.coachID and ac.year = c.year
where ac.year = 2000 and award = "NBA Coach of the Year";


#basketball
#a) Select the ID and the number of the coach who was awarded ‘NBA Coach of the Year’ in
#2000. Hint: the year in coaches and the year in awards_coaches must be the same.
#10 Marks