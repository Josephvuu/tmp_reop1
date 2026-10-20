# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: MidtermExam2

book_dict = {
    'Ulysses': 'James Joyce',
    'Don Quixote': 'Miguel de Cervantes',
    'One Hundred Years of Solitude': 'Gabriel Garcia Marquez',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'Hamlet': 'William Shakespeare',
    'The Odyssey': 'Homer',
    'Madame Bovary': 'Gustave Flaubert',
}

for book, author in book_dict.items():
    print(f"The book {book} was written by {author}")

fav_book = input("What is your favorite book? ")

if fav_book in book_dict:
    print(f"The author of {fav_book} is {book_dict[fav_book]}")

