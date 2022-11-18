class Employee:
    #constructor
    def __init__(self, gname, gsalary) :
        self.name = gname
        self.salary = gsalary

e1 = Employee("abc", 50000)
print(e1.name)
print(e1.salary)