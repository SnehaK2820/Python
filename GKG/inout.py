# in/out
# val = input("enter your name : ")
# print("your name is",val)
# li = input("Enter elements separated by space: ").split()
# print("List of elements:", li)
# x, y = input('enter your name: ').split()
# print(f'name of {x} and {y}')

# 3rd

# S = input("enter string: ")
# N = input("enter integer value:")
# n = int(N)+10
# F = float(input("enter float:"))
# f = F*10

# print(f"The string {S} is printed as it is.")
# print(f"The integer {N} is increased by 10 and results in {n}.")
# print(f"The floating-point number {F} is multiplied by 10 and results in {f}.")

#1st
# a = input()
# b = input()
# separator = input()[0]

# ########### Write your code below ###############
# print(a,b)
# # Print with space
# print(a,b+a+separator+b)
# # Print with separator
# print(a+b)
# # Print without space

# 2 problem

# print("enter your name: "+input())


# 
# a = int(input())
# b = int(input())

# ########### Write your code below ###############

# # Write Code to Swap

# ########### Write your code above ###############

# print(a, b)
# a,b = b,a
# print(a,b)

# Assign Function to a Variable in Python
# x = 123  # global variable

# def display():
#     x = 98  # local variable
#     print(x)
#     print(globals()['x'])  # accesses global x
# print(x)

# if num is even or odd
# def funct(num):
#     if ( num % 2 == 0):
#         print("Even num")
#     else:
#         print("Odd num")
# funct(20)
# funct(5)
# funct(6)

# def fun(num):
#     return num*2

# a=fun
# print(a(1))
# print(a(2))
# print(a(3))

# a = 10
# b = 12
# c = 0
# if c :
#     print("All the numbers have boolean value as True")
# else:
#     print("Atleast one number has boolean value as False")

#User function Template for python3
# a = input()
# b = input()
# c = input()
# # Write your code below that prints a a times and b b times, seperated by c
# d = int(a)
# e = int(b)
# print(a*d+c+b*e)

# walrus

# n = int(input())
# if n >0:
#     print(f'yes greater 0: {n}')
# else:
#     print('no')

# if (n := int(input())) !=0:
#     print("yes")
# else:
#     print(f"it is {n}")
# nums = [10, 20, 30]
# if ( nums := sum(nums) ) >50:
#     print(nums)

# while (data := input("Enter: ")) != "exit":
#     print(data)
s = "python"
if (s:=len(s)) %2 == 0  :
    print("even")
else:    print("odd")




