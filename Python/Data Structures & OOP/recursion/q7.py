def length(s):
    if s:
        return length(s[:-1]) + 1
    else:
        return 0

print(length("hello!"))
