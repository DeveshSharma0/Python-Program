                               #Problem_01

#  # check whether the given number is even or odd using function

# def num():
#     n = int(input("Enter the number: "))
#     if n%2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")
#     return n

# user_input = num()
# print(user_input)


                                 #Problem_02    

# # check whether the given number is prime or not using function

# def prime():
#     n = int(input("Enter the number:"))

#     if n <= 1:
#         print(n, "is not a prime number")
#         return

#     for i in range(2, n):
#         if n % i == 0:
#             print(n, "is not a prime number")
#             return
#     print(n, "is a prime number")
# prime()


                               #Problem_03

# # Write a Program to print the patten of tingle using function 

# def line():
#     line = int(input("Enter the number of lines: "))
#     for i in range(1, line + 1):
#         for j in range(i):
#             print("*", end="")
#         print()     
#     return f"now this is a pattern of line:{line}"
# user_input = line()
# print(user_input)


                                        #Problem_04

#Write a function called demo() that accepts two parameters: a name and an age. The function should print these values directly to the console

# def demo(name,age):
#     print(f"My name is {name} and I am {age} years old.")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# demo(name, age)

                                        #Problem_05

# #Create a function func1() such that it can accept a variable number of arguments and print all of them. Whether you pass two numbers or five, the function should handle them all without error.

# def func1(*args):
#     print("Printing value:")
#     for arg in args:
#         print(arg) 

# func1(20,40,60)
# func1(80,100)

                                 #Problem_06

# #Write a function calculation() that accepts two variables and calculates both addition and subtraction. The function must return both results in a single return statement.

# def calculation(a ,b):
#     addition = a + b
#     sub = a - b
#     return addition, sub

# res = calculation(10, 5)
# print(res)


                                # Problem_07

# # Function with Default Argument

# def city(name = "Delhi"):
#    print(f"The city name is {name}")
# city("Mumbai")
# city()

                                # Problem_08

# # Function with Keyword Argument
# def person(name, age):
#     print(name, age)
# person(name="Alice", age=30)

                                # Problem_09

# # Function with Variable-length Argument

# def sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# result = sum(1, 2, 3, 4, 5)
# print(result)


                            # Problem_10

# #Create an Inner Function

# def outer(a ,b):

#     def add(a ,b):
#         return a + b
#     sum = add(a, b)
#     return sum + 5

# result = outer(10, 20)
# print(result)

                                #Problem_11
#Create a Recursive Function

# def add(n):
#     if n == 0:
#         return 0
#     else:
#         return n + add(n - 1)
# result = add(5)
# print(result)   


                                #Problem_12

#Assign a Different Name to Function and Call It

# def dev(name,age):
#     print(f"My name is {name} and I am {age} years old.")

# demo  = dev 
# demo("devesh" , 25 )


                             #Problem_13

# def my_fruits(fruits):
#     for i in fruits:
#         print(i)

# my_fruit = ["apple", "Banana","charry"]
# my_fruits(my_fruit)


                              #problem_14
# def name():
#  return ["apple","banana","charry"]

# new = name()
# print(new[0])
# print(new[1])
# print(new[2])


                               #Problem_15
# def my_function(name, /):
#     print("hello",name)

# my_function("dev")

                            #Problem_16

# def name(name,*ok):
#     print(name , *ok)

# new = [21,1,1,1,1,]
# name(new)


# def name(name, **now):
#     print(name, *now)

# new ={
#     "dev" : "sharma",
#     "ok" : "okkk",
#     "mm" : "qq"
# }
# name(new)

                             #Problem_17

# def my_function(username , **details ):
#     print("username : ",username)
#     print("other details")

#     for key , value in details.items():
#         print(" ",key + ":" , value)

# my_function("emil123" , age = 25 , city = "delhi")














