#Wap which will accept list of names and sort them in both Ascending and descending orders using functions?
#sortnames.py

# Function to read names
def readnames():
	n=int(input("Enter number of values you want to enter in list: "))
	if(n<=0):
		return None
	else:
		lst=list()
		for i in range(1,n+1):
			name=input("Enter the {} value: ".format(i))
			lst.append(name)
		else:
			#print(lst)
			return lst

# Function to sort names
def sortnames(names):
	names.sort()
	print("Ascending order: ")
	displaynames(names)
	names.sort(reverse=True)
	print("Descending order: ")
	displaynames(names)

# Function to display names
def displaynames(names):
	print("-"*50)
	for name in names:
		print("\t{}".format(name))
	print("-"*50)




#main program
names=readnames() #function call
if(names==None):
	print("Invalid Input, try again")
else:
	print("Original Names:")
	displaynames(names)
	sortnames(names)