                               #Problem_01

#  # check whether the given number is even or odd using function

# def num():
#     n=int(input("Enter the number: "))
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

