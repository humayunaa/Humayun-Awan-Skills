#q1
def sum_q1(num):
    if num == 1:
        return 1
    else:
        return num + sum_q1(num - 1)

print(sum_q1(6))

#q2
def reverse_integer(n):
    if n == 0:
        return ""
    else:
        return str(n % 10) + str(reverse_integer(n // 10))

print(reverse_integer(123))
print(reverse_integer(456))

#q3
def reverse(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverse(word[:-1])

print(reverse("hello"))
print(reverse("hahaha"))

#q4
########## 1st way

def reverse(list):
    if len(list) == 0:
        return []
    else:
        return [list.pop()] + reverse(list)

print(reverse([1, 2, 3, 4]))

############ 2nd way
"""
def reverse(list=[], list1=None):
    if list1 == None:
        list1 = []

    if len(list) == 0:
        return
    else:
        list1.append(list.pop())
        reverse(list, list1)
        return list1

print(reverse([1, 2, 3, 4]))
print(reverse([5, 6]))
"""
### putting [] around a number example [4] just makes it a list with 1 element (i.e 4)
### then we can add it to another ([4] + [3] + [2] + [1] to get [4, 3, 2, 1])


#q5
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

#q6 **
def is_heteromecic(num, n=0):
    if n * (n + 1) < num:
        return is_heteromecic(num, n + 1)
    else:
        return n * (n + 1) == num

print(is_heteromecic(110))

#q7 ****
def length(s):
    if s:
        return length(s[:-1]) + 1
    else:
        return 0

print(length("hello!"))