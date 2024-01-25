def multiply(num, x):
    if x == 0:
        return 0
    elif x > 0:
        return num + multiply(num, x - 1)
    elif x < 0:
        x = -x
        return -(num + multiply(num, x - 1))


print(multiply(10, 2))
print(multiply(-51, -4))
print(multiply(3, 9))