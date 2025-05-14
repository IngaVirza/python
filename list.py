fruits =["apple", "banana", "cherry"]
print(fruits)
#["apple", "banana", "cherry"]
print(len(fruits))
#3

print("banana" in fruits)
#true
element1 ="apple"
element2 ="banana"
element3 ="cherry"
fruits1 = [element1,element2,element3]
print(fruits1)
#["apple", "banana", "cherry"]

fruits1.append("watermelon")
print(fruits1)
#["apple", "banana", "cherry", "watermelon"]
my_list = list()
print(my_list)
#[]

my_list1 =[1,2,3]
my_list2 = [1,3,2]
print(my_list1==my_list2)
#False

print(bool([]))
#false
print(bool([0]))
#true

word = "hello"
my_list = list(word)
print(my_list)
#['h', 'e', 'l', 'l', 'o']

my_list_1 = [1,2,3]
my_list_2 =[4,5,6]
my_list_3 =my_list_1+my_list_2
print(my_list_3)
#[1,2,3,4,5,6]

fruits3 = ["watermelon", "apple", "cherry"]
fruit = fruits3.pop()
print(fruit)
#cherry
print(fruits3)
#["watermelon", "apple"]


fruits4 =["grape", "lemon", ]
fruits3.extend(fruits4)
print(fruits3)
#["watermelon", "apple", "grape", "lemon"]

fruits3.reverse()
print(fruits3)
#['lemon', 'grape', 'apple', 'watermelon']

my_list4 = [4,6,7,8,9,1,2]
my_list4.sort()
print(my_list4)
#[1, 2, 4, 6, 7, 8, 9]
my_list4.sort(reverse=True)
print(my_list4)
#[9, 8, 7, 6, 4, 2, 1]

my_string = "My name is Inga"
my_list = my_string.split(" ")
print(my_list)
#['My', 'name', 'is', 'Inga']

joined_string = " ".join(my_list)
print(joined_string)
#My name is Inga

my_numbers = [ 6,5,4,3,7,44]
print(max(my_numbers))
#44
print(sum(my_numbers))
#69