# Reverse the given number

def reverse_number(n):
    rem= 0
    rev=0
    x=n
    while(x!=0):
        rem=x%10
        rev=rev*10+rem
        x//=10
    return rev  

n= int(input('Enter the number of digits you wish to reverse: '))
print(reverse_number(n))