
# Dictionary is similar to map in other programming language 
# Stores key value pair , all the working logic is similar to map
# It is mutable and unorder


dict={
        "key1":"value1",
        "key2":"value2",
        "key3":"value3",
        "nest" :{"inner":"innerValue1"}
     }

emptyDict={} # create empty dict

print(type(dict)) #will print <dict>

print(dict["key1"]) # will print value1 , if no value then error

print(dict["nest"]) # {"inner":"innerValue1"}

print(dict["nest"]["inner"]) # innerValue1

dict["key1"]="newValue1" # This will update value of key1 in dictionary

print(dict["key1"]) # will print newValue1

# Methods

dict.keys() # get all keys list

dict.values() # get all values list

dict.get("key1") #get value for key , if no value then None

dict.items()  # list of all items in map ,similar to entrySet()

dict.pop("key1") # remove key1 from dict

dict.popitem() # remove last added item

l=("key1","key2") # tuple of keys
dict.fromkeys(l,"Myval")  # create new dictionary in from keys and specific value