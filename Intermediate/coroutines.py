## coroutines exersices
"""f=open("file.txt","w")
f.write("rohit janak ramesh hasan")
f.close"""

import time
def searcher():
	time.sleep(2)
	with open("file.txt","r") as f:
		content=f.read()
		#print(content)
		while True:
			name=(yield)
			if name in content.split(" "):
				print("Yes your name is there.")
			else:
				print("Sorry, your name is not there")
		
s=searcher()
print("executing next()")
next(s)

while True :
	name=input("Enter your name >>> ")
	if name =="x":
		break
	else:
		s.send(name)

