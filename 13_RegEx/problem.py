
### Regular Expression ( regEx )......
 
                              ## RegEx Functions ##

import re
txt = "The rain in spin"
x = re.search("^The.*spin$",txt)
print(x)

x = re.findall("ai",txt)
print(x)

x = re.search("\s",txt)     # Word bhe search kar sakte ho
print(x)
 
x = re.split("\s",txt)
print(x)

x = re.sub("\s","|" ,"txt")
print(x)


####.........................................................................................................####

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

####.............................................Metacharacters............................................................####
                        

# [] - Set of characters............

import re
text = "hello"
x = re.findall("[a-m]",text)    # search A - M tak ke value dega 
print(x)

# \\ - Special sequence ya escape...............

import re
text = "hello"

x = re.findall(r"\d",text)          #  \d	Koi bhi digit 0-9
x = re.findall(r"\.",text)      # \. ke jagah koe bhe char aa sakta h 

print(x)

# . - Any character..........

import re
text = "hello Hero"
x = re.findall("he..o",text)
print(x)

# ^ - Starts with ...................

import re
text = "hello Hero"
x = re.findall("^hello",text)
print(x)

# $ - Ends with...............

import re
text = "hello world"
print(re.findall("world$", text))

# * - Zero or more..............

import re
text = "heo heoo heeeeeo"
print(re.findall("he*o", text))


# + - One or more............

import re
text = "heo heoo heeeeeo"
print(re.findall("he+o", text))

# ? - Zero or one..........

import re
text = "heo helo"
print(re.findall("he.?o", text))

# {} - Exact count..............

import re
text = "heoo hello"
print(re.findall("he.{2}o", text))

# | - Either or............

import re
text = "falls stays falls"
print(re.findall("falls|stays", text))

#  () - Capture and group.........

import re
text = "hello hello"
print(re.findall("(he)llo", text))


####.........................................................................................................####
