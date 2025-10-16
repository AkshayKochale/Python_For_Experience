
# Polymorphism -> creating many forms (Method to be very specific)
# 2 type -> Overloading (same class with multiple methods with same name and diff arguments)
#           Overriding (overriding parent method in child class )

class Test :

    def testMethod(self,i):
        print("this is form 1")

    def  testMethod(self,i):
        print("this is form 2")   

    def printParent(self):
        print("Printing from parent")    



testObj=Test()
i=5
testObj.testMethod(i)       

# Note : overloading does not truly work in python like any other programming language 
# as we dont have type mention for arguments ,so compiler runs last defined method of same name

class TestChild(Test):    # class is inherited


    def testMethod(self,i):   # Parent method testMethod is overridden in child
        print("Printing from child")



testChildObj=TestChild()
testChildObj.testMethod(1)
testChildObj.printParent()

