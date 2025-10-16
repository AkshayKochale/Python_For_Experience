
    # Abstraction - creating class which has methods without body


class parent:  # abstract class

    def work(self):   # abstract method (No body)
        pass



class child(parent):  

    def test(self):
        print("test method")

    def work(self):
        print("Work method")    



childObj=child()            
childObj.test()
childObj.work()


# Note : its not strict that child has to implement all the abstract methods like other progamming language
# code still runs without giving error ,but when abstract are called nothing happens


# Also we have make all child classes to forcefully inherit method or not let create object of abstract class
# by using ABC module 


from abc import ABC,abstractmethod    # step 0 - import packages 

class Parent(ABC):    # step 1 - need to extend with abc class

    @abstractmethod   #step 2 - mark as abstract method
    def absMethod(self): 
        pass

#cannot create object
#parent1=Parent()    # this will throw runtime error - TypeError: Can't instantiate abstract class Parent with abstract method absMethod


class Child(Parent):

    def display(self):
        print("Display method")

    def absMethod(self):   # forcefully need to implement or get runtime error
         print("abs implemented")   


child1=Child()
child1.display()
