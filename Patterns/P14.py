'''
Print the below pattern 

A
A B
A B C
A B C D
A B C D E
A B C D E F
'''


import string

alphabet = string.ascii_uppercase
for i in range(1, 7):
    print(' '.join(alphabet[:i]))

# for i in range(1, 7):
#     print(alphabet[:i], end=' ')
#     print()  