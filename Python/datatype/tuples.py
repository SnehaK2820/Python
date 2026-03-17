# # tuple()
# a = (1, 2, 3, 4, 5)
# b = ('abc', 'def', 'ghi')
# c = [a,b]
# # print(a+b+(c,), type(a), type(c,) )
# a = 'sneha'
# a = ['sneha','hema','latha']
# # print(a[1:])

# ''' tuple slicing '''
# tup = tuple('ksneha')
# # Removing First element
# # print(tup[1:])
# # Reversing the Tuple
# # print(tup[::-1])
# # Printing elements of a Range
# # print(tup[4:9])

# '''del tuple object'''
# tup = (1,2,3,4)
# # print(type(a))
# # del a
# ''' tuple with * key '''
# a,*b,c = tup
# # print(a,b,c) # just through ValueError: too many values to unpack (expected 3)
# # print(a,b,c) #*b collects everything in between into a list.
# # Remove Empty Tuples from a List - Python
# a = [(), ('sneha', 'hema'), (), ('latha',), (),('a')]
# # a = [ i for i in a if i] # empty tuple evaluated to False
# a = list(filter(None,a)) #filter keyword

# a = [[1, 2], [], [3, 4], [], [5]]
# res = list(filter(None,a)) #remove emo=pty list

# # Using for loop
# res = []
# for i in a:
#     if i:
#         res.append(i)
# # print(res)

# test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
# test_list = list(filter(None,test_list))
# # print(test_list)

# test_list = [(None, None), (None, None), (3, 4), (12, 3), (None, )] 
# # remove none tuple
# removed_none_tuple = [i for i in test_list if i != (None, None) and i != (None, )]
# # print(removed_none_tuple) # remove none tuple using filter
# test = list(filter(None,test_list))
# # print(test_list)
# # remove tuple none
# list_a = []
# for i in test_list:
#     if None not in (i):
#         list_a.append(i)


# # Count occurrences of an element in a Tuple
# tuple1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

# def Count(tup,a):
#     return tup.count(a)
# tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# enq = 4
# enq1 = 10
# enq2 = 8
# # print(Count(tup, enq), "times")
# # print(Count(tup, enq1), "times")
# # print(Count(tup, enq2), "times")

# x = [i for i in tuple1 if i == 10]
# # print(x, len(x))


# tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# # print(tup.count(10))


# # First element Last element
# a = (10, 20, 30, 40, 50)
# print(a[0])
# print(a[-1])



# # Length of the tuple Sum of all elements
# b=(5, 10, 15, 20, 25)
# print(sum(b))

    

# # Second element Check if "grapes" is in tuple (True/False output)
# c = ('apple', 'banana', 'grapes', 'orange')

# for i in c:
#     if i == 'grapes':
#         print(True)

# # Elements from index 2 to 5 (slicing use pannu)
# d =(1, 2, 3, 4, 5, 6, 7, 8)
# print(d[2:5])

# # Convert this tuple into list Add 50 Convert back to tuple Print final tuple
# e=(10, 20, 30, 40)
# e =list(e)
# e=e+[50]
# print(e)


# #  Count Even Numbers

# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# # Count how many even numbers are there
# # Print the count
# s = []
# for i in t:
#     if i % 2 == 0:
#         s.append(i)
# print(len(s))

# # 🟡 Problem 2 – Find Maximum Without max()

# t = (45, 12, 89, 32, 67)
# t = list(t)
# t.sort()
# print(t)

# # 🟡 Problem 3 – Remove Duplicates

# t = (1, 2, 2, 3, 4, 4, 5, 6, 6)
# t = set(t) 
# t = tuple(t)
# print(t)

# # 🔵 Problem 4 – Tuple Inside Tuple
# t = ((1, 2), (3, 4), (5, 6))
# print(t[1][1], t[2][0])


# Mini Challenge – Tuple Power
t = (10, 25, 30, 45, 50, 65, 70)
# # Count how many numbers are greater than 40
# t = [ i for i in t if i>40 ]
# print(len(t))
# # Find the smallest number (without using min())
# t = (10, 25, 30, 45, 50, 65, 70)
# t = list(t)
# print(min(t))
# # Create a new tuple that contains only numbers divisible by 5
# t = [ i for i in t if i%5 == 0]
# print(tuple(t))
# # Print the sum of all numbers
# print(sum(t))

# # count use counting numbers
# count = 0
# for i in t:
#     count += 1
# print(count)

# # Count Even Numbers
# count = 0
# for i in t:
#     if i%2 ==0:
#         count +=1
# print(count)

# # count greater then 10
# t = (5, 12, 7, 18, 3, 20)

# count = 0

# for i in t:
#     if i >10:
#         count +=1
# print(count)




