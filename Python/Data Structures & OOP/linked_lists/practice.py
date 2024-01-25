class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

## node is subclass of linked list. wont interact with it

class linked_list:
    def __init__(self):
        self.head = node()   # point to first element in list

    def append(self, data):
        new_node  = node(data)   # store new node
        cur = self.head   # store current node
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

my_list = linked_list()
my_list.display()

my_list.append(1)
my_list.append(2)

my_list.display()