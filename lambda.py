def sort_by_len(element: str) -> int:
    return len(element)

sort_by_len_lambda = lambda element: len(element)
print(sort_by_len("banana"))
print(sort_by_len_lambda("banana"))

#6
#6

fruits = ["banana", "apple", "cherry", "date"]

sorted_fruits = sorted(fruits, key=lambda element: len(element))
print(sorted_fruits)

#['date', 'apple', 'banana', 'cherry']

longest_word = max(fruits, key=lambda element: len(element))
print(longest_word)

#banana