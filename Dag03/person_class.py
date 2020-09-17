"https://medium.com/python-features/pythons-instance-class-and-static-methods-e9097f07829b"

class Person:
    def __init__ (self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def __repr__ (self):
        return f'{self.lastName}, {self.firstName}'

    def methodOnInstance(self):
        return f'This method operates on the instance - {self.firstName} {self.lastName}'

    @classmethod
    def classMethod(cls):
        return 'This method operates on the class, not on the instance', cls
    
    @staticmethod
    def Personfactory():
        print('This method does not rely on the containing class')
        return Person('Always', 'TheSame')

p = Person('Ernst', 'Hjulben')
print(p.methodOnInstance())

p2 = Person.classMethod()
print(p2)

p3 = Person.Personfactory()
print(p3)

p4 = Person.Personfactory()
print(p4)

