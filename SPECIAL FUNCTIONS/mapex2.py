#mapex2.py
hike=lambda sal:sal*1.02 #anonymous function
#main program
oldsallist=[10,20,5,30,40]
obj=map(hike,oldsallist)
print("Type of obj=",type(obj)) #<class, 'Map'>
print(obj)
newsallist=list(obj)
print("Old Salary List={}".format(oldsallist))
print("New Salary List={}".format(newsallist))