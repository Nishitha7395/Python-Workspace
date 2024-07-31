#Wap which will calculate Area and perimeter of Square
#areaandperimeterofsquare.py

#APPROACH-1
# INPUT from Function Calls
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaandperimeterofsquare(side):
	area = side*side
	perimeter=4*side
	return area,perimeter

#Main Program - Approach-1
side=int(input("Enter the Side of a Square: "))
area=areaandperimeterofsquare(side)
print("Area of Square: {}".format(area[0]))
print("Perimeter of Square: {}".format(area[1]))


#APPROACH-2
# INPUT taking in Function Body
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaandperimeterofsquare():
	side=int(input("Enter the Side of a Square: "))
	area = side*side
	perimeter=4*side
	print("Area of Square: {}".format(area))
	print("Perimeter of Square: {}".format(perimeter))

#Main Program - Approach-2

areaandperimeterofsquare()



#APPROACH-3
# INPUT taking in Function Calls
# PROCESSING done in Function Body
# RESULT given in Function Body

def areaandperimeterofsquare(side):
	area = side*side
	perimeter=4*side
	print("Area of Square: {}".format(area))
	print("Perimeter of Square: {}".format(perimeter))

#Main Program - Approach-3
side=int(input("Enter the Side of a Square: "))
areaandperimeterofsquare(side)



#APPROACH-4
# INPUT taken in Function Body
# PROCESSING done in Function Body
# RESULT gives to Function Call

def areaandperimeterofsquare():
	side=int(input("Enter the Side of a Square: "))
	area = side*side
	perimeter=4*side
	return side,area,perimeter

#Main Program - Approach-4

side,area,perimeter=areaandperimeterofsquare()
print("Area of Square = Side: {}* Side {} = {}".format(side,side,area))
print("Perimeter of Square = 4* Side:{} = {}".format(side,perimeter))
area = areaandperimeterofsquare()
print("Area of Square = Side: {}* Side {} = {}".format(area[0],area[0],area[1]))
print("Perimeter of Square = 4* Side:{} = {}".format(area[0],area[2]))


""" Approach-1 --------> Function with Parameters and with Return Type
	Approach-2 --------> Function without Parameters and without Return Type
    Approach-3 --------> Function with Parameters and without Return Type
    Approach-4 --------> Function without Parameters and with Return Type  """