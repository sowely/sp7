import socket

host = 'localhost'
port = 55000
addr = (host,port)

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open('video.mp4', 'rb') as vid_read:
    byte_data = vid_read.read(8096)
    while (byte_data):
        udp_socket.sendto(byte_data, addr)
        byte_data = vid_read.read(8096)
udp_socket.close()
