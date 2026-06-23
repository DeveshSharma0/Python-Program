
### ............Exception Handling ...............####

# try:
#     print(x)
# except:
#     print("An exception occurred")

### ..........Many Exceptions ..........####

# try:
#     print(x)
# except NameError:
#     print("variable x in not define")
# except:
#     print("something else went wrong")

# try:
#     print("devesh")
# except NameError:
#     print("variable x in not define")
# except:
#     print("something else went wrong")


##### ..........Finally ............. ####

# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("the 'try except' is finished")


# try:
#     f = open("demo.txt")
#     try:
#         f.write("lorem ipsum ")
#     except:
#         print("Something went wrong when writing to the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong when opening the file")


#### .................Raise an exception...............###


# x = -1

# if x < 0:
#     raise Exception("sorry")


###3 Raise a TypeError if x is not an integer:

# x = "hello"

# if not type(x) is int:
#     raise TabError("only interger are allow")

