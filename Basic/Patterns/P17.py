'''
Print the below pattern
    A
   ABA
  ABCBA
 ABCDCBA
'''

import string

alphabet = string.ascii_uppercase
n = 4
for i in range(1, n+1):
    s = alphabet[:i]
    s = s + s[-2::-1]
    print(s.center(2*n-1))



# The center() method is a built-in string method in Python that returns a string that is padded with a specified character (default is space) so that the original string is centered within the new string of a specified width.

# Here’s an example:

# text = 'hello'
# width = 10
# result = text.center(width)
# print(result)
# Copy
# This code will output the string '  hello   ', which has a total width of 10 characters and the original text 'hello' is centered within it.    