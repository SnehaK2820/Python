# Iterator and generator

# Iterable --  __iter__() --  Iterator -- __next__() -- StopIteration 
# Iterable --  list, tuple, dict, set, str
# Iterator -- object that implements the iterator protocol, which consists of the methods __iter__() and __next__()
# You prepared before Real life meaning:
# Iterable -- A container which you can iterate over
# Iterator -- An object that helps you iterate over an iterable
a = ['cho1','cho2','cho3','cho4']
b = iter(a)
print(next(b),"cjfhdhg")
# iter() -- 
# next() --

# Generator -- A generator is a special type of iterator that is defined using a function with the yield statement.