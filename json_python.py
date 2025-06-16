import json

book = {
    'title':'1984',
    'author': 'George Orwell',
    'isbn': '978-045154534',
    'uuid': 'a0eesdfs-34fsdf',
}

json_string = json.dumps(book)
print(type(json_string))

print(json_string)

#<class 'str'>
#{"title": "1984", "author": "George Orwell", "isbn": "978-045154534", "uuid": "a0eesdfs-34fsdf"}

json_books ='{"title": "1984", "author": "George Orwell", "isbn": "978-045154534", "uuid": "a0eesdfs-34fsdf"}'
book = json.loads(json_string)
print(type(book))
print(book)

#<class 'dict'>
#{'title': '1984', 'author': 'George Orwell', 'isbn': '978-045154534', 'uuid': 'a0eesdfs-34fsdf'}