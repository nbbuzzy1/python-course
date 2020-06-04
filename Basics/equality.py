print(True == 1) # true
print('1' == 1) # false
print([] == 1) # false
print(10 == 10.0) # true
print([1, 2, 3] == [1, 2, 3]) # true

print(True is 1) # false
print('1' is 1) # false
print([] is 1) # false
print(10 is 10.0) # false
print([1, 2, 3] is [1, 2, 3]) # false

print(True is True) # true
print('1' is '1') # true
print([] is []) # false
print([1, 2, 3] is [1, 2, 3]) # false