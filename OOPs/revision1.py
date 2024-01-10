class Students:
	total_marks=100
	
	def __init__(self,aname,amarks,astream):
		self.name=aname
		self.marks=amarks
		self.stream=astream
		
	def print_det(self):
		return self.name,self.marks,self.stream
	
	@classmethod
	def change_marks(cls,new):
		cls.total_marks=new
	@classmethod
	def from_string(cls,string):
		list1=string.split("-")
		return cls(*list1)
		
		
	pass
	
janak=Students("Janak",70,"Sci")
rohit=Students("Rohit",82,"Sci")
hasan=Students.from_string("Hasan-35-Com")
aditiya=rohit.from_string("Aditiya-78-Arts")
#print(janak.name,rohit.name)
#print(Students.total_marks)
'''
print(janak.print_det())
print(rohit.print_det())
'''
janak.change_marks(200)
print(rohit.total_marks)
print("-"*20)
print(hasan.marks,aditiya.name)

class Activity(Students):
	no_house=[1,2,3,4]
	def __init__(self,aname,amarks,astream,ahouse):
		self.name=aname
		self.marks=amarks
		self.stream=astream
		self.house=ahouse

	def sports(self,house):
		if self.house==4:
			return "football"	
		else:
			return "Cricket"
	
	pass
aayush=Activity("Aayush",69,"Sci",4)
print(aayush.total_marks)
print(aayush.house)
print(aayush.sports(aayush.house))

