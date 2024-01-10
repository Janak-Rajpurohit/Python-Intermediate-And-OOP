## functions chacheing 
import time
from functools import lru_cache

@lru_cache(maxsize=3)
def func(n):
	time.sleep(n)
	return n
	                                              #### max is 3 so it will take 3 latest value for cache##
if __name__=="__main__":
	print("calling")
	func(3)
	print("Done...calliung again")
	func(3)                            ### no deyal here again the function has been cached 
	print("Called")
	func(3)
	print("___")
	func(3)
	print("___")
	func(4)
	print("------")
	