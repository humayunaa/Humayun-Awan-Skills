#done
import sys

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
    def reverse(self):
        rev = []
        i = len(self.items) - 1
        while i >= 0:
            rev.append(self.items[i])
            i = i - 1

        return "".join(rev)

s = Stack()
line = "abcdef"
for each in line:
    s.push(each)

print(s.reverse())

#5.  Write a script that reads a sequence of characters and prints them in reverse order.  Use a stack.