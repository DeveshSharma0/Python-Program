                                 #Program_01

#Number Patterns Programs In Python

# for i in range(6):
#     for j in range(i):
#         print(i, end=' ')
#     print()


                                 #Program_02

#Pyramid pattern of numbers
# row = 5
# for i in range(1, row+1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

                                #Program_03

#Inverted pyramid pattern of numbers
# row = 5
# b = 0
# for i in range(row ,0 , -1):
#     b = b + 1
#     for j in range(1,i + 1):
#         print(b ,end=' ')
#     print('\r')

                                #program_04

#Inverted Pyramid pattern with the same digit
# row = 5
# num = row

# for i in range(row , 0 ,-1):
#     for j in range(0 ,i):
#         print(num, end=' ')
#     print()

                               #program_05
 
#Another inverted half-pyramid pattern with a number

# row = 5
# for i in range(row , 0 , -1):
#     for j in range(0 ,i + 1):
#         print(j, end=' ')
#     print()


                               #program_06

# #Alternate numbers pattern using a while loop
# row = 5
# i = 1
# while i <= row:
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     print()
#     i += 1


                            #program_07
##Reverse number pattern

# row = 5
# for i in range(row, 0, -1):
#     for j in range(i ):
#         print(i, end=' ')
#     print()




                                #program_08

# #Reverse Pyramid of Numbers

# row = 6
# for i in range(1,row):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()


                            #program_09

# #Another reverse number pattern

# row = 6
# for i in range(0,row,-1):
#     for j in range(row-i,0,-1):
#         print(j,end=' ')
#     print()


                                #program_10

# #Print reverse number from 10 to 1

# start = 1
# stop = 2
# current = stop
# for i in range(2,6):
#     for j in range(start, stop):
#         current = current - 1
#         print(current, end=' ')
#     print()
#     start = stop
#     stop += i
#     current = stop


                                 #program_11

# #Number triangle pattern

# row = 6
# for i in range(1, row):

#     for j in range(row, 0, -1):
#         if j > i:
#              print(' ', end=' ')
#         else:
#             print(j, end=' ')
#             i+=1       
#     print("")

                               #program_12

# #Print a pattern of stars

# for i in range(1, 6):
#     for j in range(1,6):
#         print("*", end=' ')
#     print()

                              #program_13

#Pascal’s triangle pattern using numbers

# row = 8
# for i in range(row):
#     for j in range(i + 1):
        
#         num = 1
#         temp = j
#         if temp > i-temp:
#             temp = i - temp
#         for x in range(temp ):
#             num = num * (i - x)
#             num = num // (x + 1)
#         print(num, end=' ')
#     print()

                                 #program_14

# Multiplication table pattern

# for i in range(1, 11):
#     for j in range(1, i+1):
#         print(i * j, end=' ')
#     print()


                                      #program_15

# #Downward full Pyramid Pattern of star

# row = 5
# k = 2 * row - 2
# for i in range(row,-1,-1):
#     for j in range(k,0,-1):
#         print(end=' ')
#     k= k+1
#     for j in range(0,i+1):
#          print('*', end=' ')
#     print()

                                     #program_16

# #Right start pattern of star

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=' ')
#     print()
# for i in range(5, 0, -1):
#     for j in range(0, i):
#         print("*", end=' ')
#     print()
    

                                      #program_17

# #Left triangle pascal’s pattern

# for i in range(1, 6):
#     for j in range(1, i + 1 ):
#         print(j, end=' ')
#     print()
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


                                    #program_18

# # #Print a pattern of characters

# ascii_number = 65
# for i in range(0, 7):
#     for j in range(0, i + 1):
#         character = chr(ascii_number)
#         print(character, end=' ')
#         ascii_number += 1
#     print(" ")

                                       #program_19

# # #Print a pattern of characters in reverse order

# ascii_number = 65
# for i in range(7, 0, -1):
#     for j in range(0, i + 1):
#         character = chr(ascii_number)
#         print(character, end=' ')
#         ascii_number += 1
#     print(" ")


                                    #program_20

# #Print a pattern of numbers in reverse order

# rows = 6
# for i in range(0, rows):
#     for j in range(rows - 1, i, -1):
#         print(j, '', end='')
#     for l in range(i):
#         print('    ', end='')
#     for k in range(i + 1, rows):
#         print(k, '', end='')
#     print('\n')




