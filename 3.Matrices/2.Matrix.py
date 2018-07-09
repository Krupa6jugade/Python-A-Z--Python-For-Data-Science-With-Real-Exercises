import numpy as np

my_data = np.arange(0,20)

print(my_data)

new_data = np.reshape(my_data,(5,4))
print(new_data)

print("Print Number",new_data[2,2],"in to The matrix !")

matrix_1 = np.reshape(my_data,(5,4), order='c')

print("print Matrix order by c : \n",matrix_1)

matrix_2 = np.reshape(my_data, (5,4), order='F')

print("print Matrix order by F : \n",matrix_2)

print(matrix_2[0,2])


extra_data = new_data.reshape((5,4))

print(extra_data)

#Do some thing extra

print("\n")
A = ["Aaaaa","j","Rocket"]
B = ["it's","a","Programme"]
C = [1,2,3]

make_matrix = np.array([A,B,C])

print(make_matrix)


#######################





