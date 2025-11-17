# ---------- Core library functions ----------

def list_books(library):
    return library["books"]


def add_book(library, title, author, year, tags=None):
    if tags is None:
        tags = []

    # simple id generation
    new_id = max([b["id"] for b in library["books"]] or [0]) + 1

    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": True,
        "tags": tags,
    }
    library["books"].append(book)
    return book


def find_book_by_id(library, book_id):
    matches = [b for b in library["books"] if b["id"] == book_id]
    return matches[0] if matches else None


def search_books(library, query):
    q = query.lower()
    return [
        b for b in library["books"]
        if q in b["title"].lower() or q in b["author"].lower()
    ]


def borrow_book(library, book_id):
    book = find_book_by_id(library, book_id)
    if book is None:
        return False, "Book not found."
    if not book["available"]:
        return False, "Book already borrowed."
    book["available"] = False
    return True, f'You borrowed "{book["title"]}".'


def return_book(library, book_id):
    book = find_book_by_id(library, book_id)
    if book is None:
        return False, "Book not found."
    if book["available"]:
        return False, "Book was not borrowed."
    book["available"] = True
    return True, f'You returned "{book["title"]}".'


def input_int(prompt):
    while True:
        value = input(prompt)
        if not value.strip():
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Invalid number, try again.")


def input_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required.")


def main():
    # Starting library data
    library = {
        "name": "My Library",
        "books": [
            {
                "id": 1,
                "title": "Dune",
                "author": "Frank Herbert",
                "year": 1965,
                "available": True,
                "tags": ["sci-fi", "classic"],
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "available": False,
                "tags": ["dystopian"],
            },
        ]
    }

    while True:
        print("\n=== Library Menu ===")
        print("1. List books")
        print("2. Add book")
        print("3. Search books")
        print("4. Borrow book")
        print("5. Return book")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            books = list_books(library)
            if not books:
                print("No books in the library yet.")
            else:
                for b in books:
                    status = "Available" if b["available"] else "Borrowed"
                    print(f'[{b["id"]}] {b["title"]} by {b["author"]} '
                          f'({status}, {b["year"]})')

        elif choice == "2":
            title = input_nonempty("Title: ")
            author = input_nonempty("Author: ")
            year = input_int("Year: ")
            tags_raw = input("Tags (comma separated, optional): ").strip()
            tags = [t.strip() for t in tags_raw.split(",")] if tags_raw else []
            book = add_book(library, title, author, year, tags)
            print(f'Added: [{book["id"]}] {book["title"]}')

        elif choice == "3":
            query = input_nonempty("Search term: ")
            results = search_books(library, query)
            if not results:
                print("No matching books found.")
            else:
                for b in results:
                    status = "Available" if b["available"] else "Borrowed"
                    print(f'[{b["id"]}] {b["title"]} by {b["author"]} ({status})')

        elif choice == "4":
            book_id = input_int("Book ID to borrow: ")
            success, msg = borrow_book(library, book_id)
            print(msg)

        elif choice == "5":
            book_id = input_int("Book ID to return: ")
            success, msg = return_book(library, book_id)
            print(msg)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
