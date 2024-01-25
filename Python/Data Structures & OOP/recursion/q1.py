def sum_q1(num):
    if num == 1:
        return 1
    else:
        return num + sum_q1(num - 1)

print(sum_q1(6))

## if num ==1: return 1, adds 1 to final ans THEN STOPS FUNCTION
## recursion: function which calls on itself