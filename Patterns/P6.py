'''
Print the below  pattern 
12345
1234
123
12
1

'''


for i in range(5):
    for j in range(1,5-i+1):
        print(j,end='')

    print()    

    