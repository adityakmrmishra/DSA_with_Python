'''
Print the below pattern
F
E F
D E F
C D E F
B C D E F
A B C D E F


'''
import string

N=6
alphabet = string.ascii_uppercase
for i in range(1,N+1):
    for j in range(N-i,N):
        print(alphabet[j],end=' ')
    print()