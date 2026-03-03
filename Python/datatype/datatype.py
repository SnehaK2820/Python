# string mehod

# slicing
# s = 'Hello sneha'
# s = 'H'+s[1:]
# print(s)
# s = s.replace('sneha', 'Hemalatha')
# print(s)
# print(s.count('l'))

# a = {'a':1,'b':3}
# print('sneha {a} {b}'.format_map(a))
# string='sneha'
# length = 8
# fillchar = '*'
# a = string.rjust(length,fillchar)
# print(a)

# slicing
s ='abcdefghijk'
s = s[:-1]
# print(s)
# print(type(None))
a = []
a.append([1, [2, 3], 4])
a.extend([7, 8, 9])
# print(a,a[0],a[1],a[2])
# print(a[0][1][1]+a[2])
z = []
x1 = []
for x in 'Geeks 22966 for Geeks':
    if x.isdigit():
        x1.append(x)
# print(x1)
y1 = []
for y in range(20):
    y1.append(y)
# print(y1)

for z1 in y1:
    if z1 in x1:
        z.append(z1)
# print(z)

a = 'Geeks 22536 for 445 Geeks'
b = [x for x in a if x.isdigit() ] 
# print(b)
a =[2,3,9]
a = [[x for x in [a]] for x in range(3)]
# print(a)
li = ['a', 'b', 'c'] * -3
# print(li)
a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 

a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 


subtracted = list()
for a, b in zip(a, b):
    item = a -b
    subtracted.append(item)

# print(subtracted)
a = [1998, 2002] 
b = [2014, 2016] 
# print ((a + b)*2)
# statement 1
li = range(100, 110) 
# print([x  for x in li])
# statement 2
# print (li.index(105))


a = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
b = a 
c = a[:] 

b[0] = 'Code'
c[1] = 'Mcq'

count = 0
[count  if c[0] == 'Code' else count if c[1] == 'Mcq' else count == 10 for c in (a, b, c)]

# print (count)

# list to sring
def listTraversal(arr):
    #code here
    a = ' '.join(str(x) for x in arr)
    print(a)
arr = [54, 43, 2, 1, 5]
# print(listTraversal(arr))   
def decrementList(arr):
    a = ' '.join(str(x-1) for x in arr)
    return a
# print(decrementList([54, 43, 2, 1, 5]))

def appendToList(a,b,c):
    a = a
    b = b
    c = c
    return [a,b,c]
# appendToList(1,2,3)

suma = [-12, 8, -7, 6, 12, -9, 14]
a = sum(suma)
# print(a)

# count of given item in list
from typing import List
def alt_sub(X:List[int]) -> int:
    count = 0
    for i in X:
        count+=1
    
    return count
print(alt_sub([1, 2, 3]))
