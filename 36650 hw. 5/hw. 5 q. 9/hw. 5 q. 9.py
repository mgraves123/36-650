#https://www.geeksforgeeks.org/floor-ceil-function-python/
#https://www.geeksforgeeks.org/python-list-slicing/
#https://www.journaldev.com/23647/python-reverse-string

import math
def palindrome(word):
    middle = math.floor(len(word)/2)
    return print(word[:middle+1] == word[::-1][:middle+1])

palindrome('kayak')
palindrome('ayak')
