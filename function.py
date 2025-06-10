numbers_1 = [1,2,3,4,5]
average_1 = sum(numbers_1)/len(numbers_1)
print(average_1)

#3.0

numbers_2 = [6,7,8,9,10]
average_2 = sum(numbers_2)/len(numbers_2)
print(average_2)
#8.0

# Princip DRY (don't repeat yourself)

numbers_3 = [6,7,8,9,10]
numbers_4 = [10,11,12,13,14]

def find_avarage(numbers):
    average = sum(numbers)/len(numbers)
    return average

average_3 = find_avarage(numbers_3)
average_4 = find_avarage(numbers_4)
print(average_3, average_4)

#8.0 12.0

def count_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in VOWELS:
            count += 1

    return count         
print(count_vowels("Hello, world"))
print(count_vowels("Python is a very powerful language"))

# 3
#11

# function zaglushka
def nothing():
    pass
nothing()

# * -> explicit meaning
def format_date(*, day: int, month:str)->str:
    return f"The date is {day} of {month}"

print(format_date(day=4,month="April"))
print(format_date(month="April",day=4))
#The date is 4 of April
#The date is 4 of April

def custom_greeting(*, name:str, greeting: str ="Hello")-> str:
    return f"{greeting}, {name}"

print(custom_greeting(name="John", greeting="good morning"))
print(custom_greeting(name="John"))

#good morning, John
#Hello, John