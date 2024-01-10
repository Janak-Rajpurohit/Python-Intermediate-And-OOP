# library mini projet opps
import random


class Library:
    def __init__(self, list_books, name):
        # self.books=list_books
        self.name = name

    def print_books(self):
        for i in available:
            print(i)

    def print_available(self):
        for i in list_books:
            print(i)

    def lend_books(self):
        name = input("Enter Your Name > ")
        num = input("Enter Your Phone Number > ")
        book = input("Enter The Book > ").title()
        if book in lended:
            print("Sorry the Book is been already lent, try to reffer another book ")
            return 0
        day = random.randrange(1, 4)
        return_time = f"RETURN --> After {day} days from today."
        lended_dict[book] = [name, num, f"{day} days"]
        print(return_time)
        list_books.remove(book)
        lended.append(book)
        print("Thankyou ")

    def return_books(self):
        name = input("Enter Your Name > ")
        num = input("Enter Your Phone Number > ")
        book = input("Enter Book > ")
        if book in lended:
            lended.remove(book)
            list_books.append(book)
        else:
            print("NOT REQUIRED")

    def print_borrowers(self):
        print("BOOK >>>	BORROWERS , NUMBERS , RETURN ")
        for key, val in lended_dict.items():
            print(f"{key} >>>  {val}")

    def add_books(self):
        book = input("Enter the book to be added >>> ")
        available.append(book)
        list_books.append(book)
        print("Book Added :)")


list_books = [
    "Sherlock Hlomes -- Arthur Conan Doyle",
    "How I Did It -- Jack The Ripper",
    "Inspector Morse -- Colin Dexter",
    "Do Epic Shit -- Ankur Warikoo",
    "Satyenveshi Byomkesh Bakshi -- Sharadindu Bandyopadhyay",
]

janaklib = Library(list_books, "Janak")
lended = []
available = list_books.copy()
lended_dict = {}
while True:
    print("~" * 20)
    print("(1) SHOW ALL BOOKS")
    print("(2) BORROW BOOK")
    print("(3) RETURN BOOK")
    print("(4) SHOW AVAILABLE BOOKS")
    print("(5) SHOW BORROWERS")
    print("(6) ADD BOOK")
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

    elif ch == 5:
        janaklib.print_borrowers()

    elif ch == 6:
        janaklib.add_books()
    else:
        print("Enter Valid Input")
