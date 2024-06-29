from typing import List

class LibraryItem():

    FIXED_PRICES = {200, 100, 50, 20, 10}

    def __init__(self, title: str, author: str, year: int, price: int) -> None:
        self.title = title
        self.author = author
        self.year = year
        if price not in self.FIXED_PRICES:
            raise ValueError(f"Price must be one of {self.FIXED_PRICES}")
        self.price = price

    def __str__(self) -> str:
        return f"""Title: {self.title}
Author: {self.author}
Year: {self.year}
Price: {self.price}"""



class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, price: int, isbn: int):
        super().__init__(title, author, year, price)
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{super().__str__()}, ISBN: {self.isbn}"



class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, year: int, price: int, issue_number: int):
        super().__init__(title, author, year, price)
        self.issue_number = issue_number

    def __str__(self) -> str:
        return f"{super().__str__()}, Issue Number: {self.issue_number}"



class Library():
    def __init__(self) -> None:
        self.items: List[LibraryItem] = []

    def add_item(self, item: LibraryItem) -> None:
        self.items.append(item)

    def add_item_from_input(self) -> None:
        try:
            item_type = int(input("""Select item type (1/2):
                             [1]Book
                             [2]Magazine """))
            title = str(input("Enter Title: ")).lower().strip()
            author = str(input("Enter Author Name: ")).lower().strip()
            year = int(input("Enter Publish Year: ").strip())
            price = int(input("Enter Price: ").strip())
            nums = ["1", "2"]
            if item_type not in nums:
                raise ValueError(f"Invalid output. Valid numbers: 1,2")
            elif item == 1:
                isbn = input("Enter ISBN: ").strip()
                item = Book(title, author, year, price, isbn)
            elif item_type == 2:
                issue_number = int(input("Enter issue number: ").strip())
                item = Magazine(author, year, price, issue_number)
            else:
                raise ValueError("Invalid or missing input")
            self.add_item(item)
        except Exception as e:
            return e

    def remove_item(self, title: str) -> None:
        self.items = [item for item in self.items if item.title != title]

    def find_item(self, title) -> list[LibraryItem]:
        for item in self.items:
            if item.title == title:
                return item
        return False
        
    def list_items(self):
        for item in self.items:
            print(item)

    def get_old_books(self) -> List[Book]:
        for item in self.items:
            if isinstance(item, Book) and item.year < 1990:
                print(item)

    def print_books(self, sorted: bool = False) -> None:
        books = [item for item in self.items if isinstance(item, Book)]
        if sorted:
            books.sort(key=lambda x: x.title) 

        for book in books:
            print(book)

    def books_by_budget(self, budget: int) -> List[Book]:
        books = [item for item in self.items if isinstance(item, Book)]
        books.sort(key=lambda x: x.price)
        result = []
        total_price = 0
        for book in books:
            if total_price + book.price <= budget:
                result.append(book)
                total_price += book.price
            else:
                break
        if total_price > budget:
            raise ValueError("Cannot find books within the given budget.")
        return result




library = Library()

book1 = Book("Candide", "Voltaire", 1759, 200, "9788494224768")
book2 = Book("Churchill Factor", "Boris Johnson", 2014, 50, "9803qhf074tq043t")
book3 = Book("Thus Spoke Zarathustra", "Friedrich Nietzsche", 1883, 100, "sdfsdf4444445sd")
    
magazine1 = Magazine("National Geographic", "Various Authors", 2024, 50, 1234)

books = [book1, book2, book3, magazine1]    

for i in books:
    library.add_item(i)
    print(f"\n{i}")


print("\nFinding Churchill Factor")
print(library.find_item("Churchill Factor"))

print("\nListing items:")
print(library.list_items())

print("\nListing old items")
print(library.get_old_books())

print("\nAll books (sorted by title):")
library.print_books(sorted=True)

try:
    books_within_budget = library.books_by_budget(150)
    print("Books within budget:")
    for book in books_within_budget:
        print(book)
except ValueError as e:
    print(e)
