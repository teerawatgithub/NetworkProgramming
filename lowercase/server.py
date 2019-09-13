import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("wait for cilent send request")
clientsocket, address = s.accept() #รอ client ตอบก่อนถึงจะทำอันนี้
while  True:
	#รับจาก client
	data = clientsocket.recv(1024).decode('utf-8')
	if not data :
		break
	else:
		print(f"Connect from {address} has been established!")

	print("Message From Client : "+ data)
	q = input("change to lowercase (Y/N): ")	
	if q == "Y" or q == "y" or q == "Yes" or q == "yes" or q == "YES":
		#ทำให้เป็น lower
		data=str(data.lower())
		#ส่งไป client
		print(f"lower is {data} sended to client")
		clientsocket.send(data.encode())
	else:
		clientsocket.send(data.encode())

clientsocket.close()