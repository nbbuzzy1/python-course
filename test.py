#ternary operator
is_old = False
is_licensed = True

if is_old and is_licensed:
    print('you are old enough to drive')
elif is_licensed:
    print('how did you get your license??')
else:
    print('you are not old enough to drive')

print('check check')