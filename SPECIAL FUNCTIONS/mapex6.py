#Wap which will accept list of employee salaries ranges from 1 to 20000 give 20% hike for those empys is >=10000 give 25% hike for those emplys whose sal <10000
#mapex6.py
import functools
print("Enter the Employee Salaries ranges 1 to 20000 seperated by space:")
lst=[float(emp) for emp in input().split()]
print(lst)
obj1=list(map(lambda emp:emp*1.25,filter(lambda emp:emp>=10000,lst)))
obj2=list(map(lambda emp:emp*1.20,filter(lambda emp:emp<10000,lst)))
print("-"*50)
print("Original List:{}".format(lst))
print("-"*50)
print("Salaries of Employees >= 10000 given 25% hike :{}".format(obj1))
print("Salaries of Employees < 10000 given 20% hike :{}".format(obj2))
print("-"*50)
sum1=functools.reduce(lambda x,y:x+y,obj1)
sum2=functools.reduce(lambda x,y:x+y,obj2)
total=sum1+sum2
print("Total salary of all employees:{}".format(total))