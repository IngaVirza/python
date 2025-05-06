my_name = "Inga"
print(my_name)
#Inga
print(type(my_name))
#<class 'str'>
print(id(my_name))
#2646770166704


# Long String """

info_msg= """Hello 
my dear fried, 
lololololololololololololololololololololololol"""
print(info_msg)


#function with string

my_name = 'Inga'
print(len(my_name))
#4
print(my_name[0])
#I
print(my_name[1:3])
#ng


#method string
my_comment = 'This is my short comment'
print(len(my_comment))
print(my_comment.replace('short','long'))
#This is my long comment
print(my_comment.count(' '))
#4
print(my_comment[0])
#T
print(my_comment[2:7])
#is is
print(my_comment[:10])
#This is my