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


#2. Write a function using the queue data structure to generate a sequence of binary numbers from 1 to n. 

#Example:
#Given n=16 the binary sequence is: 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000