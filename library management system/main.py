from book import Book
from exceptions import LibraryError
from library import Library
from member import Member


def main():
    library = Library()

    while True:
        print("""
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add book
2. Update book
3. Delete book
4. Search books
5. List all books
6. Register member
7. Update member
8. Delete member
9. Issue book
10. Return book
11. Available books report
12. Borrowed books report
13. Top borrowers report
14. Fine report
0. Exit
""")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                book = Book(
                    int(input("Book ID: ")),
                    input("Title: ").strip(),
                    input("Author: ").strip(),
                    int(input("Publication year: ")),
                )
                library.books.add_book(book)
                print("Book added successfully.")

            elif choice == "2":
                book_id = int(input("Book ID: "))
                title = input("New title: ").strip()
                author = input("New author: ").strip()
                year = int(input("New year: "))

                library.books.update_book(
                    book_id, title, author, year
                )
                print("Book updated successfully.")

            elif choice == "3":
                library.books.delete_book(
                    int(input("Book ID: "))
                )
                print("Book deleted successfully.")

            elif choice == "4":
                query = input("Enter title or author: ")
                results = library.books.search_books(query)

                for book in results:
                    print(book.book_id, book.title, book.author)

                if not results:
                    print("No books found.")

            elif choice == "5":
                for book in library.books.books.values():
                    status = "Available" if book.available else "Borrowed"
                    print(
                        f"{book.book_id} | {book.title} | "
                        f"{book.author} | {status}"
                    )

            elif choice == "6":
                member = Member(
                    input("Name: ").strip(),
                    input("Email: ").strip(),
                    int(input("Member ID: ")),
                )
                library.members.register_member(member)
                print("Member registered successfully.")

            elif choice == "7":
                member_id = int(input("Member ID: "))
                name = input("New name: ").strip()
                email = input("New email: ").strip()

                library.members.update_member(
                    member_id, name, email
                )
                print("Member updated successfully.")

            elif choice == "8":
                library.members.delete_member(
                    int(input("Member ID: "))
                )
                print("Member deleted successfully.")

            elif choice == "9":
                record = library.issues.issue_book(
                    int(input("Book ID: ")),
                    int(input("Member ID: ")),
                )
                print("Book issued. Due date:", record.due_date)

            elif choice == "10":
                record = library.issues.return_book(
                    int(input("Book ID: "))
                )
                print(f"Book returned. Fine: ₹{record.fine:.2f}")

            elif choice == "11":
                for book in library.reports.list_available_books():
                    print(book.book_id, book.title)

            elif choice == "12":
                for book in library.reports.list_borrowed_books():
                    print(book.book_id, book.title)

            elif choice == "13":
                for member_id, count in library.reports.top_borrowers():
                    member = library.members.members.get(member_id)
                    name = member.name if member else str(member_id)
                    print(f"{name}: {count} loan(s)")

            elif choice == "14":
                reports = library.reports.fine_report()

                if not reports:
                    print("No fines to report.")

                for issue_id, member_id, fine in reports:
                    print(
                        f"Issue: {issue_id}, Member: {member_id}, "
                        f"Fine: ₹{fine:.2f}"
                    )

            elif choice == "0":
                print("Thank you for using the library system.")
                break

            else:
                print("Invalid choice. Try again.")

        except (ValueError, LibraryError, RuntimeError) as error:
            print("Error:", error)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting the library system.")
            break


if __name__ == "__main__":
    main()