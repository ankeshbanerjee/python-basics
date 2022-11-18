# creating a tuple
a = ("abc", "def", "ghi")
print (a)

# functions of tuple are same as list

# elements of tuple can't be changed/ modified
# a[0] = "dfdf" => not possible

# to modify tuple, typecast it into list
a = list(a)
a[0] = 'jkl'
print (a)
