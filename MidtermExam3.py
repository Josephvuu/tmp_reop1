# Name: Joseph Vu
# Student ID: 887091577
# Section: 07
# Assignment: MidtermExam3

def make_book(book_title, book_author, book_length=100):
    return {'title': book_title, 'author': book_author, 'length': book_length}

firstbook = make_book('Ulysses' , 'James Boyce' , 762)
secondbook = make_book(book_title='The Odyssey', book_author='Homer')

print(f"{firstbook}")
print(f"{secondbook}")


