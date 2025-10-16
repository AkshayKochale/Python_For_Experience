

# Encapsulation - binding data with object to no one can access it

# In pyhton to make variable private or limited to class we need _ or __ infront of variable
# _ makes it soft private (can access but gives warning )
# __ makes it hard private (No one can access)


class Test:

    __val=0  # variable is hard private, so only way to access is using getters and setter 


    @property     # Getter
    def __val(self):   # function name should be same as variable name to set get value
        return self.__val

    @__val.setter   # Setter 
    def __val(self,val):    
        self.__val=val




# print(Test.__val) #   will give runtime error -AttributeError: type object 'Test' has no attribute '__val'

testObj=Test()
testObj.__val=5. # this looks same as assigning varible but internally it is using setter method 
print(testObj.__val) # same here getter method is use

# as we have getter and setter method we have acess how varible are access outside class
# we can modify getter and  setter to prevent data security

