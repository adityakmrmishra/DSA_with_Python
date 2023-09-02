
from collections import Counter

arr = [1, 2, 3, 2, 4, 3, 2]
counter = Counter(arr)
print(counter.most_common())
#above line prints [(2, 3), (3, 2), (1, 1), (4, 1)] whis is a list of tuples and each tuple consists of element and its count 
most_frequent = counter.most_common(1)[0][0]
print("Highest frequency element :", most_frequent)
least_frequent = counter.most_common()[-1][0]
print("Lowest frequency element :", least_frequent)

#  The most_common() method of the Counter object to find the most common element in the list. 
#  The most_common() method returns a list of tuples containing the elements and their counts, sorted by the count in descending order. In this case, we pass the argument 1 to the most_common() method to get only the most common element. The [0][0] indexing at the end extracts the first element of the first tuple in the list, which is the most common element.

# What does [0][0] means in counter.most_common()[0][0]

#  if we have a list arr = [1, 2, 3, 2, 4, 3, 2], then calling counter.most_common(1) will return [(2, 3)], which is a list with one tuple. The first element of the tuple is 2, which is the most common element in the list, and the second element is 3, which is its count.

# The [0] indexing after most_common(1) extracts the first tuple from the list, which is (2, 3). The second [0] indexing extracts the first element of this tuple, which is 2. So, in this example, counter.most_common(1)[0][0] will return 2.