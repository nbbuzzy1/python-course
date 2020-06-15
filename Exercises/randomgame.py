import sys
from random import randint

first = sys.argv[1]
last = sys.argv[2]

answer = randint(int(first), int(last))
user_input = None

while answer != user_input:
    user_input = int(
        input(f'Please enter a number between {first} and {last}: '))

# answer

# answer2 = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         guess = int(input('guess a number 1 to 10'))
#         if 0 < guess < 11:
#             if guess == answer2:
#                 print('you are a genius')
#                 break
#         else:
#             print('I said 1 to 10')
#     except ValueError:
#         print('please enter a number')
