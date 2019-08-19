import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print('wait')
clientsocket, address = s.accept() #รอ client ตอบก่อนถึงจะทำอันนี้
while  True:
	print(f"Connect from {address} has been established!")
	# clientsocket.send(bytes("welcom to the server!", "utf-8")) #แปลง byte to string
	#รับจาก client
	data = clientsocket.recv(1024).decode('utf-8')
	if not data :
		break
	print("Message From Client : "+ data)
	#ส่งไป client
	data=str(data.lower())
	clientsocket.send(data.encode())
clientsocket.close()