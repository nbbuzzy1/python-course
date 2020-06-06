# 0's should be spaces and 1's should be *'s

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],  
]

for image in picture:
    line = ''
    for pixel in image:
        if pixel:
            line += '*'
        else:
            line += ' '
    print(line)

for row in picture:
    for pixel in row:
        if pixel:
            print('*', end='')
        else:
            print(' ', end='')
    print('')