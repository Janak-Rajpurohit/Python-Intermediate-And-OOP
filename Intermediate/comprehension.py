#list comprehensions

l=[i for i in range(20)]    ## number 1 to 20
print(l)

ls=[i for i in range(30) if i%3==0]  ## 1 to 30 number if divisible by zero
print(ls)
print()
#d={ i:f"item{i}" for i in range(1,1001) if i%100==0}   ## dict comprehensions
d={ i:f"item {i}" for i in range(5) } 
d2={value:key for key,value in d.items()}     ## reverse key value pair
print(d)
print(d2)
print("~"*20)

set={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}    ## set comprehension
print(set)

## generator comprehensions
## use round prarenthesis
g=(i for i in range(5))   
print(g)
print(g.__next__())  ## print genrated 
print(g.__next__())
for i in g:                ##print further i  
	print(i)