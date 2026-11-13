# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 10 Assignment 1

import socket

print("Welcome to the chatBOT 3000 server.")
port = int(input("What is the listening port: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', port))
server_socket.listen(1)

conn, addr = server_socket.accept()

while True:
    data = conn.recv(1024).decode()
    if not data or data == 'q':
        break
    print(f"The client said: {data}")

conn.close()
server_socket.close()
print("chatBOT 3000 server out.")