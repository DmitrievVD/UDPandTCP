import socket

ya_sock = socket.socket()
addr = ('5.255.255.242', 443)

ya_sock.connect(addr)