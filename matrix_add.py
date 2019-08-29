from numpy import *

matrix_1=matrix('1 2 3;4 5 3;9 5 3')
matrix_2=matrix('2 4 5;6 4 5;7 4 2')

add_matrix=matrix_1+matrix_2
print(f"{matrix_1} \n + \n {matrix_2}  \n =   \n {add_matrix}")