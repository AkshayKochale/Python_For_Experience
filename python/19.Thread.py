

# Thread are also similar as java just small syntax change

from threading import Thread
from time import sleep

class MyThread (Thread):   # extends with thread class

        def run(self):     # write run method 
               for i in range(5):
                       print("value :"+str(i))
                       sleep(1)    # sleep method in sec


thread1=MyThread()   
thread2=MyThread()


thread1.start() # start thread
thread2.start()
