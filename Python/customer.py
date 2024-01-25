class Customer():

   def __init__(self, name, number, balance=0):
        self.name = name
        self.number = number
        self.balance = balance

   def lodge(self, amount):
      self.balance = self.balance + amount

   def withdraw(self, amount):
      if amount < self.balance:
         self.balance = self.balance - amount

   def __str__(self):
      lol = f"{self.balance:.2f}"
      return "Name: {}\nNumber: {}\nBalance: {}".format(self.name, self.number, lol)
