# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 10 Assignment 1

import socket

print("Welcome to the chatBOT 3000 client.")
port = int(input("What is the connecting port: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', port))

while True:
    msg = input("Enter message (type 'q' to quit): ")
    client_socket.send(msg.encode())
    if msg == 'q':
        break

client_socket.close()
print("chatBOT 3000 client out.")

