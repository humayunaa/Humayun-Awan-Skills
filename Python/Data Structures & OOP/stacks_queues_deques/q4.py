#done
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



#4. A letter means put and an asterisk means get in the following sequence.
#Write a script to show the sequence of values returned by the get operation
#when this sequence of operations is performed on an initially empty FIFO queue.

#'EAS*Y*QUE***ST***IO*N***' ➞ ['E', 'A', 'S', 'Y', 'Q', 'U', 'E', 'S', 'T', 'I', 'O', 'N']