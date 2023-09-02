def Sum_one_to_n(n,sum):
    if n<1:
        print(sum)
        return
    
    return Sum_one_to_n(n-1, sum + n)


n = int(input("Enter the number : "))
Sum_one_to_n(n,0)