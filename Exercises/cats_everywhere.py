# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('Summer', 133)
cat2 = Cat('Thome', 20)
cat3 = Cat('Reagan', 4)

# 2 Create a function that finds the oldest cat

cats = (cat1, cat2, cat3)


def find_oldest_cat(cats):
    age = 0
    oldest_cat = None

    for cat in cats:
        if cat.age > age:
            oldest_cat = cat
            age = oldest_cat.age
    return oldest_cat


oldest_cat = find_oldest_cat(cats)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {oldest_cat.age} years old.')

# ANSWER

# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")
