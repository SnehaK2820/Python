# global variable

# global x
# x="python"

# def myfun():
#     print("django using " +x)
# myfun()
# print("django using "+x)

# class myfun():
#     global y
#     global x
#     y="data base"
#     x="data types"
#     print("learn "+x)
#     def fun():
#         x="new data"
#         print("print"+x)
#     fun()
#     def newfun():
#         c=fun()
#         print(x)
#         print(y)
#     newfun()



# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
# for v in voiceFemales:
#     engine.setProperty('voice', v.id)
#     engine.say('Hello world from ' + v.name)
#     engine.runAndWait()




"""class Parent:
    def __init__(self):
        self.String1 ="Hello"
        self.String2 ="World"
    def Function2(self):
        a=10
        print(a)
        print("Function2 : ", self.String1)
        
    def Function3(self):
        print("Function2 : ", self.String2)
        Function2()
    
# Child class is inheriting from Parent class
class Child(Parent):

	def Function1(self):
		# calling Function2 Method in parent class
		self.Function2()
		print("Function1 : ", self.String2)
		return

### Instance of Parent class
Object1 = Parent()

### Instance of Child class
Object2 = Child()

# Calling Function1 using Child class instance
Object2.Function1()"""
# def Function2(self):
#     a=10
#     print(a)
#     print("Function2 : ", self.String1)
        
# def Function3(self):
#     print(a)
#     print("Function2 : ", self.String2)
#     Function2()
# Function3()
# import itertools
# a=[12,"hello",'s']
# b=[1,2,3,4,5]
# #print(enumerate(a[1]))
# for j,i in itertools.zip_longest(a,b):
#     print(j)
#     print(i)

# print("sneha", 'k', sep='.')


# str_name = input("What is your name ")
# print("Name:"+ str_name)

# a=10
# b=20

# C=a+b
# d=a-b
# e=a*b
# print(a==b)
# print(a<b)
# print(a!=b)
# a and b
# c = not b
# print(c,C,e,d)


# for i in range(0,9):
#     print("rest")



# duplicate char print

# a="sneha"
# c=len(a)
# b= set(a)
# d=len(b)
# if(a==b):
#     print("duplicate")
# else:
#     print("notduplicate")

# if(c==d):
#      print("duplicate")
# else:
#     print("notduplicate")




# k=["sneha","prabha","shapna","suresh","prince","ramesh","rahul","sivakrishan","arul","anandhi","nivetha"]
# a=input( "pls give a name:",)
# b=str(a)
# print(b)
# for i in k:
#     if (i==b):
#         print("yes")
#         c=k.pop(k.index(i))
#         print(c,"c")
#         print(k)

# for num in range(2,-5,-1):
#     print(num, end ="")

# if,else and for 
# x=0
# a=5
# b=2
# if (a>0):
#     if(b<0):
#         x=x+5
#     elif(a>5):
#         x=x+4
#     else:
#         x=x+3
# else:
#     x=x+2
# print(x)

# doubt
# for num in range(10,14):
#     for i in range(2, num):
#         print(num%i)
#         if num%i==1:
#             print(num)
#             break


# a,b=10,20
# if(a+b):
#     print(a)
# else:
#     print(b)


# x=0
# while(x<100):
#     x+=2
# print(x)

# for i in 'sneha':
#     print(i)
#     if i=='a':
#         pass
#     print(i,end=", ")

# numbers =[10,20]
# variable =["chain","table"]
# for i in numbers:
#     for j in variable:
#         print(i,j)

# for i in range(5,-2,-7):
#     print(i)

# a=[9,3,5,2]
# a.sort()
# print(a[0])

# name1 = "sneha"
# name2 = "mom"

# b=name1.reve
# 1


#'''''''' # div by 3
# a=int(input())
# for j in range(2, a):
#     if(j%3==0 and j%5==0):
#         print("FIZZBUS")
#     elif(j%3==0):
#         print("FIZZ")
#     elif(j%5==0):
#         print("BUS")
#     else:
#         print(j)
    

# slicing[:]

# listof=[1,2,3,4,4,5,6,7]
# print(listof[4:5])
# print(listof[:3])
# print(listof[5:])
# print(listof[:-4])
# print(listof[:0])

# add element
# add end of the list
# details=['k.',"sneha",22,2023]
# details.append("28.02.2000")
# print(details)

# list_of=[1,3,2,5,4,3,5,7,9,5,7,6,4,0,7,4,3,2,4,1]
# for i in list_of:
#     print(i,"i")
#     x=list_of.count(i)
#     print(x,"x")


# a=72.73
# list_values=[423.6,827.62,34.8,524.32,9.5,1]
# list_values.sort()
# len_of=len(list_values)
# print(len_of)
# for i in range(len_of):
#     if list_values[i]>a:
#         print(list_values[i],"great")
#         print(list_values[i-1],"less")
#         break

# b=[(10901.39,10012.43,10012.43,10901.39)]
# c = [i for i in b]
# print(type(c))

# list_of=[]
# for i in b:
#     list_of.append(b)
#     print(type(list_of.append(b)))
#     print(i)


