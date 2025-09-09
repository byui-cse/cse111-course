"""
CSE 111
Lesson 12 ICE - Creating and Using a Class
Author: [Your Name Here]

Description:
Practice creating and using a simple Python class with attributes and
methods.


Instructions:
Imagine you are writing a program to help a library keep track of their
books.

Complete each of these steps:
1. Create a "Book" class to keep track of a single book. The Book class
   should keep track of a book's title, author, ISBN, and number of
   pages. The Book class should also have these methods:
   get_description(), get_ISBN(), get_author(), get_title(),
   get_pages(), and __str__().

   The __str__() method should return a string that looks like this:

   To Kill a Mockingbird (281 pages)
   Author: Harper Lee
   ISBN: 123-45-6789

   The get_description() method should return a string that looks
   like this:

   "To Kill a Mockingbird" by Harper Lee, 281 pages


2. Stretch - Add a dictionary to main() that keeps track of multiple
   books using the ISBN as the key. Add three books to the dictionary,
   then display all the books in the library like this:

   Library Inventory:

    To Kill a Mockingbird (281 pages)
    Author: Harper Lee
    ISBN: 123-45-6789

    1984 (328 pages)
    Author: George Orwell
    ISBN: 987-65-4321

    The Great Gatsby (180 pages)
    Author: F. Scott Fitzgerald
    ISBN: 111-22-3333
"""

# TODO: Define a class named Book
# Attributes: title (str), author (str), pages (int), ISBN (str)
# Methods: get_description(self) -> str, get_title(self) -> str,
# get_ISBN() -> str, get_author(self) -> str, get_pages(self) -> int,
# __str__(self) -> str
class Book:

    def __init__(self, title, author, pages, ISBN):
        """Initialize a Book object with title, author, and number of pages."""
        ... # TODO: Complete this function

    def get_description(self):
        """Return a string describing the book."""
        ... # TODO: Complete this function

    def __str__(self):
        """Return a nicely formatted string for the Book object."""
        ... # TODO: Complete this function

    # TODO: Other functions here
    ...


def main():
    # Create Book objects
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 281, "123-45-6789")
    book2 = Book("1984", "George Orwell", 328, "987-65-4321")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "111-22-3333")

    # Call the get_description method and print the result
    print(book1.get_description())

    # Use print(book1) to call the __str__ method and show the book
    # nicely formatted
    print(book1)

    # TODO: Create a dictionary of books with ISBN as the key
    ...

    # Print each book in the dictionary
    print("\nLibrary Inventory:\n")
    # TODO: Your code here
    ...


if __name__ == "__main__":
    main()
