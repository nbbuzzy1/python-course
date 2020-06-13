while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter numbers {err}')


print(sum('1', 2))

while True:
    try:
        age = int(input('what is your age? '))
        10/age
        raise Exception('hey cut it out')
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you')
    finally:
        print('ok, I am finally done')
    print('can you hear me?')