#ClientChat.py
import socket # Step-1

print("-"*40)
while(True):
	s=socket.socket() # Step-2
	s.connect(("localhost",8888))
	#Step-3
	cMsg=input("Student-->")
	if(cMsg.lower()=="bye"):
		s.send(cMsg.encode())
		break
	else:
		s.send(cMsg.encode())
		#Step-4
		sMsg=s.recv(1024).decode()
		print("Professor--> {}".format(sMsg))
		print("-"*40)
