class Memories:
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def remember(self, other):
        if hasattr(self, other):
            return getattr(self, other)
        else:
            return False

person1 = Memories(name="Tom", age=32, salary=50000)
print(person1.remember("salary"))
print(person1.remember("email"))
print(person1.remember("name"))