import socket
import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

with open("vans.jpg", "rb") as imageFile:
    data = base64.b64encode(imageFile.read())
    # print(data)
    s.send(data)
s.close()
