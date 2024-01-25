select coachID, sum(won) AS wins, sum(lost) AS losses
from coaches
group by coachID
having wins > 900 
order by losses asc

#5) Find all the basketball coach IDs with more than 900 of wins, order by ascending number of
#losses (Hint: Group By required)