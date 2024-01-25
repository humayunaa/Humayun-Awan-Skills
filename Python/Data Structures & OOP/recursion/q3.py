def reverse(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverse(word[:-1])

print(reverse("hello"))
print(reverse("hahaha"))