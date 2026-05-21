# Python Keywords
# Python keywords are reserved words that have a specific meaning in the language and cannot be used as identifiers (variable names, function names, etc.). Here are some examples of Python keywords:
# and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
# You can use the built-in function kwlist from the keyword module to get a list of all Python keywords. Here's an example:

# import keyword
# print(keyword.kwlist)

# Example of using the and, or, not keywords
# a = True
# b = False
# print(a and b) # False
# print(a or b) # True
# print(not a) # False
# print(a == b) # False
# print(a != b) # True 






# Example of a break, continue keywords and identifier. check the value of i is less than 5 
# for i in range(1,10):
#     print(i)
#     if i < 5 : 
#         continue
#     else:
#         break

# keyword program for, in, if, elif, else
# for i in range(4):
#     if (i == 1):
#         print("one")
#     elif (i == 2):
#         print("two")
#     else:
#         print("exist")

# Example of def, if, and else keywords. check i is odd or not
# def oddeven(num):
#     if num%2 == 0:
#         print("even")
#     else:
#         print("odd")
# oddeven(30)

# Example of try, except, raise
# def num(num):
#     try:
#         r = 1.0/num
#     except:
#         print(f"{num} not dived by 1")
#         return
#     return r
# print(num(10))
# print(num(0))
