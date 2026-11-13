# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 10 Assignment 3

import socket

host = input("What is the hostname? ")
print("Here is the HTML:")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, 80))

req = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
s.sendall(req.encode())

response = b""
while True:
    data = s.recv(4096)
    if not data:
        break
    response += data

s.close()

print(response.decode(errors='ignore'))