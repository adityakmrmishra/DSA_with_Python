'''
print the below pattetrn 

A
BB
CCC
DDDD
EEEEE
'''


import string

alphabet = string.ascii_uppercase
for i in range(5):
        for j in range(i+1):
            print(alphabet[i],end=' ')
        print()