user_roles =("admin", "editor", "viewr")
print(user_roles)
#('admin', 'editor', 'viewr')
print(len(user_roles))
#3
for role in user_roles:
    print(role)

#admin
#editor
#viewr    

print("admin" in user_roles)
# True

my_tupe = ("admin",)
print(type(my_tupe))
#<class 'tuple'>

role_1, role_2, role_3 = user_roles

print(role_1)
print(role_2)
print(role_3)

#admin
#editor
#viewr