# f = open("dev.txt" ,"x")     # Create  a New_File 

# f = open("dev.txt","rt")
# print(f)

####.......................Reade File.................#

# f = open("dev.txt")           #file reade 
# print(f.read())

##...............Using the with statement............#

# with open("dev.txt") as f:
#     print(f.read())

##................close Files...............##

# f = open("dev.txt")
# print(f.readline())              # agar line read kre to 
# f.close()               #us file ko close kar deta h 

##..................Read Only Parts of the File................##

# with open("dev.txt") as f:
#     print(f.read(5))
    

## .............Read Lines........##

# with open("dev.txt") as f:        #read line only one line 
#     print(f.readline())


# with open("dev.txt") as f:        #read line multi line 
#    print(f.readline())
#    print(f.readline())
#    print(f.readline())


# with open("dev.txt") as f:
#     for i in f:                      # access element for loop with file extrect
#         print(i)


##.....................Python File Write......................#

# with open("dev.txt","a") as f:
#     f.write("this is all name is Row agent name .....")          # write a text in file 



###..................Overwrite Existing Content..................##

# with open("dev.txt","w") as f:
#     f.write("Not a row agent ,itd a normal peaple....")

# with open("dev.txt") as f:
#     print(f.read())


###...................Create a New File...............>###

# f = open("demo.txt","x")
    


###...................Delete a File............#

# import os

# # os.remove("demo.txt")               # delite file 


# if os.path.exists("dev.txt"):
#     os.remove("dev.txt")
# else:

#     print("This file not exit in your computer")

# os.rmdir("dev")






