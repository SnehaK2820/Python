
# a,b = '10'
# b,c = '30'
# print(a,b,c)

# # swap
# a = 10
# b = 20
# # print(a,b)
# # temp = a
# # a = b
# # b = temp

# # a = a+b
# # b = a-b
# # a = a-b

# # a=a^b
# # b=a^b
# # a=a^b
# # print(a,b)

# l1 = [1,2,3]
# l2 = [4,5,6]
# cdict = dict(zip(l1,l2))
# # print(cdict)

# convert list to string
# l1 = ['s','n','e','h','a']
# s1 = ','.join(l1)
# # print(s1)

# arr = [1, 4, 3, 2, 6, 5]
# arr.reverse()
# # print(arr)

# # row 
# m,n = 5,6
# mat = []
# for i in range(5):
#     row = []
#     for j in range(6):
#         row.append(0)
#     mat.append(row)
# a = mat
# # print(row)
# # print(mat)
# # for i in mat:
# #     print(i)
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=" ")
# print()

# # list comprehension
list_a = [1, 3,2, 4,5, 6,0]
# # list_a.sort()
# # print(list_a)
# # square = [ n*n for n in list_a]
# # print(square)
# # nested if else comprehension
# odd = [ "divided by 3" if a%3 == 0 else 'divided by 2'  if a%2 == 0 else 'others' for a in list_a ]
# # print(odd)
# # comprehension nested loop
# a = [ (j,i) for i in range(4) for j in range(2)]
# # print(a)

# # print([i for i in range(4) for i in range(4) ])
# numbers = [1, -2, 3, -4, 5]
# squared_positives = [x**2 if x > 0 else 0 for x in numbers]
# # print( squared_positives)
# words = ['python', 'list', 'comprehension']
# unique_starting_letters = {word[0].upper() for word in words}
# # print(unique_starting_letters,words)

# problem for list comprehension
def div3(list_a,x):
    even = [i for i in list_a if i%2 == 0 ]
    odd = [i for i in list_a if i%2 != 0 ]
    # print(even,"even"); print(odd,"odd")

    return [ i for i in list_a if i%x == 0 ]
x = 3
# print(div3(list_a,x) )

x = 'geeks for geeks'
vowels = [ i for i in x if i in 'aeiou' ]
# print(vowels)
starts = [ i for i in x if i.startswith('g') ]
# print(starts)
# print([x*2 for x in range(6) if x%2 == 0 ])

# print(min(list_a))
li = [['a', 'b'], ['c', 'd', 'e']] 
# print(li[10:] )
import copy
li1 = copy.copy(li)
li1[0][0] = 5
print(li)
print(li1)
