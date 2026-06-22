###iterator with Generators......

##iterator which means access the value in one by one ...


##now create a list

# myTuple = ("baba","apple","sun","mango")
# myit = iter(myTuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

#accessing word in latter  one by one...

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

#Looping Through an iterator.......
# The for loop actually creates an iterator object and executes the next() method for each loop.

# word = "banana"
# for i in word:
#     print(i)

              #####  create a iterator   ######


# class myNumber:
#     # accessing value one by one 

#     def __iter__(self):
#         self.a = 1
#         return self
    
# #Next object provide a next value

#     def __next__(self):
#         x = self.a               
#         self.a += 1     #incressing value
#         return x

# myClass = myNumber()        #coll function 
# myiter = iter(myClass)      # create  iterabale


# print(next(myiter))
# print(next(myiter))               # create object in memory address 
# print(next(myiter))


                ###### stopIterable ######

# class myNum:
#     def __iter__(self):

#         self.a = 1
#         return self

#     def __next__(self):

#         if self.a <= 20:
#             x = self.a
#             self.a +=1
#             return x
#         else:
#             raise StopIteration

# myClass = myNum()
# myiter = iter(myClass)

# for x in myiter:
#     print(x)






