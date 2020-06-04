# Set

your_set = {4, 5, 6, 7, 8, 9}
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(10)
print(my_set)

new_set = my_set.copy()
print(new_set)

my_list = [1, 2, 3, 4, 4, 5]
print(set(my_list))

# difference
my_set.difference(your_set)

# discard
my_set.discard(5)

# difference_update
my_set.difference_update(your_set)
print(my_set)

# intersection
my_set.intersection(your_set)

# isdisjoint
my_set.isdisjoint(your_set)

# issubset
my_set.issubset(your_set)

# issuperset
my_set.issuperset(your_set)

# union
my_set.union(your_set) 