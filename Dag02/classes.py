class Entity:
    def Breathe(self):
        print('Entity is breathing and alive')

class Person(Entity): # Person inherits Entity
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def Say_Hello(self):
        print(f'Hello, {self.firstName} {self.lastName}, welcome back!')

jakob = Person('Jakob', 'Hansen')
jakob.Breathe() # inherited member
jakob.Say_Hello()