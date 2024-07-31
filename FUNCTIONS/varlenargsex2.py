 #This program demonstrates the concept of Variable Length Arguments
 #varlenargsex2.py

def disp(x):
	print("{}".format(x))

disp(10) #Function Call

def disp(x,y):
	print("{}\t{}".format(x,y))

disp(10,20)  #Function Call

def disp(x,y,z):
	print("{}\t{}\t{}".format(x,y,z))

disp(10,20,30) #Function Call

def disp(x,y,z,k):
	print("{}\t{}\t{}\t{}".format(x,y,z,k))


 #main program



disp(10,20,30,40) #Function Call