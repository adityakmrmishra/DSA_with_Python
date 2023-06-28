#Print all Divisors of a given Number

# run the loop fron 1 to half of n 
#check if the number is completely divisile by the i if yes than print no.'s
def print_divisors(n):
    for i in range(1,n//2+1):
        if n % i == 0:
            print(i, end = ' ')
            if i != n/i:
                print(int(n/i), end=" ")




n= int(input('Enter the number: '))
print_divisors(n)