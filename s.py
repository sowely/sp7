import socket

host = 'localhost'
port = 55000
addr = (host,port)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(addr)

vid_write = open('recv_video.mp4', 'wb')

print('Server is running, press Ctrl+C to stop')
while True:
    temp, addr = udp_socket.recvfrom(8096)
    if not temp:
        break
    vid_write.write(temp)
vid_write.close()
#udp_socket.sendto(b'message received by the server', addr)
udp_socket.close()
