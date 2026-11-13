class Book:
    def __init__(self, title, copies=1):
        self.title = title
        # Stores copy count privately
        self.__copies = copies

    def get_copies(self):
        return self.__copies

    def add_copy(self):
        self.__copies += 1

    def remove_copy(self):
        if self.__copies > 0:
            self.__copies -= 1
            return True
        return False

    def __str__(self):
        # Defines __str__ representation
        return f"'{self.title}' (Copies available: {self.__copies})"

class Library:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title):
        # Combines duplicate titles by increasing copies
        if title in self.inventory:
            self.inventory[title].add_copy()
        else:
            self.inventory[title] = Book(title)
        print(f"Added a copy of '{title}'.")

    def list_books(self):
        # Lists books
        print("\n--- Library Inventory ---")
        for book in self.inventory.values():
            print(book)
        print("-------------------------\n")

    def borrow_book(self, title):
        # Refuses borrowing when no copies remain
        if title in self.inventory and self.inventory[title].remove_copy():
            print(f"Successfully borrowed '{title}'.")
        else:
            print(f"Borrowing refused: No copies of '{title}' remain.")

    def return_book(self, title):
        # Supports returns
        if title in self.inventory:
            self.inventory[title].add_copy()
        else:
            self.inventory[title] = Book(title)
        print(f"Successfully returned '{title}'.")
