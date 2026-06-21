# Recursicion.....
# base case which mens don't create a infinite loop 

# def countdown(n):
#     if n <= 0:
#         print("done!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)

## base case recursive case

# def factorial(n):
#     #base case
#     if n == 0 or n == 1:
#         return 1 
#     #recursive case
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


              # progran_1

# ## fibonacci sequence
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:               #6               #5
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))

              #Program_2

#Recursion with Lists sum element all

# def sum_list(n):
#     #base case
#     if len(n) == 0:
#         return 0
#     else:
#         #recursion case
#         return n[0] + sum_list(n[1:])

# my_list = [1,2,3,4,5]
# print(sum_list(my_list))


                #program_3

#max find with recursicion function

# def find_max(n):
#     if len(n)==1:     #base case
#         return n[0]
#     else:
#         max_of_rest = find_max(n[1:])    # recursicion case
#         return n[0] if n[0] > max_of_rest  else  max_of_rest 

# my_list = [1,2,9,4,5,6]
# print(find_max(my_list))

                               #program_4

# import sys
# sys.setrecursionlimit(300)
# print(sys.getrecursionlimit())

           



