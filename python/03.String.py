
# String are immutable in python
str= "Akshay"

# Accessing character
print(str[0]) # will print 'A'

# Slice/Substring 
subStr=str[1:4] # Here substring will be returned ->'ksh' 
print(subStr)
# for [x:y] x is included and y is excludeed i.e. answer will be chars from x to y-1 position 

# Repeat same string again 
repeat =str * 3   # This will repeat string 3 times -> "AkshayAkshayAkshay"

# Length of string
print(len(str))

# Some useful methods
str.lower()  # lower case
str.upper()  # uppper case
str.startswith("a")
str.endswith("y")
str.replace("a","x") # replace all chars to specific

# There are many more method , check on chatgpt or on python offical website.