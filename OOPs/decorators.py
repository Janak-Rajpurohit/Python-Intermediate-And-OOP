## Decorators
"""
def fun():
	print("hello")
	
fun2=fun
fun2()      ### its print hello even after deleted 
del fun      ## fun2 is copy
fun2()
"""

def fun_ret(num):
    if num == 0:
        return "print"
    if num == 1:
        return "one"


a = fun_ret(0)  ### 1 --> one and 0-->print
print(a)


def exe(func):  ### executing print func
    func("this")  ### by our func


exe(print)
# -----------------


def dec1(func1):
    def nowexe():
        print("Executing now")
        func1()
        print("Executed")

    return nowexe


@dec1
def who():
    print("You")


# who=dec1(who)  ## this is decorater
who()
## who is betwn func
