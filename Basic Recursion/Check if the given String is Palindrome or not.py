#normal approch
# def is_palindrome(str):
#     l = 0
#     r = len(str) - 1
#     while l < r:
#         if not str[l].isalnum():
#             l += 1
#         elif not str[r].isalnum():
#             r -= 1
#         elif str[l].lower() != str[r].lower():
#             return False
#         else:
#             l += 1
#             r -= 1
#     return True


#RECURCIVE APPROCH 
def is_palindrome(str,i):
    if i >= len(str)//2:
        return True

    if str[i] != str[len(str)-i-1]:
        return False
    
    return is_palindrome(str, i+1)

str = "abABABAba"
res = is_palindrome(str,0)

if res ==True:
    print("String is a palindrome")
else: 
    print("String is not a palindrome")