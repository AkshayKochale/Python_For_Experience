
a=5
b=0

# similar to java exception is handled by try catch finally block
# everything is simialr just syntax is little diff
# Exception hierarchy is also same

try :
    print(a/b)
except Exception as e:
    print("Error happend..")
finally:
    print("All done")    
