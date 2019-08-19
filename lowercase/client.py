import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

f = open("demofile.txt", "r")
data = f.read()
# data = input("input : ")

s.send(data.encode('utf-8'))
# get
data=s.recv(1024).decode('utf-8')
print("Data From Server : " + data)
	
# print("ss")
n = input("new file name : ")
f = open(n + ".txt", "w")
f.write(data)
f.write("testbest")
f.close()
s.close()