# Find the repeating and missing numbers
# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.



def findMissingRepeatingNumbers(a):
    repeat , missing = 0, 0
    for i in range(1,len(a)+1):
        c=0
        for j in range(len(a)):
            if a[j] == i:
                c+=1

        if c == 2:
            repeat = i
        elif c == 0:
            missing = i


        if repeat != 0 and missing != 0:
            break

    return [repeat , missing]                    



a = [3, 1, 2, 5, 4, 6, 7, 5]
ans = findMissingRepeatingNumbers(a)
print("Repeateing no. is", ans[0],"and missing no, is ", ans[1])