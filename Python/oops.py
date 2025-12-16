# what and why oops
# oops = object oriented programming system
# it is a programming paradigm that uses objects and classes in programming.
# it aims to implement real-world entities like inheritance, polymorphism, encapsulation, etc. in the programming.
# it allows us to structure our software in a way that is easy to manage and maintain.
# it helps in code reusability and modularity.
# some important terms in oops:
#  self, str, int, del, return, none, init, class, object, method, function,
# instance, inheritance, parent class, child class, polymorphism, encapsulation, abstraction
# self : it is used to represent the instance of the class. It binds the attributes with the given arguments.
# str : it is used to represent the string data type.
# int : it is used to represent the integer data type.
# del : it is used to delete the reference of an object.
# return : it is used to exit a function and return a value.
# none : it is used to represent the absence of a value or a null value.
# init : it is a special method that is called when an object is instantiated.  It is used to initialize the attributes of the class.
# class : it is used to define a class in Python.
# object : it is an instance of a class.
# method : it is a function that is defined inside a class and is used to perform operations on the attributes of the class.
# function : it is a block of code that performs a specific task.
# instance : it is an individual object of a class.
# inheritance : it is a mechanism that allows a class to inherit attributes and methods from another class.
# parent class : it is the class from which attributes and methods are inherited.
# child class : it is the class that inherits attributes and methods from the parent class.
# polymorphism : it is the ability of a function or method to behave differently based on the object that it is acting upon.
# encapsulation : it is the mechanism of restricting access to some components of an object and preventing the accidental modification of data.
# abstraction : it is the process of hiding the implementation details and showing only the essential features of the object.


# class car:
#     engine = "petrol"
#     mailage = 10
#     tires = 4
#     seats = 5
#     color = "red"
#     def moveforward(self):
#         print("forward")
#     def movebackward(self):
#         print("backward") #(return not mention so it will return none)

# car1 = car()  
# # print(car1.color)
# car2 = car()
# # print(car2.color)
# car2.color = "blue"
# print(car2.color)
# print(car1.movebackward())
# print(car1.moveforward())

# exercise:
# class Bank_Accoount():
#     Customer_name = ""
#     Bank_Accoount = 0
#     Balance = 0 

# account1 = Bank_Accoount()
# account1.Customer_name ="Sneha"
# account1.Balance = 1000
# account1.Bank_Accoount = 123456
# # print(account1.Customer_name, account1.Bank_Accoount, account1.Balance)


# # constructor
# # non parameterized constructor
# class family():
#     def __init__(self):
#         self.father = "KondappaKumareshan"
#         self.mother = "Murugaswari"
#         self.sister = "Hemalatha"
#         self.myself = "Sneha"

# myfamily = family()
# print(myfamily.father, myfamily.mother,myfamily.sister,myfamily.myself)
# # parameterized constructor
# class family1():
#     def __init__(self, father, mother, sister, myself):
#         self.father = father
#         self.mother = mother
#         self.sister = sister
#         self.myself = myself

#     def __del__(self):
#         print("Destructor called, family object deleted.")
    
#     def __str__(self):
#         return f"Father: {self.father}, Mother: {self.mother}, Sister: {self.sister}, Myself: {self.myself}"

# husbundfamily = family1("Ravichandran", "Thangamani", "Prakash", "Prabhakaran")

# print(husbundfamily)  # This will call the __str__ method
# del husbundfamily  # This will call the __del__ method
# print(husbundfamily)  # This will raise an error since the object is deleted

# print input data and name constructor
# exercise:
# class Bank_Accoount():
#     def __init__(self,name,account,balance):
#         self.Customer_name = name
#         self.Bank_Account = account
#         self.Balance = balance
#     def __str__(self):
#         return (self.Customer_name)
# account1 = Bank_Accoount("prabha", 123123, 10000000000000)
# print(account1.Customer_name,account1.Balance,account1.Bank_Account," new member details and his name is", account1)


# Encapsulation
# class car:
#     def __init__(self,carname,tires,sheet,speed):
#         self.__carname = carname
#         self.tires = tires
#         self.sheet = sheet
#         self.__speed = 200
    
#     def get_speed(self):
#         return  self.__speed 
    
#     def set_speed(self, value):
#         if value < 0:
#             print("Speed negative ah iruka kudathu ❌")
#         else:
#             self.__speed = value

# car1 = car("BMW", 4, 5, 170)

# print(car1.get_speed())
# car1.set_speed(130)
# print(car1.get_speed())

# Inharitance

# class vehicle:
#     no_of_airbags = 2
#     def carname(self):
#         return ("Volvo")

# class car(vehicle):
#     no_of_wheel = 5

# car1 = car()
# print(car1.no_of_wheel)
# print(car1.no_of_airbags)
# print(car1.carname())

# 4 types off inhertitance 
# multiple inheritance
# multi-level inheritance
# single inheritance 
# hierarchical inheritance


# class father:
#     hair_color = 'black'
# class mother:
#     hair_color = 'brown'
#     def music(self):
#         print("Melody songs!")

# class child(father,mother):
#     no_of_legs = 2

# Child = child()
# Child.music()

# polimarpism
# ruuntime and compile time polymorphism
# compile time polymorphism

class addition():
    def summ(self,*args):
        print(args)
        i = 0
        for i in args:
            print(i,"dhfdgfhdgf")
            i = i + i
            return i
            
# addition1 = addition()
print(addition().summ(12,4,3,5,6,0))
