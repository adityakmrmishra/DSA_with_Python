def print_name(i,n):
    if i > n:
        return 
    print("Lucifer")
    print_name(i+1,n)
    


n = int(input("How many time you want to print your name?: "))

print_name(1,n)
