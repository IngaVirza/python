file_names = ["document.txt", "image1.jpg", "document2.txt", "image2.jpg"]

for file_name in file_names:
    print(file_name)

#document.txt
#image1.jpg
#document2.txt
#image2.jpg    

greeting = "Hello, world"
for char in greeting:
    print(char)

#H
#e
#l
#l
#o
#,
# 
#w
#o
#r
#l
#d    
greeting1 = "Hello, world"
count_0 = 0
for char in greeting1:
    if char == "o":
        #count_0 = count_0 + 1
         count_0 += 1
    print(char)
print(count_0)    
#2

students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
    print(student)
    for char in student:
        print(char)

#Alice
#A
#l
#i
#c
#e
#Bob
#B
#o
#b
#Charlie
#C
#h
#a
#r
#l
#i
#e
#David
#D
#a
#v
#i
#d        

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for num in numbers:
    if num %2 == 0:
        continue
    print(num)

# 1
#3
#5
#7
#9
#11
#13
#15       

for num in numbers: 
    if num == 10: 
        break
    print(num)

#1
#2
#3
#4
#5
#6
#7
#8
#9    

range_object = range(10)
print(range_object)
#range(0, 10)
numbers_list = list(range_object)
print(numbers_list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(1,10,2)
print(list(my_range))
#[1, 3, 5, 7, 9]

my_range1 = range(10,1,-1)
print(list(my_range1))
#[10, 9, 8, 7, 6, 5, 4, 3, 2]

numbers_idx = [10,11,12,13,14,15]
for i in range(len(numbers_idx)):
    numbers_idx[i] +=1
print(numbers_idx)    
#[11, 12, 13, 14, 15, 16]

greeting4 = "Hello, world"

indexes= []
count = 0

for i in range(len(greeting)):
    if greeting[i] == "o":
        count +=1
        indexes.append(i)

print(count)
print(indexes)  
#2
#[4, 8]      