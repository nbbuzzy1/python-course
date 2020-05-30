#List methods

basket = [1, 2, 3, 4, 5]

#adding
new_basket = basket.append(100)
print(new_basket)
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