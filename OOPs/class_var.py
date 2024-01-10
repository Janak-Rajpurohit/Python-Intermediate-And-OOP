#class variable 
class Employee:
	no_leaves=8
	pass
	
harry=Employee()
rohan=Employee()

harry.name="Harry"
rohan.name="Rohan"
harry.salary=455
rohan.salary=600
harry.role="Gamer"
rohan.role="student"

print(harry.no_leaves)    ## all are same
print(rohan.no_leaves)
print(Employee.no_leaves)

## but if you want to change then only done through employee
Employee.no_leaves=9  ## for all changed
print(rohan.__dict__)
rohan.no_leaves=10  ##this is personal to rohan
print(rohan.__dict__)
print(harry.no_leaves)
print(rohan.no_leaves)  ##rohan's instance var obj can't change val
##class has common no leaves to all employees but rohan has own extra