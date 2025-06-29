squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)    

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = [ x ** 2 for x in range(10)]
print(squares2)

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)

print(even_squares)   
#[0, 4, 16, 36, 64]    


even_squares2 = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares2)
#[0, 4, 16, 36, 64]

labelled_numbers = []
numbers = [1,2,3,4,5]

for num in numbers:
    if num % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd") 

print(labelled_numbers)           
#['odd', 'even', 'odd', 'even', 'odd']

labelled_numbers2 = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(labelled_numbers2)

#['odd', 'even', 'odd', 'even', 'odd']


square_dict = {x: x ** 2 for x in range(10)}

print(square_dict)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

print(transpose_matrix)       

#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

transpose_matrix2 = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix2)
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]