
"""LIST"""

# Create list -> modifiable list 
list =[1,2,3,4,5]

print(type(list))
print(list)

#methods 
list.append(8) # add
list.clear() # clear all 
list.insert(0,1) # insert at speific index
list.pop() # remove last
list.remove(0,1) # remove from spcific index
# sort , reverse ..etc


"""TUPLE"""

# Create unmodifiable(can not add or remove elements) list -> called tuple in python
tupleList=(1,2,4,3,3,4,5)

print(type(tupleList))
print(tupleList)

#Method
tupleList.count(1) # count total number of occurence 
tupleList.index(1) # count first apparence of character, also we can add start and end index(window) .index(ele,s,e)




