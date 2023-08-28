# Program to generate Pascal’s Triangle
# Problem Statement: This problem has 3 variations. They are stated below:

# Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

# Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

# Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

# --------------------------------------------------------------------------------------------------- #

# Variation 1:

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element


r = 5 # row number
c = 3 # col number
element = pascalTriangle(r, c)
print(f"The element at position (r,c) is: {element}")    



# --------------------------------------------------------------------------------------------------- #

# Variation 2:
def pascalTriangle2(r):
    # for i in range(1,r+1):    
    #     print(nCr(r - 1, i - 1))
    ans= 1
    print(ans)
    for i in range(1,r):
        ans= ans*(r-i)
        ans= ans//(i)
        print(ans)


r = 5 # row number
# pascalTriangle2(r)


# --------------------------------------------------------------------------------------------------- #

# Variation 3:

def generateRow(r):
    # for i in range(1,r+1):    
    #     print(nCr(r - 1, i - 1))
    res=[]
    res.append(1)
    ans= 1
    for c in range(1,r):
        ans= ans*(r-c)
        ans= ans//(c)
        res.append(ans)    
    return res    



def pascalTriangle3(n):
    res=[]
    for i in range(1,n):
        res.append(generateRow(i))
    return res


n=7
print(pascalTriangle3(n))

