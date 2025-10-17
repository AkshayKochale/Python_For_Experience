

# In python each thing is consider as object 
# arithmatic and comparsion opertors are known to work with primitive types
#  but in python we can tell how this operator should work with object 
# in short we can customized operator as per our need hence Operator overloading

class Test :

    val =0

    def __init__(self,val):
          self.val=val


    def __add__(self,test2):    # __add__ is defined to tell how object should add 
           return self.val+test2.val ; 



obj1=Test(3)
obj2=Test(4)

print("value is :" +str(obj1+obj2))


# In similiar way there are multiple operators we can overload like 
# __add__ for +, __sub__ for -, __mul__ for *, __eq__ for ==, __lt__ for <   .... etc.