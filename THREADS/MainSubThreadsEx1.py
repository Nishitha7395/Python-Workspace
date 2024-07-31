#Program for demonstrating Thread based applications (Contains MainThread and Sub Threads)
#MainSubThreadsEx1.py
import threading
def hello():
	print("line 5: hello() executed by {}".format(threading.current_thread().name))

def hi():
	print("Line 8: hi() executed by {}".format(threading.current_thread().name))

def welcome():
	print("Line 11: welcome() executed by {}".format(threading.current_thread().name))

#main program
print("Line 14: Program Execution stated by {}".format(threading.current_thread().name))
print("Number of threads in this program=",threading.active_count())
print("----------------------------------------------------------------")
#create 3 sub threads
t1=threading.Thread(target=hello) #Here t1 is object of Thread-sub thread and its default name is Thread-1
t2=threading.Thread(target=hi) #Here t2 is object of Thread-sub thread and its default name is Thread-2
t3=threading.Thread(target=welcome) #Here t3 is object of Thread-sub thread and its default name is Thread-3
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
print("----------------------------------------------------------------")
print("Line 21: Program Execution ended by {}".format(threading.current_thread().name))