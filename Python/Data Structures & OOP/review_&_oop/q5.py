def histogram(list, shape):
    i = 0
    while i < len(list):
        print(list[i] * shape)
        i = i + 1
   
histogram([6, 2, 15, 3, 20, 5], "=")