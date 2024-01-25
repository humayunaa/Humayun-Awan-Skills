"""
* n = size of input

#q1
Time Complexity = O(n)
Reason = One loop, (for loop), goes through each element in list. 
         One loop as input increases by 1 so does time essentially. Linear

#q2
Time Complexity = O(logn)
Reason = Binary search. Input grow, time grows very slowly.
         As binary search uses halfing.

#q3
Time Complexity = O(2n) --> O(n)
Reason = Two loops (for loops). Not nested.
         i.e loop1 = O(n), loop2 = O(n), 
         total (time complexity) = O(n) + O(n) = O(2n) [can drop constant "2"] = O(n)

#q4
Time Complexity = O(logn)
Reason = Binary search. i is halfing

#q5
Time Complexity = O(n^2)
Reason = Nested loops. Two loops. 1 loop = O(n). Nested means: 
         O(n) x O(n) = O(n^2)

#q6
Time Complexity = O(2^n)
Reason = Fibonacci. For each num added to the input the time doubles

"""