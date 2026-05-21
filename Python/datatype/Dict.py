# # dictionary
# my_dict = {"name": "Sneha", "age": 30, "city": "New York"}
# # print(my_dict["name"])
# # print(my_dict.get("age"))


# # Python Dictionary get() method chained
# S = {'GFG': {"nis":"name"}}

# # print(S['GFG'])
# # print(S.get('GFG',{}.get('nis')))
# # print(S.get('Gfg', {}).get('nis'))
# # print(str(S.get('Gfg', {}).get('nis')))

# test_dict = {'Gfg' : {'is' : 'best'}}
# # print("test"+" "+ test_dict['Gfg']['is'])
  
# # printing original dictionary
# # print("The original dictionary is : " + str(test_dict))
  
# # using nested get()
# # Safe access nested dictionary key
# res = test_dict.get('Gfg', {}).get('is')
  
# # printing result
# # print("The nested safely accessed value is :  " + str(res))

# # iterate dictionary kyes(), values(), items()
# my_dict = {"name": "Sneha", "age": 30, "city": "New York"}
# d = my_dict.keys()
# print(type(d))
# print(my_dict.values())
# for i in my_dict.values():
#     print(i)

# x = {X:X**2 for X in range(1,6)}
# print(x)
# keys = ['a', 'b', 'c', 'd', 'e', 'f']
# values= [1,2,3,4,5,6]
# d = {k:v for k,v in zip(keys,values)}
# # print(d)
# d={x:x*3 for x in 'orange' }
# d={x: len(x) for x in ['apple','fig','banana']}
# print(d)

# # dict with condition statement
# d = { x:x for x in range(6) if x %2 ==0 }
# print(d)

# #dict to list tuple
# d = {'a':1, 'b':2, 'c':3}
# print(list(d))
# print(tuple(d))

# # Combine Dictionary keys and values
# d = {'a':1, 'b':2, 'c':3}
# a = d.keys()
# b = d.values()
# c = zip(a,b)
# c = list(c)
# print(c)
# print(type(c))


# a = [10, 20, 30]
# b = ['a', 'b', 'c']

# for sub,(add,even) in enumerate(zip(a,b),start=1):
#     print(sub,add,even)

# a = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']
# b = ['java', 'python', 'R', 'cpp', 'bigdata']
# c = [78, 100, 97, 89, 80]

# for i, (name, subject, mark) in enumerate(zip(a, b, c)):
#     print(i, name, subject, mark)


 
# N = 5 
# names = ['john', 'ala', 'ilia', 'sudan', 'mercy'] 
# marks = [100, 200, 150, 80, 300]
# a = zip(names,marks)
# print("Roll No. Name Marks", list(a))


# 
chatgpt = {"name": "YourName", "age": 26}
# city" key add p
chatgpt['city'] = 'Dindigul'
# print(chatgpt)

# Count using dictionary
a = "banana"
count = {}
for i in a:
    count[i] = a.count(i)
# print(count)

students = {
    {"name": "Arun", "age": 20, "mark": 80},
    {"name": "Bala", "age": 22, "mark": 85},
    {"name": "Chitra", "age": 21, "mark": 90},
    {"name": "Dinesh", "age": 23, "mark": 75}
}

 

