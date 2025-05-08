##### Assigning Subsequent Rows to Matrix first row elements

list_1  = [[1,2,3],[4,5,6],[7,8,9],[9,8,7]]

dic = {list_1[0][i]:list_1[i+1] for i in range(len(list_1) -1)} #Using dictionary comprehension
print(dic)

dic_1 = dict(zip(list_1[0],list_1[1:])) # Using zip()
print(dic_1)


A = [[1, 2], [3, 4]]
 
# creating second matrix
B = [[4, 5], [6, 7]]
 
print("Printing elements of first matrix")
print(len(A))
print("Printing elements of second matrix")
print(B)

