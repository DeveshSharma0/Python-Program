

# import json
# x= dir(json)
# for i in x:
#     print(i)


##Convert from JSON to Python:

# import json
# x = '{"name":"devesh","age":30,"city":"up"}'
# y = json.loads(x)
# print(y["age"])


####............................................................###

##Convert from Python to JSON:
# import json
# ## a Python object (dict):
# x = {
#     "name":"devesh",
#     "age":20,
#     "city":"up"
# }
# #convert into JSON
# y = json.dumps(x ,indent=4 , separators=(".","="))        ##seprate result (, = .) % (: = = ) Replace 
# #The result is a JSON string
# print(y)

####............................................................###

# ##Convert from Python to JSON:
# import json
# ## a Python object (dict):
# x = {
#     "name":"devesh",
#     "age":20,
#     "city":"up"
# }
# #convert into JSON
# y = json.dumps(x, indent=4, sort_keys=True)            # shorted result
# #The result is a JSON string
# print(y)

####............................................................###



                                      #Program_01
      ##Convert the following dictionary into JSON format   ( data = {"key1" : "value1", "key2" : "value2"} )

# import json
# data = {"key1" : "value1", "key2" : "value2"}
# x = json.dumps(data)
# print(x)

                                      # Program_02
    ## Access the value of key2 from the following JSON  ( sampleJson = """{"key1": "value1", "key2": "value2"}"""  )

# import json
# simplejson = """{"key1": "value1", "key2": "value2"}"""
# x = json.loads(simplejson)
# print(x["key2"])


                                      #Program_03
    ##PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").( sampleJson = {"key1": "value1", "key2": "value2"}  )
# import json

# simpleJson = {"key1": "value1", "key2": "value2"}
# x = json.dumps(simpleJson, indent=2 ,separators=(","," = ") )
# print(x)


                                   #Program_04

      ###  Sort JSON keys in and write them into a file ( sampleJson = {"id" : 1, "name" : "value2", "age" : 29} )

# import json
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# x = json.dumps(sampleJson,indent=2, sort_keys=True)
# print(x)

                                #Program_05
        ##  Access the nested key ‘salary’ from the following JSON

# import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# data = json.loads(sampleJson)
# print(data['company']['employee']['payble']['salary'])


                        #Program_06

   ###Convert the following Vehicle Object into JSON
# from json import JSONEncoder
# import json

# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
# class VehieleEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__

# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# # Convert it into JSON format
# x = json.dumps(vehicle,indent=4,cls=VehieleEncoder)
# print(x)

                                     #Program_07
   ###Convert the following JSON into Vehicle Object   { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

# import json

# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price

# def vehicleDecoder(obj):
#         return Vehicle(obj['name'], obj['engine'], obj['price'])

# vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
#            object_hook=vehicleDecoder)     # coll function

# print("Type of decoded object from JSON Data")
# print(type(vehicleObj))
# print("Vehicle Details")
# print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)


                                         # Program_08
           ###Check whether following json is valid or invalid. If Invalid correct it  """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""                 

# import json

# def validateJSON(jsonData):
#     try:
#         json.loads(jsonData)
#     except ValueError as err:
#         return False
#     return True

# InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
# isValid = validateJSON(InvalidJsonData)

# print("Given JSON string is Valid", isValid)


                                            # Program_09
        ##Parse the following JSON to get all the values of a key ‘name’ within an array


# import json

# sampleJson = """[ 
#    { 
#       "id":1,
#       "name":"name1",
#       "color":[ 
#          "red",
#          "green"
#       ]
#    },
#    { 
#       "id":2,
#       "name":"name2",
#       "color":[ 
#          "pink",
#          "yellow"
#       ]
#    }
# ]"""

# data = []
# try:
#     data = json.loads(sampleJson)
# except Exception as e:
#     print(e)

# dataList = [item.get('name') for item in data]
# print(dataList)



