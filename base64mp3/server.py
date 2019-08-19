import socket
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print('wait')
dataFull = ""
clientsocket, address = s.accept()
while True:
    # send to client
    # print(f"Connect from {address} has been established!")
    # clientsocket.send(bytes("welcom to the server!", "utf-8")) #แปลง byte to string
    # รับจาก client
    data = clientsocket.recv(1024)
    if not data:
        break
    # print(type(data))
    data1 = repr(data.decode())
    data1 = data1[1:len(data1)-1]
    dataFull = dataFull + data1


namePhoto = input("Name photo : ")
imgdata = base64.b64decode(dataFull)
filename = namePhoto + '.mp3'  # I assume you have a way of picking unique filenames
with open("C:\\Users\\waran\\Desktop\\alex\\network\\python\\base64mp3\\server\\" + filename, 'wb') as f:
    f.write(imgdata)
    print('successful!')
    # # ส่งไป client
    # data = str(data.lower())
    # clientsocket.send(data.encode())
clientsocket.close()
