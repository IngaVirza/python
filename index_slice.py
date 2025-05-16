fruits = ["apple", "banana", "cherry", "watermelon"]

print(fruits[0])
#apple

print(fruits[-3])
#"banana"

numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers[0:5])
#[0, 1, 2, 3, 4]
print(numbers[:5])
#[0, 1, 2, 3, 4]
print(numbers[0:10])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:len(numbers)])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:10:2])
#[0, 2, 4, 6, 8]
print(numbers[::2])
#[0, 2, 4, 6, 8]
print(numbers[::-1])
#!!![9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers.reverse)
#!!![9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
new_numbers = list(reversed(numbers))
print(type(new_numbers))
print(new_numbers)
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
string = "Hello, world"
print(string[5:])
#, world
print(string[::2])
#Hlo ol
