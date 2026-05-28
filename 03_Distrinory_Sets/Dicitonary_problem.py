                                    # problem_01


#Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# print(dic)

# dic["contery"]="india"
# print(dic)

# dic["city"] = "delhi"
# print(dic)

# print(dic["name"])


                                   #Problem_02

#Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic.pop("age")
# print(dic)

# for key in dic:
#     print(f"key is exit : {key}")


                                #Problem_03

#Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.

# keys = ["name", "age", "city"]
# values = ["devesh", 25, "New York"]
# my_dic = dict(zip(keys, values))
# print(my_dic)

                                #Problem_04

#Write a Python program to remove all items from a dictionary while keeping the dictionary object itself intact.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic.clear()
# print(dic)

                                    #Problem_05

#Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.
# dic1={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic2={
#     "age": 30,
#     "country": "India"
# }
# dic1.update(dic2)
# print(dic1)

                                        #Problem_06

#Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary
# family = {  
#     "father": {
#         "name": "John",
#         "age": 50
#     },
#     "mother": {
#         "name": "Jane",
#         "age": 48
#     },
#     "child": {
#         "name": "Emily",
#         "age": 20
#     }
# }
# print(family["mother"]["name"])
# print(family["father"]["name"])
# print(family["child"]["name"])


                                           #problem_07

#Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.

# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# grades = student["grades"]["history"]
# print(grades)

                                           #Problem_08

#Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.

# keys = ["math", "science", "english", "history"]
# default_value = 0
# a = dict.fromkeys(keys, default_value)
# print(a)


                                           #Problem_09

#Write a Python program to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic["full_name"] = dic.pop("name")
# print(dic)

                                        #problem_10

#Write a Python program to remove multiple specific keys from a dictionary in one operation

# dict={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York",
#     "country": "India",
#     "profession": "Engineer"
# }
# keys_to_remove = ["age", "city", "profession"]
# for key in keys_to_remove:
#     dict.pop(key, None)
# print(dict)

                                      #problem_11

#Write a Python program to verify whether a specific value is present anywhere in a dictionary
# dict={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# for i in dict.values():
#     if i == "devesh":
#         print(f"value is present in dictionary :{i}")
#         break

                                            # problem_12

#Write a Python program to calculate the total of all numerical values stored in a dictionary
# dict={
#     "item1": 10,
#     "item2": 20,
#     "item3": 30,
#     "item4": 40
# }
# sum = 0
# for i in dict.values():
#     sum = sum + i
# print(f"total of all numerical values stored in a dictionary : {sum}")

# total = sum(dict.values())
# print(f"total of all numerical values stored in a dictionary : {total}")

                                         # problem_13

#Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary

# user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
# data ={}
# subset_keys = ["id", "username", "email"]
# for key in subset_keys:
#     if key in user:
#         data[key] = user[key]
# print(data)

                                            # program_14

#Write a Python program that uses zip() to combine a list of keys and a list of values into a single dictionary.

# keys = ["name", "age", "city"]
# values = ["devesh", 25, "New York"]
# my_dic = dict(zip(keys, values))
# print(my_dic)

                                          # Program_15 

#Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.

# text = "hello world"
# char_count = {}

# for i in text:
#     if i in text:
#         char_count[i] = char_count.get(i, 0) + 1
# print(char_count)
 
                                           # Program_16
#Write a Python program to change a specific value inside a dictionary that is nested within another dictionary
# family = {
#     "father": {
#         "name": "John",
#         "age": 50
#     },
#     "mother": {
#         "name": "Jane",
#         "age": 48
#     },
#     "child": {
#         "name": "Emily",
#         "age": 20
#     }
# }
# family["child"]["age"] = 21
# print(family)

                                          #Program_17

#Write a Python program to update a value located multiple levels deep inside a nested dictionary structure
# company = {
#     "department": {
#         "team": {
#             "employee": {
#                 "name": "Alice",
#                 "age": 30,
#                 "position": "Developer"
#             }
#         }
#     }
# }
# company["department"]["team"]["employee"]["position"] = "Senior Developer"
# print(company)  

                                              #Program_18

#Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.

# squares = {}
# for i in range(1, 11):
#     squares[i] = i ** 2
# print(squares)

# squares = {i: i ** 2 for i in range(1, 11)}
# print(squares)

                                              #Program_19

#Write a Python program to create a new dictionary containing only the key-value pairs from an existing dictionary where the value meets a specified condition.

# dict = {
#     "item1": 10,
#     "item2": 20,
#     "item3": 30,
#     "item4": 40
# }
# new_dict = {}
# for key, value in dict.items():
#     if value > 20:
#         new_dict[key] = value
# print(new_dict)


                                              # Program_20

#Write a Python program to find the key associated with the smallest numerical value in a dictionary

# stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
# min_key = min(stock, key=stock.get)
# print(f"The key associated with the smallest numerical value is: {min_key}")

                                               #Program_21

#Write a Python program to count the frequency of each word in a string, treating words case-insensitively so that “The” and “the” are counted as the same word.

# text = "the cat sat on the mat the cat"
# word_count = {}
# for i in text.split():
#     word = i.lower()
#     word_count[word] = word_count.get(word, 0) + 1
# print(word_count)

                                             #Program_22








=======
                                    # problem_01

#Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# print(dic)

# dic["contery"]="india"
# print(dic)

# dic["city"] = "delhi"
# print(dic)

# print(dic["name"])


                                   #Problem_02

#Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic.pop("age")
# print(dic)

