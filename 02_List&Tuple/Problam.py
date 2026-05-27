                                  # Problem_01

# F1 = input("Enter the Fruits Name1 : ")
# F2 = input("Enter the Fruits Name2 : ")
# F3 = input("Enter the Fruits Name3 : ")
# F4 = input("Enter the Fruits Name4 : ")
# F5 = input("Enter the Fruits Name5 : ")
# F6 = input("Enter the Fruits Name6 : ")
# F7 = input("Enter the Fruits Name7 : ")

# Fruits = [ F1 ,F2  , F3 ,F4 , F5, F6, F7]
# print(Fruits)


                                 #problem_02

# S1 = int(input("Enter the Student marks1 : "))
# S2 = int(input("Enter the Student marks2 : "))
# S3 = int(input("Enter the Student marks3 : "))
# S4 = int(input("Enter the Student marks4 : "))
# S5 = int(input("Enter the Student marks5 : "))
# S6 = int(input("Enter the Student marks6 : "))

# Marks = [ S1 , S2 , S3 , S4 , S5 , S6]
# Marks.sort()
# print(Marks)

                                #Problem_03



# Fruits = ('F1' ,'F2' , 'F3' ,'F4' , 'F5', 'F6', 'F7' )
# x = list(Fruits)
# x[0:14] = x + ["Mango", 1, 2, 3, 4, 7, 8, 9, 10, True, False]
# Fruits = tuple(x)
# print(Fruits)

                    #Problem_04   ( use Ai solve )

# Num = [1, 2, 3, 4]
# # Sum of all elements
# total = sum(Num)
# print(total)

                                 # Problem_05

# a =  (7,0,8,0,0,9)
# # Count the number of zeros in the tuple
# zero_count = a.count(0)
# print(zero_count)

                                 # Problem_06


# a = [1, 2, 3, 4, 5]
# print(a[2]) # problem_01

# for i in range(len(a)):#problem_02   
#     print(a[i])

# if a is not None: # problem_03
#     print("The list is not empty.")         #Type 1

# b = len(a) == 0               #Type 2
# print("Empty list")

                                   #Problem_07


#Exercise 3. Sum and Average of All Numbers in a List

# a = (1,2,3,4,5,6,7,8)
# sum = sum(a)
# avg = sum/ len(a)
# print(f"sum is {sum} and Average is {avg}")

                                 # Problem_08

# Exercise 4. Find Maximum and Minimum from List

# A = ( 34,5659,5861,256,235,5,558)
# max = max(A)
# min = min(A)
# print(f"The maximum is :{max}, the minimum is :{min}")

                             
                                  #Problem_09

#Exercise 5. Calculate the Product of All Elements

# a = (1,2,3,4,5,6,7,8)
# product = 1
# for i in a:
#     product = product*i
# print(f"Product :{product}")

                                #Problem_10

#Exercise 6. Count Even and Odd Numbers

# a = (1,2,3,4,5,6,7,8)
# even = 0
# odd_count = 0
# for num in a:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd_count += 1
# print(f"Even num : {even}")
# print(f"odd num : {odd_count}")
    
                                # Problem_11

#Exercise 7. Reverse a List

# a = [1,2,3,4,5,6,7,8]
# reversed_list = a[::-1]
# print(reversed_list)

                                 #Problem_12

#Exercise 9. Create a Copy of a List

# a = [1,2,3,4,5,6,7,8]
# copy_list = a.copy()
# copy_list.append(9)
# print(a)  
# print(copy_list)  

                                 #Problem_13

#Exercise 12. Swap Two Elements at Given Indices

# Original = [23, 65, 19, 90]
# index1 = 1
# index2 = 3      
# Original[index1], Original[index2] = Original[index2], Original[index1]
# print(Original)

# # Same concept 

# a = 2 
# b = 3
# a, b = b, a
# print(f"a: {a}, b: {b}")


                                   # Problem_14

#Exercise 13. Access Nested Lists (Simple Indexing)

# A = [[1, 2], [3, 4, 5], [6, 7]]

# print(A[0][1])  # Output: 2
# print(A[1][2])  # Output: 5
# print(A[2][0])  # Output: 6

                                 #problem_15

#Exercise 14. Check if List Contains a Specific Item

# a = [1, 2, 3, 4, 5]

# if 5 in a:
#     print("True")

# else:
#     print("False")


                                   # Problem_16

#Exercise 15. Find the Longest String in a List

# A = ["apple", "banana", "cherry", "date"]
# longest_string = max(A, key=len)
# print(longest_string) 

                                #Problem_17

#Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
# a = [1, 2, 3, 4, 5]
# for i in a:
#     square = i ** 2
#     print(square)   


                                # problem_18

#Exercise 17. Count Occurrences of an Item

# sample_list = [10, 20, 30, 10, 40, 10, 50]
# occurrence_count = sample_list.count(10)

# print(f"The number {10} appears {occurrence_count} times.")

                                 # problem_19
         
#Exercise 19. Remove Empty Strings from a List of Strings

# string_list = ["apple", "", "banana", "cherry", "", "date"]
# for i in string_list:
#     if i == "":
#         string_list.remove(i)   #type 1
# print(string_list)

# names = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# cleaned_names = list(filter(None, names))
# print(f"Cleaned Names: {cleaned_names}")     #Type 2

                               # problem_20

#Exercise 20. Remove Duplicates from List

# original_list = [1, 2, 3, 2, 4, 1, 5]
# unique_list = list(set(original_list))
# print(unique_list)


                            # problem_21

#Exercise 22. Concatenate Two Lists Index-wise

# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]                     #Type 1
# for i in range(len(list1)):
#     concatenated = list1[i] + list2[i]
#     print(concatenated) 


# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]                     #Type 2  same
# concatenated_list = [i + j for i, j in zip(list1, list2)]
# print(concatenated_list)


# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]                     #Type 3  Same
# concatenated_list = []
# for a, b in zip(list1, list2):
#      concatenated_list.append(a + b)
# print(concatenated_list)
 

# list1 = ["A", "B", "C"]
# list2 = ["D", "E", "F"]                     #Type 3  
# for a, b in zip(list1, list2):
#     print(a,b)

                          

#************************************************* Thanks for solve these problems  *************************************************