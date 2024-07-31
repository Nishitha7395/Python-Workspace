#Program to copy content of one file into another
#FileCopy.py
sfile=input("Enter Source File:")
try:
	with open(sfile) as rp:
		dfile=input("Enter Destination File:")
		with open(dfile,"a") as wp:
			sfiledata=rp.read()
			wp.write(sfiledata)
			print("\n '{}' file data copied into '{}' file".format(sfile,dfile))
except FileNotFoundError:
	print("Source File Does not exist !")