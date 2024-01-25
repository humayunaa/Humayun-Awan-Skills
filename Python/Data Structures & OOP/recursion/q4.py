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


#if list1=None: list1 = []
# this resets list1 so that we can use new list1 each time. 
# but then must do reverse(list, list1) so it doesnt reset while doing recursion