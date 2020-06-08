# my answer
def highest_even(li):
    largest_even = 0
    for num in li:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    return largest_even


print(highest_even([10, 1, 2, 4, 8]))

# class answer


def highest_even2(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even2([10, 1, 2, 4, 8]))

for i in [1, 2]:
    hi = 'hi'


print('hi', hi)
