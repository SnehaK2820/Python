# python set is an unordered collection of items.
#  Every element is unique (no duplicates) and must be immutable (cannot be changed).
#  However, a set itself is mutable.
#  We can add or remove items from it. 
# Sets are defined by values separated by comma inside curly braces {} or by using the built-in set() function.

# Creating a set
a = {1, 2, 3, 4, 5}
b = set([1, 2, 3, 4, 5])
c = set((1, 2, 3, 4, 5))
d = set('hello')
e = set()

# set methods (add, update, remove, discard, pop, clear)
# add() method is used to add a single element to the set. If the element already exists, it will not be added again.
# a = {6, 0, 4}

# # adding 1
# a.add(1)
# print(a)

# # adding 0
# a.add(0)
# print(a)


s = {'g', 'e', 'e', 'k', 's'}
t = ('f', 'o')
l = ['a', 'e']

# adding tuple t to set s.
s.add(t)

# # adding list l to set s.
# s.update(l)
# print(s)

# removing an element from the set using remove() method. If the element is not present, it will raise a KeyError.
s.remove('g')
# print(s)
# removing an element from the set using discard() method. If the element is not present, it will not raise an error.
s.discard('x')
# print(s)
# removing an element from the set using pop() method. It removes and returns an arbitrary element
popped_element = s.pop()
# print(popped_element)
# print(s)
# removing all elements from the set using clear() method.
s.clear()
# print(s)

# accessing elements in a set
''' Since sets are unordered, we cannot access elements by index. However, we can iterate through
the set using a for loop or check for membership using the in keyword. '''
# s = {'g', 'e', 'k', 's'}
# # iterating through the set
# for element in s:
#     print(element)
# # checking for membership
# print('g' in s)
# print('x' in s)

# set1 = {1, 2, 3} 
# set2 = set1.copy() 
# set2.add(4) 
# print(set1)
# set1 = {1, 2, 3} 
# set2 = set1.add(4) 
# print(set2) ''' The add method doesn’t return anything. Hence there will be no output.'''
set1 = {1, 2, 3} 
set2 = {4, 5, 6} 
# print(len(set1 + set2)) ''' The + operator is not supported for sets. To combine two sets, you can use the union() method or the | operator.'''


''' Frozenset() is a built-in function in Python that returns an immutable frozenset object.'''
# frozenset is an immutable version of a set. Once a frozenset is created, it cannot be modified.
# frozenset1 = frozenset([1, 2, 3])
# print(frozenset1)  #frozenset({1, 2, 3})
