# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 10 Assignment 2

import socket

welcome_msg = "Welcome to the chatBOT 5000 client."
print(welcome_msg)
ip = input("What is the connecting IP address: ")
port = int(input("What is the connecting port: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
    msg = input("Enter message (type 'q' to quit): ")
    client_socket.send(msg.encode())
    if msg == 'q':
        break
    response = client_socket.recv(1024).decode()
    print(f"Server sent back: {response}")

client_socket.close()
print("chatBOT 5000 client out.")