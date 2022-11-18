# creating a set
# in set, repeating of elements isn't possible

s1 = {334, 31, 11, 8, 22, 2, 2, 2, 1, 7, 8, 9}
print (s1)

# add element
s1.add(18)
print(s1)

# remove
s1.remove(11) 
# if the element in the argument, is not present in the set,
# then it shows error
print(s1)

#discard
s1.discard(8)
# if the element is present then removes it
# if not present, then it doesn't show error
print(s1)

# same as list : .clear(), .pop(), del


# intersection and union
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {4, 5, 6, 7}

#intersection
#set.intersection(set1, set2 ... etc)
print (s1.intersection(s2))
print (s1.intersection(s2, s3))
#or
print (s2 & s3)
print (s1 & s2 & s3)


#union
# set.union (set1, set2 ... etc)
print(s1.union(s2))
print (s1.union(s2,s3))
#or
print (s1 | s2)
print (s1 | s2 | s3)