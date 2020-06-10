class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
print(wizard1.sign_in())
print(wizard1.attack())

archer1 = Archer('Nick', 20)
print(archer1.attack())

print(isinstance(wizard1, Wizard))  # returns True
print(isinstance(wizard1, User))  # returns True
print(isinstance(wizard1, object))  # returns True


def player_attack(char):
    char.attack()


player_attack(wizard1)
player_attack(archer1)
