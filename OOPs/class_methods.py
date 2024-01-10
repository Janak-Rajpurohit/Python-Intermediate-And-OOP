# class methods
# change no of leaves through instance
class Employee:
    no_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdet(self):  ##self is arg
        return self.name, self.salary, self.role

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_leaves = newleaves


janak = Employee("Janak", 300, "dancer")
harry = Employee("Harry", 455, "gamer")
rohan = Employee("Rohan", 600, "student")

harry.change_leaves(34)
print(harry.no_leaves)
