import socket

s = socket.socket()

"""Test connect"""
s.connect(("127.0.0.1",8080))

s.send(b"Hello")