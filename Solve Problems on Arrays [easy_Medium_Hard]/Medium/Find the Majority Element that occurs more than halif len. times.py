from collections import Counter
def Majorty_elements(arr):
    mp = Counter(arr)
    for i in mp:
        if mp[i] >= len(arr)/2:
            return i

# In this code, we create a Counter object called mp by passing the arr list as an argument to the Counter constructor. The Counter object automatically counts the frequency of each element in the list and stores it as a key-value pair, where the key is the element and the value is its frequency. Then we iterate over the keys of the mp dictionary and print the element and its frequency.  



arr = [4,4,2,4,3,4,4,3,2,4]

print("The elements that occures more then half are ",Majorty_elements(arr))