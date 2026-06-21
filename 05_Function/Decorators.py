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


def changeCase(n):
    def changeCase(fun):
        def myInner():
            if n == 1:
                a = fun().lower()
            else:
                a = fun().upper()
            return a
        return myInner
    return changeCase

    #Use case.......

@changeCase(1)
def myFunction():
    return "hello os "

print(myFunction())



                            # Program_5

# multypal Decorator.....

def changeCase(fun):
    def myInner():
        return fun().upper()
    return myInner

def add(fun):
    def myInner():
        return "hello " + fun() + " have a good day!"
    return myInner

    

@changeCase
@add
def myFunction():
    return "devesh"
print(myFunction())
