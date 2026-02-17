# def name():
#     print("hello")
#     print("hi")
# name()
# a=19757.46
# b=133.


#   print(123'n'3
# i=[1,3,2,4]

# lst = ['Alice', 'Bob', 'Carl']
# for i, j in enumerate(lst):
#     print(i, j)


# i = [1, 3, 2, 4]
# j = ["asdf", "asd", "asd", "asd"]
# for a in i:
#     for b in j:

#         print(a)
#         print(b)

# # python function


# def fectorial(n):
#     if n < 1:
#         return 1
#     else:
#         return (n * fectorial(n-1))


# num = int(input("enter the number "))
# print("the fectorial of", num, "is", fectorial(num))

# python function


# def fectorial(n):
#     if n < 1:
#         return 1
#     else:
#         return (n * fectorial(n-1))


# num = int(input("enter the number "))
# print("the fectorial of", num, "is", fectorial(num))


# anonymous function lambda()
'''syntax
    lambda argument:expression
    map(function,iterable)

    sorted(iterable, key=None, reverse=False)
'''
# add two number
add = lambda x:x+2
# print(add(2))
# multiple two number
mul = lambda x:x*2
# print(mul(5))
# Even or Odd Check
is_even = lambda x:x%2 == 0
# print(is_even(2))
# print(is_even(1))
# List Double Using map()
l1 = [2,1,3,0,4,8,-9,5,-1,6]
double_list = list(map(lambda x:x*2, l1)) 
# print(double_list)
# Filter Even Numbers
filter_even = list(filter(lambda x:x%2 == 0, l1))
# print(filter_even)
# Sort List (Very Important)
filter_short = list(sorted(l1, key = lambda x:x))
# print(filter_short)
# example
# number cube 
cube = lambda x: x**3
# print(cube(3))
# 2 numbers-la biggest
biggest = lambda a,b: a if a>b else b
# print(biggest(10, 25))
# odd numbers mattum filter
l2= [1,2,3,4,5,6,7]
odd_filter = list(filter(lambda x:x%2 != 0, l2 ))  
# print(odd_filter)
# String reverse
s = lambda s:s[::-1]
# print(s('PYTHON'))

# Marks based on descending order sort  sorted(iterable, key=None, reverse=False)
students = [
    {"name": "Arun", "marks": 80},
    {"name": "Bala", "marks": 95},
    {"name": "Chetan", "marks": 70}
]
stend = list(sorted(students, key = lambda x: x['marks'] ))
# print(stend)

#Number Square
x=lambda x:x**2
# print(x(7))
# Two Numbers Comparison
low = lambda x,y: y if x>y else x
# print(low(10, 25))

# List Odd Numbers Filter
l1 = [10, 15, 20, 25, 30]
odd = list(filter(lambda x:  x%2 != 0, l1 ))
# print(odd)
fruits = ['apple', 'banana', 'cherry']
fruits = list(map( lambda x:x.upper(), fruits))
# print(fruits)

students = [
    {"name": "Arun", "marks": 80},
    {"name": "Bala", "marks": 95},
    {"name": "Chetan", "marks": 70}
]

# marks descending order
des_order = list(sorted(students, key = lambda x:x['marks'], reverse=True))
# print(des_order)
# . Using with Condition Checking
check = lambda x: "Positive" if x > 0 else "Zero" if x == 0 else "Negative" 
# print(check(5))
# print(check(-3))
# print(check(0))
lc_fun = [lambda arg = x: arg*2  for x in range(6)]
# for i in lc_fun:
    # print(i())
na = lambda:'hemllo'
# print(na())

# double each elements of the given list
a = [1, 2, 3, 4] 
def fun(val):
    return val*2

map_method = list(map(fun,a))
# print(map_method)

import json
data = {"name": "Sneha", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)

    import json

with open("data.json", "r") as file:
    data = json.load(file)

# print(data)

# Symmetrical and Asymmetrical Function and palindrome

# a = "abaaba"
# s = len(a)//2
# sym = a[:s] == a[s:] if len(a) %2 == 0 else a[:s] == a[s+1:]
# pal = s == a[::-1]
# print("Symmetrical" if sym else "Not Symmetrical")
# print("Palindrome" if pal else "Not Palindrome")

# s = "amaama"
# half = len(s) // 2

# # Palindrome
# pal = all(s[i] == s[-i-1] for i in range(len(s)//2))

# # Symmetry
# sym = s[:half] == s[half:] if len(s) % 2 == 0 else s[:half] == s[half+1:]

# print("Symmetrical" if sym else "Not Symmetrical")
# print("Palindrome" if pal else "Not Palindrome")

# count of the char
a = "Python"
count = 0
for char in a:
    count += 1
# print(count)   
# 
def trim(str):
    s = str.strip()
    return s
# print(trim("  Hello World  "))
def exists(str, x):
    s = str.find(x)
    return s
# print(exists('hello', 'l'))
def titleIt(str):
    s = str.title()
    return s
# print(titleIt('hello'))
def casesSwap(str):
    s = str.swapcase()
    return s

# print(casesSwap('hello'))
s = "ABCddE"
s = s.lower()
# print(s)
class student:
    def removeduplicate(s):
        result = ""

        for i in s:
            if i not in result:
                result += i
        return result

    # print(removeduplicate("Geeks for Geeks problem"))

def isPalindrome(s):
    return s.lower() == s.lower()[::-1]

# print(isPalindrome('Hello'))
# print(isPalindrome('TenEt'))
 


