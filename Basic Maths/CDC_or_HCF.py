# Find the gcd or HCF  of two numbers.
#Recursively call gcd(b,a%b) function till the base condition is hit.
#b==0 is the base condition.When base condition is hit return a,as gcd(a,0) is equal to a.

def gcd(a, b):
    if b == 0:
        return a
    else: 
        print(a%b)
        return gcd( b , a % b )

a = 2
b=4
print("The GCD of the two numbers is", gcd(a, b))