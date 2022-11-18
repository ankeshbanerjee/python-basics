age = input("Enter your age: \n")
print(type(age)) #python considers every input as a string

# so typecast it
age = int(age)
print(type(age))
print("Your age is {}".format(age))