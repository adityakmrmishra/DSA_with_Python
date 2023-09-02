#Given a number, check if it is Armstrong Number or Not.

#first count the no. of digits
def count_digits(n):
    c=0
    x=n
    while(x != 0):
        x//=10
        c+=1
    return c
#now do sum of digits raised to power no. of digits
def is_armstrong(n,c):
    sum=0
    x=n
    while x != 0:
        digit = x % 10
        sum += pow(digit,c)
        x //=10
    return sum == n  # if sum == original no. i.e. n than it is Armstrong Number otherwise not

n= int(input('Enter the number: '))

print(is_armstrong(n,count_digits(n)))