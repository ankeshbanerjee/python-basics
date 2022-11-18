# dictionaries are key-value pairs
schoolDict = {
    "name" : "abc",
    "class" : "4th",
    "marks" : 70,
    "Hours in school" : 6
}
print (schoolDict)
print (schoolDict["name"])

# modifying elements
schoolDict["name"] = "def"
print (schoolDict)

# pop and del
schoolDict.pop("Hours in school")
del schoolDict["marks"]
print (schoolDict)

#update
schoolDict.update(Marks = 70, attendance= '80%')
print(schoolDict)
schoolDict2 = {"school name" : "ABC school"}
schoolDict.update(schoolDict2)
print(schoolDict)

#clear
schoolDict.clear()
print(schoolDict)