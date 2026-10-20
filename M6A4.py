# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 6 Assignment 4

def show_messages(messages_list):
    temp_list = messages_list.copy()
    while temp_list:
        print(temp_list.pop())

my_messages = []

while True:
    msg = input("What is the next message? (type 'q' to quit) ")
    if msg == 'q':
        break
    my_messages.append(msg)

print("First time calling function")
show_messages(my_messages)

print("Second time calling function")
show_messages(my_messages)