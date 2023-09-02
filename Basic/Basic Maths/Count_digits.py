'''
Given an integer N, write a program to count the number of digits in N.
'''
# METHOD 1 :- 
def count_digits(n):
    c=0
    x=n
    while(x != 0):
        x//=10
        c+=1
    return c

n=12345
print(count_digits(n))    

# METHOD 2 :-as the inpuyt is in string so simply take out  its length using len method 
n=input('Enter the number of digits you wish to count: ')
print(len(n))