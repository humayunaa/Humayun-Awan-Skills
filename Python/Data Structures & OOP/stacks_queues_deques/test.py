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

    
s = Stack()
s.push(6)
s.push(7)
print(s.is_empty())
print(s.top())
print(s.size())
s.pop()
print(s.size())