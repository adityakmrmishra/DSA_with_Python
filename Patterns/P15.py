'''

Print the below pattern 
ABCDE
ABCD
ABC
AB
A

'''

import string

alphabet = string.ascii_uppercase
c=5
for i in range(1,6):
        print(alphabet[:c],end=' ')
        c=c-1
        print()