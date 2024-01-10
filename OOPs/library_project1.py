## library mini projet opps
import random


class Library:
    def __init__(self, list_books, name):
        self.books = list_books
        self.name = name

    def print_books(self):
        for i in enumerate(self.books):
            print(i)

    def print_available(self):
        available = self.books.copy()
        for i in available:
            print(i)

    def lend_books(self):
        name = input("Enter Your Name > ")
        num = input("Enter Your Phone Number > ")
        book = input("Enter The Book > ").title()
        if book in lended:
            return "Sorry the Book is been already lent, try to reffer another book "
        return_time = f"RETURN --> After {random.randrange(4)} days from today."
        print(return_time)
        lended.append(book)
        available.remove(book)
        print("Thankyou ")

    def return_books(self):
        name = input("Enter Your Name > ")
        num = input("Enter Your Phone Number > ")
        book = input("Enter Book > ")
        if book in lended:
            lended.remove(book)
            available.append(book)
        else:
            print("NOT REQUIRED")


list_books = [
    "Sherlock Hlomes -- Arthur Conan Doyle",
    "How I Did It -- Jack The Ripper",
    "Inspector Morse -- Colin Dexter",
    "Do Epic Shit -- Ankur Warikoo",
    "Satyenveshi Byomkesh Bakshi -- Sharadindu Bandyopadhyay",
]
janaklib = Library(list_books, "Janak")
lended = []

while True:
    print("~" * 20)
    print("(1) SHOW AVAILABLE BOOKS")
    print("(2) BORROW BOOK")
    print("(3) RETURN BOOK")
    print("(4) SHOW AVAILABLE BOOKS")
    print("~" * 20)
    ch = int(input("Enter Your Choice  (1/2/3/4) > "))
    if ch == 1:
        janaklib.print_books()

    elif ch == 2:
        janaklib.lend_books()

    elif ch == 3:
        janaklib.return_books()

    elif ch == 4:
        janaklib.print_available()
    else:
        print("Enter Valid Input")
