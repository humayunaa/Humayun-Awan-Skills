def q1_sum(list):
    even = []
    for each in list:
        i = 0
        for num in each:
            if num % 2 == 0 and str(num).isnumeric():
                even.append(num)
            i = i + 1
    return sum(even)

print(q1_sum([[1, 0, 2],
        [5, 5, 7],
        [9, 4, 3]]))