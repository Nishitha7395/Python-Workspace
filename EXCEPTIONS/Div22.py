#Program for accepting two integer values and find their division
#Div22.py
try:
	s1=input("Enter First Value: ")
	s2=input("Enter Second Value: ")
	#s3=s1/s2--invalid process
	a=int(s1) #------X
	b=int(s2) #------X
	c=a/b #----------X	
	s="PYTHON"
	print(s[11])
except ZeroDivisionError:
	print("\nDo not enter Zero for Denominator")
except ValueError:
	print("\nDo not enter strs / symbols / alphanumerics")
except IndexError:
	print("string index out of range please correct it")
except Exception as e:
	print("\nOOPS something went wrong",e)
except :
	print("\nSomething went wrong")
else:
	print('-'*20)
	print("Value of a=",a)
	print("VAlue of b=",b)
	print("Div=",c)
	print('-'*20)

finally:
	print("\nI am from finally block")