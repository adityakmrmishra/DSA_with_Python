def fib(i):
    if i <= 1:
        return i
    return fib(i-1) + fib(i-2)


n = int(input("Enter the number : "))
for i in range(n): 
    print(fib(i))