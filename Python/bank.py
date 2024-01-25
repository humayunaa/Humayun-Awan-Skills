class Customer():

   def __init__(self, name, number, balance=0):
      self.name = name
      self.number = number
      self.balance = balance

   def __str__(self):
      lol = f"{self.balance:.2f}"
      return "Name: {}\nNumber: {}\nBalance: {}".format(self.name, self.number, lol)

def sort_on(t):
   return t.name

class Bank():

   def __init__(self):
       self.d = {}

   def add(self, other):
      self.d[other.number] = other

   def remove(self, number):
      if number in self.d:
         del self.d[number]

   def lookup(self, number):
      if number in self.d:
         return self.d[number]

   def __str__(self):
      total = 0
      for k, v in sorted(self.d.items()):
         total = total + v.balance
      slist = ["{}".format(t) for t in sorted(self.d.items())]                                                                                   1,1           All
      slist.append(v.balance)
      return "\n".join(slist)