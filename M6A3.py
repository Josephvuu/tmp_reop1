# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 6 Assignment 3

def make_album(artist, album_title, numsongs='None'):
    return {
        'artist': artist,
        'title': album_title,
        'number of songs': numsongs
    }

while True:
    title = input("What is the title of the album (or q for quit)? ")
    if title == 'q':
        break
    
    artist = input("What is the name of the artist? ")
    album_dict = make_album(artist, title)
    print(album_dict)
    