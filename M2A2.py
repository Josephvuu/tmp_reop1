# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 2 Assignment 2

g_list = ['Mortal Kombat' , 'Contra' , 'Streets Of Rage' , 'Shinobi' , 'Sonic' , 'Phantasy Star']

print("Here are the top Sega games: ")

for item in g_list:
    print(item)

remove_game = input("Which one do you think should be removed? ")

if remove_game in g_list:
    g_list.remove(remove_game)

    print("Here are the new top Sega games:")

    for item in g_list:
        print(item)
