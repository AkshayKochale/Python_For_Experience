
# Python uses def keyword to define function


#1. No argument function 

def printingFunction():
    print("Function is called.")


printingFunction() #  # calling function

#2. argument function

def argfunction(val):
    print("hello",val)

argfunction("akshay")  # calling function


#3. return value function

def performSum(a,b):
    return a+b

sum=performSum(2,3) #calling function
print(sum) #printing value



# Python specific syntax
def defaultValueSyntax(name="akshay"):
    print(name)

#this sets default value for name, if name is not passed akshay will be taken 

defaultValueSyntax() # this is valid as we have default value assign to name ,else will throw error
defaultValueSyntax("myName")