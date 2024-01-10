# static methods
class Employee:
    no_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdet(self):  ##self is arg
        return self.name, self.salary, self.role

    @classmethod
    def from_str(cls, string):
        # return cls(*string.split("-"))
        param = string.split("-")
        return cls(param[0], param[1], param[2])

    @staticmethod
    def print_good(string):  # does take harry,rohan
        print("this is good", string)
        return "good"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_leaves = newleaves


janak = Employee("Janak", 300, "dancer")
harry = Employee("Harry", 455, "gamer")
rohan = Employee("Rohan", 600, "student")
karan = Employee.from_str("Karan-450-singer")
print(harry.print_good(33))
