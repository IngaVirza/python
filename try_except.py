def find_average(*, numbers: list) -> float: 
    return sum(numbers)/ len(numbers)

print(find_average(numbers=[1,2,3,4,5]))
#3.0

#print(find_average(numbers=[]))

# return sum(numbers)/ len(numbers)          
#ZeroDivisionError: division by zero

def find_average(*, numbers: list) -> float: 
    return sum(numbers)/ len(numbers)

try:
    find_average(numbers=[])
except ZeroDivisionError:
    print("The list is empty")    

print("we are here")
#The list is empty
#we are here


