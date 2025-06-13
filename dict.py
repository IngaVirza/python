person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(person)

#{'name': 'John', 'age': 30, 'city': 'New York'}

person["job"] = "Engineer"
print(person)
#{'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

person2 = {}
person2["name"]="Frank"
person2["age"]=50
person2["city"]="Boston"

print(person2)
#{'name': 'Frank', 'age': 50, 'city': 'Boston'}
print(person2["name"])
#Frank
print(person2.get("name"))
#Frank
print(person2.get("country"))
#None
#default value 
print(person2.get("country", "USA"))
#USA

for p in person2:
    print(p)
#name
#age
#city   
for p in person2:
    print(person[p]) 
#John
#30
#New York

for item in person2.items():
    print(item)
    print(type(item))
#('name', 'Frank')
#<class 'tuple'>
#('age', 50)
#<class 'tuple'>
#('city', 'Boston')
#<class 'tuple'>    

for item in person2.items():
    key, value = item
    print(item)
    print(key)
    print(value)
    print(type(item))

#('name', 'Frank')
#name
#Frank
#<class 'tuple'>
#('age', 50)
#age
#50
#<class 'tuple'>
#('city', 'Boston')
#city
#Boston
#<class 'tuple'>    

for key, value in person.items():
    print(key)
    print(value)

#name
#John
#age
#30
#city
#New York
#job
#Engineer    


for values in person2.values():
    print(values)

#Frank
#50
#Boston    

person3 = {
    "name": "Oleg",
    "age":30,
    "city": "New York"
}

other_person3 = {
    "city": "New York","age":30,"name": "Oleg",
}
print(person3==other_person3)
#True

person4 = {
    "city": "Minsk",
    "age": 30,
    "name": "Inga"
}

additional_person_info = {
    "job": "Engineer",
    "married": False,
    "city": "Lida"
}

person4.update(additional_person_info)
print(person4)
#{'city': 'Lida', 'age': 30, 'name': 'Inga', 'job': 'Engineer', 'married': False}

person5 = person4 | additional_person_info
print(person5)
#{'city': 'Lida', 'age': 30, 'name': 'Inga', 'job': 'Engineer', 'married': False}
