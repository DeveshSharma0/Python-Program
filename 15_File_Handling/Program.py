                             #Program_1

##Write a Python program that accepts a user’s name as input and writes it to a file called user.txt.

# name = input("Enter the name : ")
# with open("user.txt","w") as f:
#     f.write(name)
# print("Name written to user.txt")


                             #Program_2

## Write a Python program that opens a file called data.txt and prints its entire contents to the console.

# with open("user.txt","r") as f:
#     content = f.read()
#     print(content)

                            #program_3

## Write a Python program that reads a file called lines.txt and prints each line one at a time using a loop.

# with open("user.txt","r") as f:
#     for line in f:
#         print(line)

                           #program_4

## Write a Python program that reads all lines from a file called items.txt into a list and prints the list.


# with open("user.txt","r") as f:
#     line = f.readline()

# print(line)


                          #Program_5

## Write a Python program that appends the sentence This is a new line. to an existing file called notes.txt without overwriting its current content.

# with open("user.txt","a") as f:
#     f.write("\nThis is a row agent")

# print("successfully added text in your file")


                        #Program_6

## Write a Python program that clears all content from an existing file called temp.txt, leaving it as an empty file.

# with open("temp.txt", "w") as f:
#     pass

# print("File content cleared.")


                             #Program_7
## Write a Python program that creates a new file called output.txt and writes three lines of text to it.

# lines = ["devesh\n","sharma\n","mohit\n",]

# with open("output.txt","w") as f:
#     f.writelines(lines)
# print("Text written to output.txt")

                        #Program_8

## Write a Python program that checks whether a file called data.txt exists in the current directory and prints an appropriate message based on the result

# import os
# if os.path.exists("output.txt"):
#     print("file exits..")
# print:print("file does not exit")

                                 #Program_9

## Write a Python program that attempts to open a file called missing.txt and gracefully handles the case where the file does not exist using a try-except block.

# try:
#     with open("output.txt","r") as f:
#         content = f.read()
#         print(content)

# except FileNotFoundError:
#     print("Error : The filewas not found.")


                                 #Program_10

## Write a Python program that opens a file called data.txt and counts the total number of lines it contains.

# with open("user.txt", "r") as f:
#     lines = f.readlines()

# print("total line:",len(lines))



                                    #Program_11

##  Write a Python program that reads a file called data.txt and counts the total number of words across all its lines.

# with open("user.txt", "r") as f:
#     content = f.read()

# words = content.split()
# print("Total words:", len(words))


                                   #Program_12

### Write a Python program that reads a file called data.txt and counts the total number of characters it contains, including spaces and newlines.

# with open("user.txt","r") as f:
#     content = f.read()

# print("Total char :",len(content))


                                       #program_13
## Write a Python program that reads a file called data.txt and counts how many times the word Python appears in it.

# word = "devesh"
# with open("user.txt","r")as f:
#     content = f.read()

# count = content.count(word)
# print(f"occurrences of '{word}' :",count)


                                       #Program_14

## Write a Python program that reads and prints only the first 3 lines from a file called data.txt.

# n = 3
# with open("user.txt","r") as f:
#     for i, line in enumerate(f):
#         if i >= n:
#             break
#         print(line, end="")


                                        #Program_15

## Write a Python program that reads and prints only the last 3 lines from a file called data.txt
# n = 3
# with open("user.txt","r")as f:
#     lines = f.readline()

# for line in lines[-n:]:
#     print(line , end="")

                                     



