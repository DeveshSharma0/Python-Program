#  ##  Frist self write a code in oop with python........... 

# class dev:
#     def __init__(self,name,age,year):
#         self.name = name
#         self.age = age
#         self.year = year

# name = dev("devesh",24,2001)

# print(f"my Name is '{name.name}'\n my age is '{name.age}'\nNow year is : {name.year}")

####-----------------------------------------------------------------------------------------------------------------------###

# class data:
#     def __init__(self,name,clas,Branch,roll_No):
#         self.name = name
#         self.clas = clas
#         self.Branch = Branch
#         self.roll_No = roll_No
        
       
# a = input("Enter the name :")
# b = input("Enter the clas :")
# c = input("Enter the Branch :")
# d = input("Enter the Roll_No :")

# info = data(a,b,c,d)
# print("........Student Details.........")
# print(f"Name : {info.name},\n Clas : {info.clas},\n branch : {info.Branch},\n Roll_No : {info.roll_No},")
            
####-----------------------------------------------------------------------------------------------------------------------###


# class Person:
#     def __init__(myobj,name,age):
#         myobj.name = name
#         myobj.age = age

#     def greet(abc):
#         print("hello, My Name Is " + abc.name)

# p1 = Person("devesh",23)
# p1.greet()

####-----------------------------------------------------------------------------------------------------------------------###

### modify concept....... add , del

### change value.......

# class person:
#     def __init__(self, name ,age,room):
#         self.name = name
#         self.age = age
#         self.room = room

# p1 = person("devesh",24 ,"b.tech")
# p1.age = 16
# p1.room = "------"
# p1.name = "------"
# print(p1.name)
# print(p1.age)
# print(p1.room)


###delete value ..............

# class person:
#     def __init__(self, name ,age,room):
#         self.name = name
#         self.age = age
#         self.room = room
# p1 = person("devesh",24 ,"b.tech")
# del p1.room               ###...............##
# print(p1.name)
# print(p1.age)
# print(p1.room)

### add item value ...............

# class person:
#     def __init__(self,name):
#         self.name = name
# p1 = person("Tobias")
# p1.age = 23
# p1.room = "b.tech"
# print(p1.name)
# print(p1.age)
# print(p1.room)


####-----------------------------------------------------------------------------------------------------------------------###

                            ### Methord 
### --------------##
# class person:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"my name is " + self.name)

# p1 = person("devesh")

# p1.greet()

### -------Methods with Parameters-------##

# class calculator:
#     def add(self, a, b):
#         return a + b

#     def multiply(self, a, b):
#         return a * b

# calc = calculator()

# print(calc.add( 8, 5 ))
# print(calc.multiply( 4, 8 ))

### -------Methods Modifying Properties-------###

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1                     ## increase age every coll
#     print(f"Happy birthday! You are now {self.age}")

# p1 = Person("Linus", 25)
# p1.celebrate_birthday()    
# p1.celebrate_birthday()
# p1.celebrate_birthday()      #coll age 

### --------------##
### ------The __str__() Method--------##

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name} ({self.age})"

# p1 = Person("Tobias", 36)
# print(p1)

### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###

                                              ##-> inharitance  <-##

# class person:
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(self.name,self.age)

# class student(person):
#     pass

# x = student("Devesh sharma ", 24 )
# x.info()


###--------------------------------------------------###

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()

###--------------------------------------------------###

### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
                  
                                    ###   Python Polymorphism    ###

# class Vehicle:   ##invariance
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):##Polymorphism
#     print("Move!")

# class Car(Vehicle):## inheritance
#   pass

# class Boat(Vehicle):## inheritance
#   def move(self):##Polymorphism
#     print("Sail!")

# class Plane(Vehicle):## inheritance
#   def move(self):##Polymorphism
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

### -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
###-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------###
                                   ###-> Python Encapsulation <-##

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age    # private

#     def get__age(self):
#         return self.__age

# p1 = person("devesh sharma" , 25)
# print(p1.get__age())

###----------------------------------------------------##


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(26)
# print(p1.get_age())

###----------------------------------------------------###

# class student:
#     def __init__(self,name):
#         self.name = name
#         self.__grade = 0

#     def set_grade(self,grade):
#         if 0 <= grade <= 100 :
#             self.__grade = grade

#         else:
#             print("Grade must be between 0 and 100")

#     def get_grade(self):
#         return self.__grade 

#     def get_status(self):
#         if self.__grade >= 100:
#             return "passed"
#         else:
#             return "Failed"

#     student = student("devesh")
#     student.set_grade(82)
#     print(student.get_grade())
#     print(student.get_status())

        
















    











