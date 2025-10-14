

# Inheritance - extending one class by another (parent child relationship)

class Father:  # Father class 
    value =2
    text="hi"

    def call(self):
        print("call father ")

    def __init__(self):   
        print("parent is created")



class Mother: # Mother class
    input=3.2

    def motherMethod(self):
        print("from mother method")

    def call(self):
        print("call mother")    


class Child(Mother,Father):  # child class using (parentclassname) to extend to that class
    value=3

    def childMethod(self):
        print("from child")

   
    def __init__(self):  
        print("child is created")



# calling methods and variables

childObj=Child()   
print(childObj.text)    #accesing parent functionality in child 

#calling parent method - as child inherit property of parent 
childObj.motherMethod()

# If both have same method then which method to call is depend on which object is created
# Hierarchy can be multilevel and last declared (top -bottom) init will be called 
# To call parent constructor we have to use super().__init__()
# Overriding method is possible

# almost all the properties are similar to c++/Java inheritance 
# except multiple inheritance is allowed and during conflict which method to call is resolved by which parent class is extended first has prefrence.
childObj.call()   # will invoke call method of mother as it was extended before father