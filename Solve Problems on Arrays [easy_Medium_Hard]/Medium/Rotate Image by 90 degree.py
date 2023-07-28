# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.
import numpy as np

m =[[1,2,3],[4,5,6],[7,8,9]]
l = np.transpose(m)
print(np.fliplr(l))

from typing import List
def rotate(m: List[List[int]]) -> None:
    for i in range(len(m)):
        for j in range(i):
            m[i][j] , m[j][i] = m[j][i] , m[i][j]

    for i in range(len(m)):
        m[i].reverse()        

    

arr =[[1,2,3],[4,5,6],[7,8,9]]
rotate(arr)
print()
print("method 2")
for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()


''' Program to transpose a matrix using list comprehension'''

# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

# for r in result:
#     print(r)        