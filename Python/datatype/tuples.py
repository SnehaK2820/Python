# tuple()
a = (1, 2, 3, 4, 5)
b = ('abc', 'def', 'ghi')
c = [a,b]
# print(a+b+(c,), type(a), type(c,) )
a = 'sneha'
a = ['sneha','hema','latha']
# print(a[1:])

''' tuple slicing '''
tup = tuple('ksneha')
# Removing First element
# print(tup[1:])
# Reversing the Tuple
# print(tup[::-1])
# Printing elements of a Range
# print(tup[4:9])

'''del tuple object'''
tup = (1,2,3,4)
# print(type(a))
# del a
''' tuple with * key '''
a,*b,c = tup
# print(a,b,c) # just through ValueError: too many values to unpack (expected 3)
# print(a,b,c) #*b collects everything in between into a list.
# Remove Empty Tuples from a List - Python
a = [(), ('sneha', 'hema'), (), ('latha',), (),('a')]
# a = [ i for i in a if i] # empty tuple evaluated to False
a = list(filter(None,a)) #filter keyword

a = [[1, 2], [], [3, 4], [], [5]]
res = list(filter(None,a)) #remove emo=pty list

# Using for loop
res = []
for i in a:
    if i:
        res.append(i)
# print(res)

test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
test_list = list(filter(None,test_list))
# print(test_list)

test_list = [(None, None), (None, None), (3, 4), (12, 3), (None, )] 
# remove none tuple
removed_none_tuple = [i for i in test_list if i != (None, None) and i != (None, )]
# print(removed_none_tuple) # remove none tuple using filter
test = list(filter(None,test_list))
# print(test_list)
# remove tuple none
list_a = []
for i in test_list:
    if None not in (i):
        list_a.append(i)


# Count occurrences of an element in a Tuple
tuple1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

def Count(tup,a):
    return tup.count(a)
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(Count(tup, enq), "times")
print(Count(tup, enq1), "times")
print(Count(tup, enq2), "times")

x = [i for i in tuple1 if i == 10]
print(x, len(x))



