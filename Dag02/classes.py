class Entity:
    def Breathe(self):
        print('Entity is breathing and alive')

class Person(Entity): # Person inherits Entity
    def __init__(self, firstName, lastName): # creator
        self.firstName = firstName # attribute
        self.lastName = lastName

    def Say_Hello(self): # self is required arg
        print(f'Hello, {self.firstName} {self.lastName}, welcome back!')

    def __repr__(self):  # to-string
        return f'The created entity has {self.firstName} and {self.lastName} as values'

jakob = Person('Jakob', 'Hansen')
jakob.Breathe() # inherited member
jakob.Say_Hello()
print(jakob)