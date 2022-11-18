name = "abc"
print(name)

# print string with multiple lines
name = '''abc
is a good boy'''
print (name)

#accessing elements of a string with their indeces
name = "abcdef"
print(name[1])
print(name[2:5]) # 2 to (5-1)=4

#strip function
name = "   abcdef   "
print(name)
print(name.strip()) #removes unwanted spaces

#length of string
name = "abcdef"
print(len(name))

# upper, lower
name = name.upper()
print(name)
name = name.lower()
print(name)

# replace
name = name.replace("de", "R")
print(name)
var = "abc, def, ghi"
var = var.replace(", ", "")
print(var)

# adding strings
str1 = "His name is: "
str2 = "abcdef"
print(str1 + str2)

name1 = "abc"
name2 = "def"
temp = "His name is {} and is his friend is {}".format(name1, name2)
print(temp)
temp = "His name is {1} and is his friend is {0}".format(name1, name2)
print(temp)
temp = f"His name is {name1} and his friend is {name2}"
print(temp)