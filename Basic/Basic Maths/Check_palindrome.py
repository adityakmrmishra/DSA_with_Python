# check whether the given number is a palindrome or not 
# A palindromic number  is a number (such as 16461) that remains the same when its digits are reversed
# the following program returns true if it is a palindromic number and false otherwise
def is_palindrome(n):
    rem= 0
    rev=0
    x=n
    while(x!=0):
        rem=x%10
        rev=rev*10+rem
        x//=10
    if rev == n :
        return True
    else: 
        return False

n= int(input('Enter the number: '))
print(is_palindrome(n))