def is_prime(n):
    p = 0
    for i in range(2,n//2):
        if n%i ==0:
            p = 1
        break
    if  p == 0:
        print("It is prime no")
    else:
        print("It is not a prime no")    


n= int(input('Enter the number: '))
is_prime(n)        