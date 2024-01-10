## exercise 

l=[]
while True :
	item=input("Enter item (x to exit ) >>> ")
	if item=="x" :
		break
	else:
		l.append(item)
	
print("(1) LIST COMPREHENSION")
print("(2)SET COMPREHENSION")
print("(3) DICT COMPREHENSION")
print("(4) GEN COMPREHENSION")

ch=int(input("Enter your choice (1/2/3/4) >>> "))
if ch==1:
	lst=[i for i in l]
	print(lst)
elif ch==2:
	set={i for i in l}
	print(set)
elif ch==3:
	d={i:f"value {i}" for i in l }
	print(d)
elif ch==4:
	g=(i for i in l)
	print(g)
	for i in g:
		print(i)
else:
	print("INVALID INPUT")