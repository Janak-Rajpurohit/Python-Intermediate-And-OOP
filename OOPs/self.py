## self METHODS


class Employee:
	no_leaves=8
	def __init__( self ,aname,asalary,arole):
		self.name=aname
		self.salary=asalary
		self.role=arole
		
		
	def printdet(self):        ##self is arg
		return self.name ,self.salary,self.role	
janak=Employee("Janak",300,"dancer")	
#harry=Employee()
#rohan=Employee()

"""harry.name="Harry"
rohan.name="Rohan"
harry.salary=455
rohan.salary=600
harry.role="Gamer"
rohan.role="student"""

#print(rohan.printdet())   #rohan goes as arg
#print(harry.printdet()) #harry go as agr

#new employee
#janak=Employee("Janak",300,"dancer")
# no janak.name and all 
## constructor give agrs to Employee()
# by __init__
##in self janak will go
# then name salary and role

print(janak.salary)