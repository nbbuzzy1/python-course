# OOP

class BigObject:
    pass


obj1 = BigObject()
obj2 = BigObject()
obj3 = BigObject()

print(type(5))  # an example that everything is an object in Python

print(obj1)


class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name='Nick', age=0):
        if(self.membership):  # or PlayerCharacter.membership
            self.name = name
            self.age = age

        if(age > 18):
            self.name = name
            self.age = age

    def shout(self, hello):
        print(f'{hello} my name is {self.name}')
        return('done')

    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2

    @classmethod
    def adding_things2(cls, num1, num2):
        return cls('John', num1 + num2)


player1 = PlayerCharacter('nick', 33)
print(player1.shout('Hello'))
print(player1.name)

print(player1.membership)

print(PlayerCharacter.adding_things(1, 2))
player3 = PlayerCharacter.adding_things2(20, 2)
print(player3.age)
