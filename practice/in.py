# lambda argument: expression
add = lambda x,y: x+y
# print(add(3,4))
sqr = lambda x: x**2
# print(sqr(2))
#### lambda map
mapl = [1,2,3]
dobule = list(map(lambda x: x*2, mapl))
# #print(dobule)
lam3 = [1, 4, 2, 5, 6, 0]
fillam =  list(filter(lambda x: 3<x, lam3))
# print(fillam)

let = [(2,1),(1,2),(3,2)]
sorrt = sorted(let, key=lambda x:x[1])
# print(sorrt)
name = ['sneha','prabhakaran','boys']
sorrt = sorted(name, key=lambda name: len(name))
# print(sorrt,"so")

people = [
    {"name": "Anu", "age": 25},
    {"name": "Sneha", "age": 22},
    {"name": "Kavi", "age": 30}
]
peoplesrt = sorted(people, key= lambda people: people['age'])
# print(peoplesrt)
items = ['sneha', 'gokul', 'ajay', 'divya']
# sort = sorted(items, key=lambda x: x[-1]) '''last char'''
# sort = sorted(items, key=lambda x: x[1])  '''first next char'''
# sort = sorted(items, key=lambda x: x[0])'''first char'''
# print(sort)
words = ['apple', 'banana', 'mango', 'kiwi']
result = sorted(words, key=lambda x: len(x))
# print(result)

# map
listq = [1,2,3]
a = list(map(lambda x:x+1, listq))
print(a)


