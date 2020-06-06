# Functions

def say_hello(name='Darth Vader', emoji='😒'): #these are parameters
    print(f'hello {name} {emoji}')

say_hello('Nick', '😊') #these are arguments
say_hello('Christina', '😊')

say_hello(emoji='😊', name='Nick') #keyword arguments

say_hello() #the above default parameters will provide the values

#using return
def sum(num1, num2):
    return num1 + num2

total = sum(2, 4)
print(total)

#nested functions
def sum2(num1, num2):
    def another_function(num1, num2):
        return num1 + num2
    return another_function(num1, num2)

total2 = sum2(10, 20)
print(total2) #returns 30