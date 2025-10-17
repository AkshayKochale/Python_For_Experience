

# Like any other programming language 2 simple types of loop while and for

list=[1,2,3,4,5,6,7,8]

""" For loop """

# 1. using range
# need to pass range (start,end) , start in including and end is excluding ,so loop will run start to end-1
# flexible to process data between range 
# pass third parameter to take n jumps into index (start,end,jump/skip) eg. (1,8,2)-> 1,3,5,7
for idx in range(0,len(list)):
                  print(list[idx])

# 2.using enhance loop
# direct iteration on list from start to end 
for no in list:
        print(no)


""" While loop """

len=len(list)
idx=0
while(idx<len):
        print(list[idx])
        idx+=1


""" Iterator """

it =iter(list)

try:
    while True:
        print(it.__next__())     # Has next is not there is python so this is the way
except StopIteration:
        print("end")
  
