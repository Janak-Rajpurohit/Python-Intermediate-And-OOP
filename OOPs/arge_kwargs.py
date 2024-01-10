# args and kwargs

"""def fun(a,b,c,d):     ### just 4 arguments
	print(a,b,c,d)       ## if i want to add more 
fun(1,2,3,4) """             ## argument I CAN'T....'

def argfun(*args,**kwargs):
	for i in args:
		print(i)
	for j,k in kwargs.items():    ## kwargs 
		print(j,k)

har =[1,2,3,4,5]        ### i can add many elem
kw={ "a":1,"b":2,"c":3}

argfun(*har,**kw)
