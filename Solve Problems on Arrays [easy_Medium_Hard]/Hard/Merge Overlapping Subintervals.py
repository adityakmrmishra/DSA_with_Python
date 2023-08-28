# Merge Overlapping Sub-intervals
# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.


def mergeOverlappingIntervals(arr):

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(len(arr)):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans


arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
ans = mergeOverlappingIntervals(arr)
print("The merged intervals are:")
print(ans)