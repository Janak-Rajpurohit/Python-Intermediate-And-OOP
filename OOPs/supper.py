class A:
    classvar="This is class variable A"   ## this is class 
    def __init__(self):
        self.var1="This variable in class A"
        # classvar="This is class variable A first instance"   ## this instance variable which is looked first before class var
        self.special="This is special"
    
class B(A):
    # classvar="This is class variable B"   ## This class B variable 
    def __init__(self):
        self.var1="This variable in class B"
        # classvar="This is class variable B"    ## this instance in class B which looked first before class A & B variables
        self.special="This is special in vlass B"
        super().__init__()       ## this command calls super class-A constructor {which set self.var1=.....}


a=A()
b=B()

print(b.var1,b.special,sep="\n")

