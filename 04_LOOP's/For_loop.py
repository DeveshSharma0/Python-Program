                                #Program_01

#write h program to print 1 to 10 using for loop
# for i in range(1,11):
#     print(i)

                                #Program_02 

# write a Program to print square of first 10 natural number using for loop
# for i in range(1,11):
#     print(i**2 , end=" ")

                                #Program_03

# write a program to print multiplication table of 5 using for loop
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

          # # Reverse of a number using for loop
# num = int(input("Enter a number: "))
# for i in range(10 ,0,-1):
#     print(i * num, end=" ")


                                #Program_04

#even number from 1 to 20
# for i in range(1,21):
#     if i%2==0:
#         print(i , end=" ")

                                #Program_05

#odd number from 1 to 20
# for i in range(1,21):
#     if i%2!=0:
#         print(i , end=" ")

                               #Program_06

# Write a program to using triple nested for loop

# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9,10]
# num3 = [11,12,13,14,15]
# for i in range(len(num1)):
#     for j in range(len(num2)):
#         for k in range(len(num3)):
#             print(num1[i], num2[j], num3[k])

                                #Program_07

##write a program to count occurrences of a specific character in a given string using while loop.

# sentence = input("Enter a string: ")
# character = input("Enter a character to count: ")
# vowel_count = 0
# for char in sentence:
#     if char in 'aeiouAEIOU':
#         vowel_count += 1
# print(f"The number of vowels in the string is: {vowel_count}")

                                            #Program_08

##write a program to reverse each word in the sentence "Hello World" using for loop.

# sentence  = "Hello World"
# words = sentence.split()
# for word in words:
#     print(word[::-1], end=" ")

                                           #Program_09

#write a Program to calculate the Product of number from 1 to 5 using 1 for loop.

# product = 1
# for i in range(1,6):
#     product *= i
# print(f"The product of numbers from 1 to 5 is: {product}")

                                          #Program_10

#write a program to print the first 10 Fibonacci numbers using for loop.

# a = 0
# b = 1
# print("Fibonacci sequence:")
# for i in range(10):
#     print(a, end=" ")
#     a = b
#     b = a + b

                                        #Program_11

#write a program to print the first 10 prime numbers using for loop.

# print("Prime numbers between 1 and 30:")
# for num in range(3, 31):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")

                                        #Program_12

#Write a Python program to calculate the factorial of a given number.

# input_num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, input_num + 1):
#     factorial *= i
# print(f"The factorial of {input_num} is: {factorial}")


                                     #Program_13

#write a program to sum 1 to 10 using for loop.

# total = 0
# for i in range(1, 11):
#     total = total + i
# print(f"The sum of numbers from 1 to 10 is: {total}")

                                   #Program_14

#write a program to count occurrence for each charter

# word = input("enter the number")
# char_count = {}

# for char in word :
#     if char in char_count:
#         char_count[char] +=1

#     else:
#         char_count[char] =1

# for char, count in char_count.items():
#     print(char + ':' , count)     
    







