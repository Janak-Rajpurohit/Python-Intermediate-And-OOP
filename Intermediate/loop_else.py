## for loop and else 
item=["j","a","n","a","k"]
for i in item:
	print(i)                ### else is executed when loop gets complete 
	#break                   ## if there break then else is not executedt
	                                 ## jab for loop pura chal jayega tab else execute hoga
else:
	print("this for loop ended properly")
	
khana=["roti","sabzi"]
for i in khana :
	if i =="roll":
		break
else:
	print("roll not found")