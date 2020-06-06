# while loops

i = 0

while i < 50:
    print(i)
    i += 1
else:
    print('done with all the work')

i = 0
my_list = [1, 2, 3]

while i < len(my_list):
    print(i)
    i += 1

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break

for item in my_list:
    pass
