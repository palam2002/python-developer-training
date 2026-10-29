from dataclasses import asdict, dataclass

from exceptions import NotFoundError, ValidationError
from storage import JsonStorage


@dataclass
class Book:

    book_id: int
    title: str
    author: str
    year: int
    available: bool = True

    def __post_init__(self):
        if self.book_id <= 0:
            raise ValidationError("Book ID must be positive.")
        if not self.title.strip() or not self.author.strip():
            raise ValidationError("Title and author are required.")
        if self.year < 0:
            raise ValidationError("Year cannot be negative.")

    def to_dict(self):
        return asdict(self)


class BookService:

    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage
        self.books = {
            item["book_id"]: Book(**item)
            for item in storage.load("books.json")
        }

    def _save(self):
        self.storage.save(
            "books.json",
            [book.to_dict() for book in self.books.values()],
        )

    def add_book(self, book: Book):
        if book.book_id in self.books:
            raise ValidationError("Book ID already exists.")

        self.books[book.book_id] = book
        self._save()

    def get_book(self, book_id: int):
        if book_id not in self.books:
            raise NotFoundError("Book not found.")

        return self.books[book_id]

    def update_book(
        self, book_id: int, title: str, author: str, year: int
    ):
        book = self.get_book(book_id)
        updated = Book(book_id, title, author, year, book.available)
        self.books[book_id] = updated
        self._save()

    def delete_book(self, book_id: int):
        book = self.get_book(book_id)

        if not book.available:
            raise ValidationError("Return the book before deleting it.")

        del self.books[book_id]
        self._save()

    def search_books(self, query: str) -> list[Book]:
        """Search books by title or author."""
        query = query.strip().casefold()

        if not query:
            raise ValidationError("Search query cannot be empty.")

        return [
            book for book in self.books.values()
            if query in book.title.casefold()
            or query in book.author.casefold()
        ]

    def available_books(self) -> list[Book]:
        return [book for book in self.books.values() if book.available]