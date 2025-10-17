

# lambda function -> annonymous function ,used to pass into another function

square =lambda x :x*x     # need to mention lamda keyword 

print(square(2))    # calling is similar to normal function

additionOf3 =lambda x,y,z: x+y+z     # with multiple arguments

print(additionOf3(2,3,4))



#python provides some utility function which make easy to play with collection of object
# Lambda functions are very useful here as we can pass this as argument in these utility function

numbers=[2,3,4,5,6,7,8]

# common syntax
    # list(xxx(lambda,listtoprocess))
    # we have to cast it to list , xxx is type of function ,then lambda and list on which we want to perform operation

# 1.MAP - when you have to perform operation on every singel element of collection
#suppose we have to add 2 in every element of list

add2Lambda=lambda x:x+2
mapList=list(map(add2Lambda,numbers))

print(mapList)


# 2.filter - when we want to filter out some elements based on some condition
# take out even numbers from mapList

evenList=list(filter(lambda x:x%2==0,mapList))
print(evenList)

# 3.reduce -> reduce all elements to single number
from functools import reduce   #need to import this

reduceValue=reduce(lambda x,y:x+y,evenList)
print(reduceValue)