# d=b.sort()
# print(b)
# a=['q2','q2','q1','q4','qtd']
# d=b.sort()
# print(d)
# for i in b:
#     print(i)
#     # print(b)
# a=[72.73]
# listA = [[9.5], [8.5], [4.5], [9.5]]
# # list_values=[423.6,827.62,34.8,524.32,9.5,1]
# print(listA.sort())
# len_of=len(listA)
# print(len_of)
# for i in range(len_of):
#     print(i)
#     print(listA[i]<a)
#     if listA[i]>a:
#         # print(listA[i]>a)
#         print(listA[i],"great")
#         print(listA[i-1],"less")
#         break
# listA = [9.5]
# x = listA[0]
# print(str(x))
# c= str(x)
# print(type(c))
# Given list
# listA.sort()
# print("Given list : \n", listA)
# res = [ele for ele in listA]
# d =len(res)
# print(d)
# # Result
# print("Final list: \n",res)
# for ele in listA:
#     print(ele)

# list_of = res
# print(list_of)

# a=[72.73]
# list_of = res
# list_of.sort()
# len_of=len(list_of)
# print(len_of)
# for i in range(len_of):
#     if list_of[i]<a:
#         print(list_of[i],"less")
#         print(list_of[i-1],"great")
#         break

# # list items


# c.sort()
            # print("Given list : \n", c)
            # res = [ele for ele in c]
            # d =len(res)
            # print(d)
            # # Result
            # print("Final list: \n",res)
            # for ele in c:
            #     print(ele)

            # list_of = res
            # print(list_of)

            # a=list(get_ppv_invoiceprice)
            # list_of = res
            # list_of.sort()
            # len_of=len(list_of)
            # print(len_of)
            # for i in range(len_of):
            #     if list_of[i]<a:
            #         print(list_of[i],"less")
            #         print(list_of[i-1],"great")

# a =int(input("enter a:"))
# b= int(input("enter b:"))
# c = a+b
# d = a-b
# e = a*b
# f = a/b
# print("add of:",c)
# print("add of:",d)
# print("add of",e)
# print("add of",f)

# q=['Q5', 'Q6', 'Q7', 'Q8', 'Q1', 'Q2', 'Q3', 'Q4', 'QTD', 'Q5', 'Q6', 'Q7', 'Q8', 'Q1', 'Q2', 'Q3', 'Q4', 'QTD']
# v= [49.6157, 49.6157, 53.657, 59.0227, 62.1, 60.31, 58.03, 52.227, 58.03, 49.6157, 49.6157, 53.657, 59.0227, 62.1, 60.31, 58.03,
# 52.227, 58.03]

# q.sort()
# # print(q)
# b=[[9.5], [9.5], [9.5], [9.5]] 
# a=[2.4]
# for a in b:
#     print(a)

# # d = float(a)
# b=[2.4]
# c=[3.2]
# a = [[9.5], [9.5], [9.5], [9.5]] 

# a=[1,3,2,4,2,3,2,3,2,5,3,1,3]
# b = set(a)
# print(b)
# c= list(b)
# print(c)


# [('Source Discrepancy,Blended Std Cost,Supplier Discrepancy,Supplier Discrepancy',), ('Source Discrepancy,Blended Std Cost,Supplier Discrepancy,Supplier Discrepancy',)]

# d = "Source Discrepancy,Blended Std Cost,Supplier Discrepancy,Supplier Discrepancy"
# x = d.split(",")
# print(x)

# s=['No Discrepancy', 'Supplier Discrepancy', 'Supplier Discrepancy']
# d=set(s)
# print(d,"ddddd")

# s = {'Supplier Discrepancy', 'Source Discrepancy','Source Discrepancy','Blended Std Cost','Supplier Discrepancy','Supplier Discrepancy'} 
# for i in s:
#     print(i)

# v = ['Source Discrepancy,Blended Std Cost,Supplier Discrepancy,Supplier Discrepancy', 'Source Discrepancy,Blended Std Cost,Supplier Discrepancy,Supplier Discrepancy']
# for i in v:
#     print(i)
#     x = i.split(',')
#     print(x)
#     s=set(x)
#     print(s)
#     d = {'Source Discrepancy', 'Blended Std Cost', 'Supplier Discrepancy'}
#     for i in d:
#         print(i)
#     ty ={'Supplier Discrepancy', " 'Source Discrepancy'}", "{'Blended Std Cost'", " 'Supplier Discrepancy'"}
#     s=ty.split(" \" ")
#     print(s)

# d = "12-02-2002"

# date_string = "2023-02-12 00:00:00"
# print(date_string,"yyy")
# x= date_string[:10]
# print(x,'xxxx')
# r = 
# x = d.split('-')
# j =  ('-'.join(x))
# print(j,x,d)
# x = o.split('\'')
# print(x)


# print(1+  2.2)


#  chatgpt
# name = "Sneha"
# years=4
# goal = "Become a Django Web Developer"
# print("Name:", name)
# print("Experience:", years, "years")
# print("Goal:", goal)

# years = 4
# if years>=3:
#     print("Eligible for Django Developer")
# else:
#     print("Need more practice")

# for i in range(1,20):
#     if i%3 == 0:
#         print(i)

# def functname(argu):
#     print("def func : ", argu)
# functname('python function')

# def add_task(task_name):
#     print("Task added:", task_name)

# add_task("Learn Django")
# add_task("Practice Python")
