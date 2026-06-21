#lamda argument : Expression

                         #X = the is a functoion
# x = lambda a :a+10        #a= perameter 

# print(x(5))                # x() = return statement


# dev = lambda name: name
# print(dev("devesh"))


# x = lambda a,b,c,: a+b+c
# print(x(2,3,5))

                       #Program_1

#now func take one argument and that argument will be multiplied with an unknown number

# def myFun(n):
#     return lambda a : a*n

# dev = myFun(7)
# print(dev(2))

                         #Program_2

# def myFub(n):
#     return lambda a : a * n

# one = myFub(1)
# five = myFub(5)

# print(one(2))
# print(five(7))


                              # Program _3

# lambda with built-in-functions map() , filter(), sorted() ......\\

# a = [1,2,3,4,5,6]
# double = list(map(lambda x : x*2 ,a))  #map means sbhe ko lega , this is function map()
# print(double)


# a = [1,2,3,4,5,6]
# odd = list(filter(lambda x : x % 2  != 0 , a))
# print(odd)


# a = [("dev" , 39),("mohan" , 2 ),("sachin",23)]
# sorted_student = sorted(a  , key = lambda x : x[1])
# print(sorted_student)



