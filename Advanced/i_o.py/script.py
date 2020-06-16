my_file = open('test.txt')
print(my_file)

print(my_file.readlines())

with open('test.txt', 'w') as my_file:
    text = my_file.write('hey it is me!')
    print(text)

with open('test.txt', 'a') as my_file:
    text = my_file.write('hey it is me!')
    print(text)

with open('sad.txt', 'w') as my_file:
    text = my_file.write('sad!')
    print(text)


try:
    with open('Advanced/shopping/oop.py') as my_file2:
        print(my_file2)
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('file does not exist')
    raise err
