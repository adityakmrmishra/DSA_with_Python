def countFreq(arr):
    mp = {}
    for i in range(len(arr)):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        if mp[x] == 1 :
            return x




from collections import Counter

arr = [4,1,2,1,2]
counter = Counter(arr)
print(counter.most_common())
least_frequent = counter.most_common()[-1][0]
print("The no. that apperas one is  :", least_frequent)
print("The no. that apperas one is  :", countFreq(arr))
