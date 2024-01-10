##    generators 

def gen(n):
	for i in range(n):
		yield i          #generates i which gets stored in g

g=gen(5)
print(g)
#print(g.__next__())   ## print stored i in sequence 
#print(g.__next__())
#print(g.__next__())
for i in g:                   ## print stored i
	print(i,end=" ")