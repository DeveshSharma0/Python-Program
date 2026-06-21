# def changeCase(fun):
#     def MyInner():
#         return fun().upper()
#     return MyInner


# # @changeCase

# # def myFunction():
# #     return "Hello sally"
# # print(myFunction())


# @changeCase
# # name = input("Enter the number ")
# def dev():
#   ok = input("Enter the number")
#   return ok
# print(dev())


                               #Program_2

# def changeCase(fun):
#     def myInner(x):
#         return fun(x).upper()
#     return myInner


# @changeCase
# def myFunction(naam):
#     return "hello" + naam

# print(myFunction(" devesh sharma"))



                            #Programm_3


# def changeCase(fun):
#     def myInner(*args, **kwargs):
#         return fun(*args, **kwargs).upper()
#     return myInner

# @changeCase

# def myFunction(naam ,*m):
#     return "Helloo" + naam
    

# print(myFunction("devesh"))


                          #Program_4

  # decorator with argument



                            # Program_5

#test code ....

# def myFunction(fun):
#     def myInner(x):
#         dev = "hello" ,fun(x)
#         return dev
#     return myInner

# def decorator(fun):
#     def date(y):
#         return fun(y)
#     return date


# @myFunction
# def myFun(name):
#     return name

# @decorator
# def Tarek(num):
#     return num

# print(Tarek("3/3/3000" ))
# print(myFun("devesh"))



                                         #program_6
#Presrving Function Matadata

def myFunction():
    return "have a great day"

## attributes........

# print(myFunction,__name__)
# print(myFunction.__doc__)
# print(myFunction.__code__)
# print(myFunction.__defaults__)
# print(myFunction.__dict__)
# print(myFunction.__kwdefaults__)
# print(myFunction.__module__)


                               # Program_7

#decoator with Presevering function matadat 

# def myFunction(fun):
#     def myInner():
#         return fun().upper()
#     return myInner

# @myFunction

# def changeCase():
#     return "have a good Day"

# print(changeCase.__name__)


                                         # Program_8
# functools.wraps use case in decorator .....

# import functools

# def changeCase(func):

#     @functools.wraps(func)
#     def myInner():
#         return func().upper()
#     return myInner


# @changeCase
# def myFunction():
#     return "have a Good day"

# print(myFunction.__name__)



