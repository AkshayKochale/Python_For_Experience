
    # To define class "class" is used 
    # Intendation is required other will throw complie time exception


class Myclass:
    
    number =10  # define variable 

    @staticmethod         #annotation not mandatory but good practice
    def customStaticFun():  # static function - can be access without creating object
        print("from static function")

    def printSomething(self):  #define function non static function 
        print("heyy")

    def __init__(self):   # similar to constructor -> automatic call when object is created
        print("object is created")

    


# Create and access variables and methods

obj=Myclass() ## creating object

print(obj.number) # access variable inside Object 

obj.printSomething()  # access methods using Object

Myclass.customStaticFun() # access static method using class name