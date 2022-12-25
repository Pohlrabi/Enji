import socket

"""Create a socket"""
s = socket.socket()

"""Bind the above socket to a specific address"""
s.bind(("127.0.0.1",8080))

"""Listen to any connection"""
s.listen()

"""Accept any connection attemp"""
client_socket, client_address = s.accept()

data = client_socket.recv(1024)

print(data)
