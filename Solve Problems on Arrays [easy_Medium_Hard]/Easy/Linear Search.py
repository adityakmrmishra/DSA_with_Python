def Linear_Search(array,item):
    pos = -1
    for i in range(len(array)):
        if array[i] == item:
            pos=i
        else:
            pos    
    return pos

# array=[] 
# n = int(input("Entser the size of array :"))
# print("Enter the array you want to sort:")
# for i in range(n):
#     array.append(int(input()))
array = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
item = 7
pos = Linear_Search(array,item)
if pos == -1:
    print("Item not found ")
else:
    print("The {0} is present at Position {1}".format(item ,pos))