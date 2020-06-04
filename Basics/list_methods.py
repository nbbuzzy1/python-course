#List methods

basket = [1, 2, 3, 4, 5]

#adding
new_basket = basket.append(100)
print(new_basket) #returns none
print(basket)

#insert
basket.insert(3, 100)
print(basket)

#extend
basket.extend([50])
print(basket)

#removing
test = basket.pop()
print(test)

basket.remove(2)
print(basket)

basket.clear()
print(basket) 

modified_basket = basket[::-1]
print(modified_basket)

print(list(range(1, 100))) 

#List unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c, d)
print(*other) 