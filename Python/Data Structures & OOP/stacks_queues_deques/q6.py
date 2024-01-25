# Q6: this is a solution for single digit formula

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