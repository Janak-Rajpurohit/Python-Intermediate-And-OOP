# encapsulation - hide process of implementation
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

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_leaves = newleaves


class Programmer(Employee):
    def __init__(self, name, salary, role, lang):
        self.name = name
        self.salary = salary
        self.role = role
        self.lang = lang

    def print_prog(self):
        return self.name, self.lang


janak = Employee("Janak", 300, "dancer")
harry = Employee("Harry", 455, "gamer")
rohan = Employee("Rohan", 600, "student")
karan = Employee.from_str("Karan-450-singer")
subh = Programmer("Subh", 700, "coder", "python")
print(subh.print_prog())
print(subh.printdet())
