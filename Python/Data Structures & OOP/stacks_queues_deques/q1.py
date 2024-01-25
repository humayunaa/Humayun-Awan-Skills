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
