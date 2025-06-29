my_set = {1,2,3,4,5}
print(type(my_set))
print(my_set)
#<class 'set'>
#{1, 2, 3, 4, 5}

for i in range(5):
    my_set.add(i)

print(my_set)
#{0, 1, 2, 3, 4, 5}

my_set.remove(2)
print(my_set)
#{0, 1, 3, 4, 5}

my_set.add(4)
print(my_set)
#{0, 1, 3, 4, 5}

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))
#{1, 2, 3, 4, 5, 6}


united_set = set1.union(set2)

print(len(united_set))
#6

print(set1.intersection(set2))
#{3, 4}
print(set1.difference(set2))
#{1, 2}

squares = {x ** 2 for x in range(10)}
print(squares)
#{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

print({1,2,3}=={3,2,1})
#True

numbers = [1,2,2,3,4,4,4,5,6,6,7]

unique_numbers = set(numbers)
print(type(unique_numbers))
print(unique_numbers)
#<class 'set'>
#{1, 2, 3, 4, 5, 6, 7}

unique_numbers = list(unique_numbers)
print(unique_numbers)
#[1, 2, 3, 4, 5, 6, 7]

unique_numbers2 = list(set(numbers))
print(unique_numbers2)
#[1, 2, 3, 4, 5, 6, 7]
print(type(unique_numbers2))
#<class 'list'>