# list




# count()
# for loop
a = [1, 2, 3, 4, 5, 6, 3,5,3,7, 8, 9, 10]
count = 0
for val in a:
    if val == 3:
        count +=1
print(count)
print(len(a))
print(a.index(3, 6,10))
b = [1,2,3]
for val in b:
    if val in a:
        a.remove(val)
print(a)