# for key in dic:
#     print(f"key is exit : {key}")


                                #Problem_03

#Write a Python program to create a dictionary by mapping two equal-length lists, one containing keys and the other containing values.

# keys = ["name", "age", "city"]
# values = ["devesh", 25, "New York"]
# my_dic = dict(zip(keys, values))
# print(my_dic)

                                #Problem_04

#Write a Python program to remove all items from a dictionary while keeping the dictionary object itself intact.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic.clear()
# print(dic)

                                    #Problem_05

#Write a Python program to combine two dictionaries into a single dictionary. If both dictionaries share a key, the value from the second dictionary should take precedence.
# dic1={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic2={
#     "age": 30,
#     "country": "India"
# }
# dic1.update(dic2)
# print(dic1)

                                        #Problem_06

#Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary
# family = {  
#     "father": {
#         "name": "John",
#         "age": 50
#     },
#     "mother": {
#         "name": "Jane",
#         "age": 48
#     },
#     "child": {
#         "name": "Emily",
#         "age": 20
#     }
# }
# print(family["mother"]["name"])
# print(family["father"]["name"])
# print(family["child"]["name"])


                                           #problem_07

#Write a Python program to access the value associated with the key 'history' from a dictionary nested within a larger data structure.

# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# grades = student["grades"]["history"]
# print(grades)

                                           #Problem_08

#Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.

# keys = ["math", "science", "english", "history"]
# default_value = 0
# a = dict.fromkeys(keys, default_value)
# print(a)


                                           #Problem_09

#Write a Python program to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.

# dic={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# dic["full_name"] = dic.pop("name")
# print(dic)

                                        #problem_10

#Write a Python program to remove multiple specific keys from a dictionary in one operation

# dict={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York",
#     "country": "India",
#     "profession": "Engineer"
# }
# keys_to_remove = ["age", "city", "profession"]
# for key in keys_to_remove:
#     dict.pop(key, None)
# print(dict)

                                      #problem_11

#Write a Python program to verify whether a specific value is present anywhere in a dictionary
# dict={
#     "name":"devesh",
#     "age": 25,
#     "city": "New York"
# }
# for i in dict.values():
#     if i == "devesh":
#         print(f"value is present in dictionary :{i}")
#         break

                                            # problem_12

#Write a Python program to calculate the total of all numerical values stored in a dictionary
# dict={
#     "item1": 10,
#     "item2": 20,
#     "item3": 30,
#     "item4": 40
# }
# sum = 0
# for i in dict.values():
#     sum = sum + i
# print(f"total of all numerical values stored in a dictionary : {sum}")

# total = sum(dict.values())
# print(f"total of all numerical values stored in a dictionary : {total}")

                                         # problem_13

#Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary

# user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
# data ={}
# subset_keys = ["id", "username", "email"]
# for key in subset_keys:
#     if key in user:
#         data[key] = user[key]
# print(data)

                                            # program_14

#Write a Python program that uses zip() to combine a list of keys and a list of values into a single dictionary.

# keys = ["name", "age", "city"]
# values = ["devesh", 25, "New York"]
# my_dic = dict(zip(keys, values))
# print(my_dic)

                                          # Program_15 

#Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.

# text = "hello world"
# char_count = {}

# for i in text:
#     if i in text:
#         char_count[i] = char_count.get(i, 0) + 1
# print(char_count)
 
                                           # Program_16
#Write a Python program to change a specific value inside a dictionary that is nested within another dictionary
# family = {
#     "father": {
#         "name": "John",
#         "age": 50
#     },
#     "mother": {
#         "name": "Jane",
#         "age": 48
#     },
#     "child": {
#         "name": "Emily",
#         "age": 20
#     }
# }
# family["child"]["age"] = 21
# print(family)

                                          #Program_17

#Write a Python program to update a value located multiple levels deep inside a nested dictionary structure
# company = {
#     "department": {
#         "team": {
#             "employee": {
#                 "name": "Alice",
#                 "age": 30,
#                 "position": "Developer"
#             }
#         }
#     }
# }
# company["department"]["team"]["employee"]["position"] = "Senior Developer"
# print(company)  

                                              #Program_18

#Write a Python program to generate a dictionary of the squares of numbers from 1 to 10 using a dictionary comprehension in a single line.

# squares = {}
# for i in range(1, 11):
#     squares[i] = i ** 2
# print(squares)

# squares = {i: i ** 2 for i in range(1, 11)}
# print(squares)

                                              #Program_19

#Write a Python program to create a new dictionary containing only the key-value pairs from an existing dictionary where the value meets a specified condition.

# dict = {
#     "item1": 10,
#     "item2": 20,
#     "item3": 30,
#     "item4": 40
# }
# new_dict = {}
# for key, value in dict.items():
#     if value > 20:
#         new_dict[key] = value
# print(new_dict)


                                              # Program_20

#Write a Python program to find the key associated with the smallest numerical value in a dictionary

# stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
# min_key = min(stock, key=stock.get)
# print(f"The key associated with the smallest numerical value is: {min_key}")

                                               #Program_21

#Write a Python program to count the frequency of each word in a string, treating words case-insensitively so that “The” and “the” are counted as the same word.

# text = "the cat sat on the mat the cat"
# word_count = {}
# for i in text.split():
#     word = i.lower()
#     word_count[word] = word_count.get(word, 0) + 1
# print(word_count)

                                             #Program_22








>>>>>>> e47c744 (first commit)
