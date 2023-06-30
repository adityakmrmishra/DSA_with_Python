def one_to_n(i,n):
    if i > n:
        return
    print(i)
    one_to_n(i+1,n)


n = int(input("Enter the number : "))
one_to_n(1,n)