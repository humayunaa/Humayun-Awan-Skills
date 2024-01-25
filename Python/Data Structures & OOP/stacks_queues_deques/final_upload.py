##### Q1 #####
class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def reverse(self):
        if (self.is_empty()):
            return
        temp = self.items[-1]
        self.dequeue()
        self.reverse()
        self.enqueue(temp)

    def reverse_k_element(self, k):
        tmp = Queue()
        to_be_reversed = self.items[0:k]
        tmp.items = to_be_reversed
        tmp.reverse()
        tmp.items.extend(self.items[k:])
        for _ in range(self.size()):
            self.dequeue()
            self.enqueue(tmp.dequeue())
            
    def push_to_last(self, q_size):
        # pop the front element and push
        if q_size <= 0:
            return

        self.items.append(self.items.pop(0))
        self.push_to_last(q_size - 1)

    def enqueue_conditioned(self, temp, q_size):
        if self.is_empty() or q_size == 0:
            self.items.append(temp)
            return

        elif temp <= self.items[0]:
            self.items.append(temp)
            self.push_to_last(q_size)

        else:
            self.items.append(self.items.pop(0))
            self.enqueue_conditioned(temp, q_size - 1)

    def sort_queue(self):
        if self.is_empty():
            return

        temp = self.items.pop(0)
        self.sort_queue()

        self.enqueue_conditioned(temp, self.size())

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.items)
print(q.dequeue())
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.size())

##### Q2 #####
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
n = 16
def generatePrintBinary(n):
    for i in range(1, n + 1):
        str = ""
        temp = i
        # Convert decimal number to binary number
        while temp:
            if temp & 1:
                str = "1" + str
            else:
                str = "0" + str
            temp >>= 1  # Right shift the bits of temp by 1 position
        q.enqueue(str)

generatePrintBinary(16)
print(q.items)

##### Q3 #####
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

##### Q4 #####
class Queue:

    def __init__(self):
        self.items = []
        self.list1 = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def get(self):
        self.list1.append(self.items[0])
        self.items.remove(self.items[0])
    
    def lol(self):
        return self.items        

q = Queue()
line = "EAS*Y*QUE***ST***IO*N***"

list = []
for each in line:
    if each != "*":
        q.enqueue(each)
    else:
        list.append(q.dequeue())

print(list)

##### Q5 #####
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

##### Q6 #####
class Stack:
    """
    Python implementation the stack
    """

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

def evaluate_postfix(formula):
    OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
    stack = Stack()
    for ch in formula:
        if ch not in OPERATORS:
            stack.push(float(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            c = {'+': a + b, '-': a - b, '*': a * b, '/': a / b, '^': a ** b}[ch]
            stack.push(c)
    return stack.pop()


exp = "1432^*+147--+"
obj = evaluate_postfix(exp)
print("\nPostfix evaluation: %d" % obj)