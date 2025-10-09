

# Python has very simple built-in function for all operations to perform on file

data=open("TempFile.txt") # open(filename with absolute/relative path)
print(data.read()) # read all data from file 
#data.readLine() -> read line by line
#data.readLines() -> read all lines but gives each line  in form of list 
data.close() #close resource 


# There are different modes in open function by default its read -> open(path,"r")
# These modes allow us to perform various operation on file


#1. Write mode
fileObj=open("TempFile.txt","w")   # clears and write new data to file
fileObj.write("I am writing from here..") 
fileObj.close()

#2. Append mode
appendMode=open("TempFile.txt","a") # when we dont wan to clear previous data just append at the end
appendMode.write("I am appending data from here..") 
appendMode.close()    
  # Note. you can add \n to add new line
 
#3. Read/write in binary data
# modes are rb -> read binary , wb-> write binary

# also we can combine mode together using + for example  r+, w+ , a+
# this allows to perform 2 operation together, like first read and then write
# for more info check pyhton file modes table

# manully manageing resource 
# Instead of closing resources every time we can use with statment to autoclose resource

with open("TempFile.txt") as f:
    print(f.read())

# reosurce is autoclose 

     
