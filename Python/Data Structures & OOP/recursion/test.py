def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(4))

## if num == 0: return 1. times' 1 to the final ans THEN STOPS FUNCTION