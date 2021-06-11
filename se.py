import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(1) 
print('Server is running, press Ctrl+C to stop')
while True:
    conn, addr = sock.accept()
    message = conn.recv(1024)
    print(message, 'from client')
    conn.send(message.upper())
    img = open('recv_img.jpg','wb')
    byte_data = conn.recv(1024)
    while (byte_data):
        img.write(byte_data)
        byte_data = conn.recv(1024)
    img.close()
    print('img received')
conn.close()    
