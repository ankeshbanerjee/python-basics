'''
python collections:
1. list
2. tuple
3. set
4. dictionary

'''

#creating a list :
# list in python is same as arrays in other programming languages
lst = [1, 2, 3, 4, 5, 6, 7]
print(type(lst))
print(lst)
print(lst[2:6]) # prints lst[2] to lst[5]


#length of the string
print(f"the length of the list is: {len(lst)}")

# modifying element using index
lst[2] = 37
print("priting the list after modification: {}".format(lst))

# .append() : adds element at the end of the list
lst.append(100)
print(lst)

# insert : insert an element at the given position
lst.insert(1, 71)
print (lst)

#remove and del
lst.remove(71)
del lst[5]
print(lst)

#pop : removes the last element of the list
lst.pop()
print(lst)

# clear : clears the list
lst.clear()
print(lst)