import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('',55000))

sock.send(b'hello!')
message = sock.recv(1024)

img = open ("img.jpg", "rb")
byte_data = img.read(1024)
while (byte_data):
    sock.send(byte_data)
    byte_data = img.read(1024)
sock.close()

print(message,'from server')

