def is_heteromecic(num, n=0):
    if n * (n + 1) < num:
        return is_heteromecic(num, n + 1)
    else:
        return n * (n + 1) == num

print(is_heteromecic(110))

# return n * (n + 1) == num, returns T or F depending
# n=0 instead of using a range as we want recursive
# learn to use n=0 more