class Memories:
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

#k = name, v = "Tom"
#** means dictionary (i think)

person1 = Memories(name="Tom", age=32)

#setattr(person1, "email", "tom@gmail.com")
#same thing
#print(person1.name)
#print(getattr(person1, "name"))