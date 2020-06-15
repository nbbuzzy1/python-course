import datetime
from array import array
from collections import Counter, defaultdict, OrderedDict
import utility
import shopping.shopping_cart

print(utility)
print(utility.divide(2, 3))

print(shopping.shopping_cart.buy('apple'))


li = [1, 2, 3, 4, 5, 6, 7, 7]
print(Counter(li))

sentence = 'blah blah blah thinking about python'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {
    'a': 1,
    'b': 2
})

print(dictionary['c'])


print(datetime.time(5, 45, 2))
print(datetime.date.today())


arr = array('i', [1, 2, 3, 4])
print(arr)
print(arr[0])
