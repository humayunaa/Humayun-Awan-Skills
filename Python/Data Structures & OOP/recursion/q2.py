# Q2
def reverse_integer(n):
    if n == 0:
        return ""
    else:
        return str(n % 10) + str(reverse_integer(n // 10))

print(reverse_integer(123))
print(reverse_integer(456))