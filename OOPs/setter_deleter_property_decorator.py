#setter 

class Employee:
	
	def __init__(self,fname,lname):
		self.fname =fname 
		self.lname=lname
		
		
	@property     ## in function no require to give brackets i.e.. NO-->func() only func
	def print_det(self):
		return f"name-{self.fname},{self.lname}"
	@property
	def email(self):
		if self.fname==None or self.lname==None :
			print("No mail set.")
			exit()
		return f"{self.fname}.{self.lname}@gmail.com"
		
	@email.setter
	def email(self,string):
		self.mail=string
		name=string.split("@")[0]
		self.fname=name.split(".")[0]
		self.lname=name.split(".")[1]
	
	@email.deleter
	def email(self):
		self.lname=None
		self.fname=None
		
jan_raj=Employee("jan","raj")
#print(jan_raj.print_det)
print(jan_raj.email)
#jan_raj.fname="adi" 	## for made seprate function to change fname
print(jan_raj.email)
jan_raj.email="adi.ghar@gmail.com"
print(jan_raj.lname)
del jan_raj.email
print(jan_raj.email)
