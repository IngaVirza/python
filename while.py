counter = 1 

while counter <= 5:
    print(f"Counter is: {counter}")
    counter +=1

#Counter is: 1
#Counter is: 2
#Counter is: 3
#Counter is: 4
#Counter is: 5    

my_list = [0,1,2]

while my_list:
    element = my_list.pop()
    print(f"element: {element}")

print(my_list)    
#element: 2
#element: 1
#element: 0
#[]

while True:
    answer = input("Enter a number:")
    if answer == 'quit':
        break
    print(f"You entered: {answer}")

#Enter a number:2
#You entered: 2
#Enter a number:quit   