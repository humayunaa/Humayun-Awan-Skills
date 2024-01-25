#done
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
        return self.items[-1]
    
    def size(self):
        return len(self.items)


line = "EAS*Y*QUE***ST***IO*N***"
s = Stack()

pops = []
for each in line:
    if each != "*":
        s.push(each)
    else:
        pops.append(s.pop())

print(pops)


#3.  A letter means push and an asterisk means pop in the following sequence.
#Write a script to show the sequence of values returned by the pop 
#operations when this sequence of operations is performed on an initially empty LIFO stack.


#'EAS*Y*QUE***ST***IO*N***' ➞ ['S', 'Y', 'E', 'U', 'Q', 'T', 'S', 'A', 'O', 'N', 'I', 'E']