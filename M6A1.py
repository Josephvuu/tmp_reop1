# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: Module 6 Assignment 1

def favorite_book(book_title):
    print(f"One of my favorite books is {book_title}")

for _ in range(3):
    title = input("What is your favorite book? ")
    favorite_book(title)
    