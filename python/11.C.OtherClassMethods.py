
# Decorators are nothing but annotation which provides some feature 
# similar to annotation from other programmming language


class Test:

    a="Original" 

    @classmethod      # This helps to not override variable even value is assigned
    def classMethod(self):
        print("value of a is ",self.a)


    def __str__(self):    # similar to tostring - what data to print when actual object is printed
        return "this act as toString method"

    


testObj=Test();          # new Object is created
testObj.a="Overloaded"   # Value is modified 
testObj.classMethod()    # will print "Original" because of classMethod annotation

print(testObj)
print(testObj.a)
