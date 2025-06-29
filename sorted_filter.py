fruits = ["banana", "apple", "cherry", "date"]

sorted_fruits = sorted(fruits)

print(sorted_fruits)

#['apple', 'banana', 'cherry', 'date']

print(fruits)
#['banana', 'apple', 'cherry', 'date']

sorted_fruits2 = sorted(fruits, reverse=True)
print(sorted_fruits2)
#['banana', 'apple', 'cherry', 'date']

def sort_by_len(element: str) -> int:
    return len(element)

sorted_fruits3 = sorted(fruits, key=sort_by_len)
print(sorted_fruits3)
#['date', 'apple', 'banana', 'cherry']


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30},
]

def sort_by_age(person: dict) -> int:
    return person["age"]

sorted_people = sorted(people, key=sort_by_age)
print(sorted_people)
#[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]

people2 = [
    {"name":"Alice", "age": 25},
    {"name":"Oscar", "age": 17},
    {"name":"Diana", "age": 30},
    {"name":"John", "age": 30},
]


def sort_by_age_name(element: dict) -> tuple[int,str]:
    return element["age"], element["name"]

sorted_people = sorted(people2, key = sort_by_age_name)
print(sorted_people)
#[{'name': 'Oscar', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Diana', 'age': 30}, {'name': 'John', 'age': 30}]


def is_even(n:int) -> bool:
    return n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9]

filtered_numbers = list(filter(is_even, numbers))
print(type(filtered_numbers))
print(filtered_numbers)

#<class 'filter'>
#[2, 4, 6, 8]


def is_adult(person: dict)-> bool:
    return person["age"]>=18

filtered_people = list(filter(is_adult, people))
print(filtered_people)

#[{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}] 