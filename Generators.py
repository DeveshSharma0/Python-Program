#simple generator

# def my_Genrator():
#     yield 1
#     yield 2
#     yield 3

# for value in my_Genrator():
#   print(value)

"""................................................................"""

#yeald Keyword ......

# def count_up(n):
#     count = 1
#     while count <=n:
#         yield count
#         count += 1 

# for num in count_up(6):
#   print(num)

"""................................................................"""

# def large(n):
#     for i in range(n):
#         yield i

# gen = large(100)

# print(next(gen))
# print(next(gen))
# print(next(gen))               #Frist type to run
# print(next(gen))

# for j in gen:                  # second type to run
#     print(j)

"""................................................................"""

# def  simple():
#     yield "dev"
#     yield "mohan"
#     yield "devesh"

# gen = simple()

# print(next(gen))
# print(next(gen))
# print(next(gen))


"""................................................................"""
                                              # Generator Expresion

# total = sum(x*x for x in range(10))
# print(total)


# list_comp = [x*x for x in range(5)]
# print(list_comp)                   # list return


# gen_exp = (x * x for x in range(5))
# print(gen_exp)                          #address return 
# print(list(gen_exp))             #list return

"""................................................................"""

###generate 100 Fibonacci number.........

# def fibonacci():
#   a, b = 0, 1
#   while True:
#     yield a
#     a, b = b, a + b

# # Get first 100 Fibonacci numbers
# gen = fibonacci()
# for _ in range(100):
#   print(next(gen))

"""................................................................"""

####send() mehord......

# def echo_generator():
#     while True:
#         received = yield
#         print("received :",received)

# gen = echo_generator()
# next(gen)
# gen.send("hello")
# gen.send("world")

"""................................................................"""

# def my_gen():
#     try:
#         yield 1
#         yield 2 
#         yield 3
#     finally:

# print("Generator close")
# gen = my_gen()
# print(next(gen))
# gen.close()
    














