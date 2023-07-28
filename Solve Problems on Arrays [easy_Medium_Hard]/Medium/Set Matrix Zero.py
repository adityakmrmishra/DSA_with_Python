# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.




def set_zero(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                for k in range(len(m)):
                        if m[k][j] != 0:
                            m[k][j] = -1
                for k in range(len(m[0])):
                        if m[i][k] != 0:
                            m[i][k] = -1

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == -1:
                m[i][j] = 0

    return m                





# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))

# # Initialize matrix
# matrix = []
# print("Enter the entries row wise:")

# # For user input
# # A for loop for row entries
# for row in range(Row):   
#     a = []
#     # A for loop for column entries
#     for column in range(Column):  
#         a.append(int(input()))
#     matrix.append(a)

# # For printing the matrix
# for row in range(Row):
#     for column in range(Column):
#         print(matrix[row][column], end=" ")
#     print()
import numpy 

matrix=[[1,1,1],[1,0,1],[1,1,1]]
print(numpy.shape(matrix))


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j] ,end = ' ')
    print()  

print(set_zero(matrix))