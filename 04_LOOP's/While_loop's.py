                                        #Program_01

#Write a Python program to print the square of all numbers from 0 to 10.

# i = 0
# while i <= 10:
#     print(i ** 2, end=" ")
#     i += 1

                                            #Program_02 

#Write a Python program to print the cube of all numbers from 0 to 10.
# i = 0
# while i <= 10:
#     print(i ** 3, end=" ")
#     i += 1

                                            #Program_03

#Write a Python program to print the all num of all numbers from 0 to a given number.|cube z,square 4,5,6,7 or any num. multiply of all num from 0 to a given number.


# input_number = int(input("\nEnter a number: "))
# num = int(input("Enter a number: "  ))
# i = 0
# while i <= input_number:
#     print(i**num, end=" ")
#     i += 1

                                            #Program_04

#Write a Python program to print the multiplication table of a given number.
# input_num = int (input("Enter a number: "))
# i = 1 
# while i <=10:
#     mul = input_num * i
#     print(f"{input_num} x {i} = {mul}")
#     i += 1

                                            #Program_05

#Write a Python program to calculate the factorial of a given number.
# input_num = int(input("Enter a number: "))
# factorial = 1
# i = 1
# while i <= input_num:
#     factorial  = factorial * i
#     i += 1  
# print(f"The factorial of {input_num} is: {factorial}")

                                         # Program_06

# write a program to print numbers from 10 to 15 using while loop.

# i = 10
# while i <= 15:
#     print(i, end=" ")
#     i += 1

                                     # Program_07

#write a program to print the even or odd number using while loop.

# input_num = int(input("Enter a number: "))
# i = 0
# while i <= input_num:
#     if i % 2 != 0:
#         print("odd number: ", i)
#     i += 1

                                   #Program_08

#write a Program to calculate the Product of number from 1 to 5 using 1 while loop.

# product = 1
# num = 2
# while num<=5:
#     product = product * num
#     num += 1    
# print("The product of number from 1 to 5 is: ", product)



                                  # Program_09

#write a program to reverse each word in the sentence "Hello World" using while loop.
# sentence = "Hello World"
# words = sentence.split()
# i = 0
# while i < len(words):
#     word = words[i]
#     print(word[::-1], end=" ")
#     i += 1


# sentence = input("Enter a sentence: ")
# words = sentence.split()
# for word in words:
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i], end="")
#         i -= 1
#     print(end="")
    
                                 #Program_10

# write a program to count the number of consonants in a given string using while loop.
# sentence = input("Enter a string: ")
# vowel = "aeiou"
# consonants = 0
# i = 0
# while i < len(sentence):
#     if sentence[i] not in vowel and sentence[i].isalpha():
#         consonants += 1
#     i += 1
# print("The number of consonants in the string is: ", consonants)


                                   #Program_11

# write a program to count the number of vowel in a given string using while loop.

# sentence = input("Enter a string: ")
# consonants = "bcdfghjklmnpqrstvwxyz"
# vowel = 0
# i = 0
# while i < len(sentence):
#     if sentence[i] not in consonants and sentence[i].isalpha():
#         vowel+= 1
#     i += 1
# print("The number of vowel in the string is: ", vowel)

                                       #Program_12

# write a program to print the first 5 multiples of 3 using while loop.
# multiple = 3
# count = 1
# while count <= 5:
#     print(multiple,end=" ")
#     multiple += 3
#     count += 1


                                  #Program_13

#write h program to calculate 3 to the power of 4 using while loop.

# base = 3
# exponent = 4
# result = 1
# i = 1
# while i <= exponent:
#     result *= base
#     i += 1
# print(f"{base} to the power of {exponent} is: {result}")

                               #Program_14

#write a program to check if a given number ,such as 16,is a perfect square using while loop.
# number = int(input("Enter a number: "))
# i = 0
# while i * i < number:
#     i += 1
# if i * i == number:
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")


# number = int(input("Enter a number: "))
# i = 0
# is_perfect_square = False
# while i * i <= number:
#     if i * i == number:
#         is_perfect_square = True
#         break
#     i += 1
# if is_perfect_square:
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")


                             #Program_15

#write a program to find the greatest common divisor (GCD) of two numbers using while loop.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# while num2:
#     num1, num2 = num2, num1 % num2  
# print(f"The greatest common divisor (GCD) of the two numbers is: {num1}")
  

                                        #Program_16

#write a program to count occurrences of a specific character in a given string using while loop.
# sentence = input("Enter a string: ")
# character = input("Enter a character to count: ")
# count = 0
# i = 0
# while i < len(sentence):
#     if sentence[i] == character:
#         count += 1
#     i += 1
# print(f"The character '{character}' occurs {count} times in the string.")


                                                 #Program_17
#now using nested while loop
# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# i = 0
# while i < len(num1):
#     j = 0
#     while j < len(num2):
#         print(num1[i], num2[j])
#         j +=1
#     i +=1

                                                #Program_18
#Write a program to print the multiplication table of a given number using nested while loop.
# number = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(f"{number} x {i} = {number * i}")
#     i += 1

# #reverse the multiplication table
# j = 10
# while j >= 1:
#     print(f"{number} x {j} = {number * j}")
#     j -= 1

                                                  #Program_19

# Write a program to using triple nested while loop

# num1 = [ 1, 2, 3, 4, 5]
# num2 = [ 6, 7, 8, 9, 10]
# num3 = [11, 12, 13, 14, 15]
# i = 0
# while i < len(num1):
#     j = 0
#     while j < len(num2):
#         k = 0
#         while k < len(num3):
#             print(num1[i], num2[j], num3[k])
#             k += 1
#         j += 1
#     i += 1


                                               # Program_20
# print('''\n-------------------------------------------------
# |        S E A R C  H  I T E M  IN  L I S T       |
# --------------------------------------------------''')

# num = int(input("Enter a number to search in the list: "))
# item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i <= len(item):
#     try:
#         if item[i] == num:
#             print(f"{num} is found in the list.")
#             break
#     except IndexError:
#         print(f"{num} is not found in the list.")
#         break       
#     i += 1




        