import datetime

# x = datetime.datetime.now()    #Display current Date & Time ....
# print(x)


# x = datetime.datetime.now()

# print(x.year)                          #Display year....
# print(x.strftime("%A"))           #format code for reference


##### Create Date Object ............

# x = datetime.datetime(2026,5,14)       # Provide spacific date and time and year
# print(x)


###### The Strftime() Method...........


x = datetime.datetime(2026,5,14) 

print(x.strftime("%A"))
print(x.strftime("%p"))   #more formate......



