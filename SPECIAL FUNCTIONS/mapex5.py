#mapex5.py
print("Enter list of elements seperated by space:")
lst=[int(val) for val in input().split()]
possqlist=list(map(lambda n:n**2,list(filter(lambda val:val>0,lst))))

negsqlist=tuple(map(lambda n:n**2,tuple(filter(lambda val:val<0,lst))))
print("\nOriginal List={}".format(lst))
print("\nPositive Square List={}".format(possqlist))
print("\nNegative Square List={}".format(negsqlist))



