'''
Print the below pattern
6 6 6 6 6 6  6 6 6 6 6 
6 5 5 5 5 5  5 5 5 5 6 
6 5 4 4 4 4  4 4 4 5 6 
6 5 4 3 3 3  3 3 4 5 6 
6 5 4 3 2 2  2 3 4 5 6 
6 5 4 3 2 1  2 3 4 5 6 

6 5 4 3 2 2  2 3 4 5 6 
6 5 4 3 3 3  3 3 4 5 6 
6 5 4 4 4 4  4 4 4 5 6 
6 5 5 5 5 5  5 5 5 5 6 
6 6 6 6 6 6  6 6 6 6 6

'''

n = 6
# for top pattern
for i in range(n, 0, -1):
    # for top left pattren
    for j in range(n, 0, -1):
        print(max(i, j), end=' ')
    # for top right pattren
    for j in range(2, n +1):
        print(max(i, j), end=' ')
    print()

#for bottom pattern    
for i in range(2, n + 1):
    # for bottom left pattren
    for j in range(n, 0, -1):
        print(max(i, j), end=' ')
    # for bottom right pattren
    for j in range(2, n + 1):
        print(max(i, j), end=' ')
    print()
