def add(x: int, y: int):
    return x + y

print(add(1, 2))
#3

def add_all(*args):
    print(args)
    print(type(args))

add_all(1,2,3)    
#(1, 2, 3)
#<class 'tuple'>

def add_all2(*args):
    summary = 0
    for num in args:
        summary += num
    return summary
print(add_all2(4, 2, 3))

#9

values = [1,2,3,4,5]
other_values = [6,7,8,9,10]

print(add_all2(*values,*other_values))

#55

def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

introduce(name="John", age=30, city="Newton")
#{'name': 'John', 'age': 30, 'city': 'Newton'}
#<class 'dict'>

def introduce2(**kwards):
    for key, value in kwards.items():
        print(key)
        print(value)
introduce2(name="Inga", number=4, city="Lida")        
#name
#Inga
#number
#4
#city
#Lida

person = {
    "name":"Inga", "number": 4, "city":"Lida"
}
introduce(**person)
#{'name': 'Inga', 'number': 4, 'city': 'Lida'}
#<class 'dict'>

def func_with_all_arguments(x: int, y:int, *args, value: int = 6, **kwargs):
    print(x,y)
    print(args)
    print(value)
    print(kwargs)

person = {
    "name":"Inga", "number": 4, "city":"Lida"
}
func_with_all_arguments(1,2,3,4,5, **person)    
#1 2
#(3, 4, 5)
#6
#{'name': 'Inga', 'number': 4, 'city': 'Lida'}

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) !=value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified

product = {'id':1, 'name': 'Laptop', 'price': 999.99}
structure = modify_dict(old_dict=product, in_stock=True)        
print(structure)
print(type(structure))

#({'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}, True)
#<class 'tuple'>

structure = modify_dict(old_dict=product, name="Laptop")        
print(structure)
print(type(structure))

#({'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}, False)
#<class 'tuple'>

structure, was_modified = modify_dict(old_dict=product, name="Laptop")        
print(structure)
print(was_modified)

#{'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
#False