# Built-in function

print(4, 'Inga', True)

print(dir(__builtins__))

name = input("Enter your name:")

print(name)

print(name.capitalize())

print(dir(name))


# function

def my_name(name):
    print(   name)

my_name('Igor')

def hello():
    print("Hello there!")
    print("Hi there")

hello()

def hi(name):
    print("Hello there,", name)
    print("Hi ther,", name)

hi('Inga')

def sum_nums(a, b):
    sum = a+ b
    return sum


first_sum = sum_nums(4, 8)    
print(first_sum)