# Mini Project: Library Management System

## 1. Project Overview

The **Library Management System** is a Python-based mini project developed using Object-Oriented Programming (OOP) concepts.

The main purpose of this project is to manage library operations such as adding books, registering members, issuing books, returning books, calculating late fees, and generating reports.

This application follows a modular architecture, where each Python file is responsible for a specific functionality.

The system uses JSON files for permanent data storage and implements exception handling, input validation, type hints, and docstrings to improve code quality and maintainability.

---

## 2. Project Objectives

The objectives of this project are:

- To understand and implement OOP concepts in Python.
- To develop a modular Python application.
- To manage books and library members.
- To issue and return books.
- To calculate late return fines.
- To generate library reports.
- To store and retrieve data using JSON files.
- To implement exception handling.
- To validate user input.
- To follow PEP 8 coding standards.
- To demonstrate SOLID principles.

---

## 3. Functional Requirements

### 3.1 Book Management Module

The Book module manages all book-related operations.

**Features:**

**1. Add Book**
- Add new books to the library.
- Store book ID, title, author, and availability.
- Prevent duplicate book IDs.
- Validate book information.

**2. Update Book**
- Update book title.
- Update book author.
- Update book information using book ID.
- Validate updated information.

**3. Delete Book**
- Delete books using their unique ID.
- Check whether the book exists.
- Prevent deletion if the book is currently issued.

**4. Search Book**
- Search books using book ID.
- Search books using book title.
- Display complete book information.

**5. Track Availability**
- Check whether a book is available.
- Change availability when a book is issued.
- Make the book available when it is returned.

### 3.2 Member Management Module

The Member module manages library members.

**Features:**

**1. Register Member**
- Register new library members.
- Store member ID and member name.
- Set membership status to active.
- Prevent duplicate member IDs.

**2. Update Member**
- Update member details.
- Search members using member ID.

**3. Delete Member**
- Delete registered members.
- Check whether the member exists.
- Prevent deletion if the member has active borrowed books.

**4. Validate Membership**
- Verify member registration.
- Check membership status.
- Allow book issuing only to active members.

### 3.3 Issue Management Module

The Issue module handles book issuing and returning operations.

**Features:**

**1. Issue Book**
- Verify book availability.
- Validate member registration.
- Check active membership.
- Record book issue date.
- Calculate due date.
- Update book availability.
- Store issue information.

**2. Return Book**
- Identify the active issue record.
- Record the return date.
- Calculate overdue days.
- Calculate applicable fines.
- Update book availability.

**3. Fine Calculation**

The system calculates fines when a book is returned after its due date.

**Fine Formula:**

Fine = Late Days × Fine Per Day

**Example:**

- Issue Date: 1 October 2026
- Due Date: 15 October 2026
- Return Date: 20 October 2026
- Late Days: 5
- Fine Per Day: ₹5

Total Fine = 5 × 5 = ₹25

If the book is returned before or on the due date, no fine is charged.

### 3.4 Report Management Module

The Reports module generates library reports.

**Features:**

**1. Available Books Report**
- Display all available books.
- Show book ID, title, and author.

**2. Borrowed Books Report**
- Display all currently issued books.
- Show book and member details.

**3. Top Borrowers Report**
- Identify members who have borrowed the highest number of books.
- Display member names.
- Display total borrowing counts.
- Sort borrowers by borrowing count.

**4. Fine Report**
- Display members with outstanding fines.
- Display individual fine amounts.
- Calculate total fines.

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OOP | Organize code using classes and objects |
| JSON | Store and retrieve data |
| Exception Handling | Handle application errors |
| Type Hints | Improve code readability |
| Docstrings | Explain classes and methods |
| PEP 8 | Follow Python coding standards |
| unittest | Test application functionality |
| Git | Track source code changes |
| GitHub | Host the project repository |

---

## 5. Project Folder Structure

The project follows a modular architecture. Each Python file has a specific responsibility.

```text
library_management/
│
├── app.py
├── book.py
├── member.py
├── issue.py
├── reports.py
├── storage.py
├── exceptions.py
├── validator.py
├── README.md
│
└── data/
    ├── books.json
    ├── members.json
    └── issues.json
```

### Explanation of Files

**1. app.py**
- Main entry point of the application.
- Displays the library management menu.
- Accepts user input.
- Connects all modules.
- Executes selected operations.

**2. book.py**
- Contains the Book class.
- Add books.
- Update book details.
- Delete books.
- Search books.
- Track book availability.

**3. member.py**
- Contains the Member class.
- Register members.
- Update member information.
- Delete members.
- Validate membership.

**4. issue.py**
- Handles book issuing and returning.
- Maintains issue dates and due dates.
- Calculates late return days.
- Calculates fines.
- Updates book availability.

**5. reports.py**
- Displays available books.
- Displays borrowed books.
- Identifies top borrowers.
- Generates fine reports.

**6. storage.py**
- Handles JSON file operations.
- Saves book information.
- Saves member information.
- Saves issue records.
- Loads previously stored data.

**7. exceptions.py**
- Contains custom exception classes.
- Handles book-related errors.
- Handles member-related errors.
- Handles invalid issue and return operations.

**8. validator.py**
- Validates user input.
- Checks book IDs and member IDs.
- Validates names and titles.
- Prevents invalid data.
- Checks positive numeric values.

**9. README.md**
- Contains project documentation.
- Explains project features.
- Describes OOP concepts.
- Provides installation and execution instructions.

**10. data/**
- Stores application data using JSON files.

**books.json:** Stores book details and availability.

**members.json:** Stores member information and membership status.

**issues.json:** Stores book issue records, due dates, return dates, and fines.

---

## 6. Object-Oriented Programming Concepts

This project demonstrates practical OOP concepts using real-world library management examples.

### 6.1 Classes and Objects

A class is a blueprint used to create objects.

An object is an instance of a class.

**Practical Example:**

The Book class represents library books. Each book object stores its own information.

```python
class Book:

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str
    ):

        self.book_id = book_id
        self.title = title
        self.author = author


book1 = Book(101, "Python Programming", "Guido")

print(book1.title)
```

**Explanation:**
- Book is a class.
- book1 is an object.
- book_id, title, and author are attributes.
- __init__ initializes the object.

### 6.2 Encapsulation

Encapsulation means combining data and methods inside a class and controlling access to internal data.

**Practical Example:**

```python
class Book:

    def __init__(self, title: str):
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str):
        if title.strip():
            self.__title = title


book = Book("Python")

print(book.get_title())
```

**Explanation:**
- __title is a private attribute.
- get_title() retrieves the title.
- set_title() updates the title after validation.
- Internal data is accessed through methods.

### 6.3 Inheritance

Inheritance allows one class to reuse the attributes and methods of another class.

**Practical Example:**

```python
class Person:

    def __init__(self, name: str):
        self.name = name


class Member(Person):

    def display(self):
        print("Member Name:", self.name)


member = Member("Ravi")
member.display()
```

**Explanation:**
- Person is the parent class.
- Member is the child class.
- Member inherits the name attribute from Person.

### 6.4 Multiple Inheritance

Multiple inheritance allows a child class to inherit from more than one parent class.

**Practical Example:**

```python
class Person:

    def personal_details(self):
        print("Personal details")


class LibraryAccess:

    def library_access(self):
        print("Library access granted")


class Member(Person, LibraryAccess):
    pass


member = Member()

member.personal_details()
member.library_access()
```

**Explanation:**
- Member inherits from Person and LibraryAccess.
- It can access methods from both parent classes.

### 6.5 Multilevel Inheritance

Multilevel inheritance occurs when a class inherits from another child class.

**Practical Example:**

```python
class Person:

    def show_name(self):
        print("Person information")


class LibraryUser(Person):
    pass


class Member(LibraryUser):
    pass


member = Member()
member.show_name()
```

**Explanation:**

Inheritance chain:

Person → LibraryUser → Member

Member receives methods from both parent levels.

### 6.6 Hierarchical Inheritance

Hierarchical inheritance occurs when multiple child classes inherit from one parent class.

**Practical Example:**

```python
class Person:

    def display(self):
        print("Person details")


class Member(Person):
    pass


class Librarian(Person):
    pass


member = Member()
librarian = Librarian()

member.display()
librarian.display()
```

**Explanation:**
- Person is the parent class.
- Member and Librarian are child classes.
- Both inherit the display method.

### 6.7 Polymorphism

Polymorphism means one method name can perform different behaviours depending on the object.

**Practical Example:**

```python
class Report:

    def generate(self):
        print("General report")


class FineReport(Report):

    def generate(self):
        print("Fine report")


class BorrowedReport(Report):

    def generate(self) -> None:
        print("Borrowed books report")


reports = [
    FineReport(),
    BorrowedReport()
]

for report in reports:
    report.generate()
```

**Explanation:**
- All classes use the generate() method.
- Each child class implements different behaviour.
- This demonstrates method overriding and polymorphism.

### 6.8 Abstraction

Abstraction hides implementation details and exposes only essential functionality.

**Practical Example:**

```python
from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def save(self, data: list):
        pass


class JSONStorage(Storage):

    def save(self, data: list):
        print("Saving data into JSON")


storage = JSONStorage()
storage.save([])
```

**Explanation:**
- Storage is an abstract class.
- save() is an abstract method.
- JSONStorage implements the abstract method.
- The user interacts with the storage interface without needing to know every implementation detail.

### 6.9 Composition

Composition represents a relationship in which one object contains references to other objects.

**Practical Example:**

```python
class Issue:

    def __init__(self, book: Book, member: Member):
        self.book = book
        self.member = member
```

**Explanation:**
- Issue contains a Book object.
- Issue contains a Member object.
- This connects different modules of the application.

---

## 7. JSON-Based Data Storage

JSON stands for JavaScript Object Notation.

It is a lightweight format used to store and exchange data.

This project uses JSON files to store library information permanently.

### 7.1 books.json

Example:

```json
[
    {
        "book_id": 101,
        "title": "Python Programming",
        "author": "john",
        "available": true
    },
    {
        "book_id": 102,
        "title": "Object Oriented Programming",
        "author": "Lucky",
        "available": false
    }
    {
        "book_id": 3,
        "title": "Data Structures",
        "author": "Mahesh",
        "available": false
    }
]
```

### 7.2 members.json

Example:

```json
[
    {
        "member_id": 1,
        "name": "Malli",
        "email": "malli@example.com"
    },
    {
        "member_id": 2,
        "name": "Kumar",
        "email": "chinnu@example.com"
    }
]
```

### 7.3 issues.json

Example:

```json
[
    {
        "issue_id": 1,
        "book_id": 102,
        "member_id": 1,
        "issue_date": "2026-9-23",
        "due_date": "2026-10-27",
        "return_date": null,
        "fine": 0
    }
    {
         "issue_id": 2,
        "book_id": 1,
        "member_id": 102,
        "issue_date": "2026-10-10",
        "due_date": "2026-10-17",
        "return_date": "2026-10-18",
        "fine": 10
    }
]
```

### 7.4 Saving JSON Data

Python provides a built-in json module.

Example:

```python
import json

data = [
    {
        "book_id": 101,
        "title": "Python",
        "author": "Guido"
    }
]

with open("books.json", "w") as file:
    json.dump(data, file, indent=4)
```

### 7.5 Loading JSON Data

```python
import json

with open("books.json", "r") as file:
    data = json.load(file)

print(data)
```

**Benefits of JSON storage:**
- Simple to understand.
- Easy to read and modify.
- No external database required.
- Supports permanent data storage.
- Allows data to be retrieved when the application restarts.

The application should load existing data when it starts and save changes after successful operations.

---

## 8. Exception Handling

Exception handling prevents the application from crashing when unexpected errors occur.

The project uses built-in and custom exceptions.

### Custom Exceptions

| Exception | Purpose |
|---|---|
| BookNotFoundError | Book does not exist |
| MemberNotFoundError | Member does not exist |
| BookUnavailableError | Book is already issued |
| InvalidMembershipError | Membership is inactive |
| DuplicateBookError | Book ID already exists |
| DuplicateMemberError | Member ID already exists |
| ActiveLoanError | Book or member has an active loan |
| InvalidIssueError | Issue or return operation is invalid |

### Example: Custom Exception

```python
class BookNotFoundError(Exception):
    """Raised when a requested book is not found."""
    pass
```

### Example: Handling Exceptions

```python
try:
    raise BookNotFoundError("Book not found")

except BookNotFoundError as error:
    print(error)
```

**Benefits:**
- Handles invalid operations.
- Improves application reliability.
- Provides meaningful error messages.
- Prevents unexpected program termination.

---

## 9. Input Validation

Input validation ensures that users enter correct information before processing.

The validator.py module is responsible for validating user input.

### Validation Rules

1. Book ID must be a positive integer.
2. Member ID must be a positive integer.
3. Book ID must be unique.
4. Member ID must be unique.
5. Book title cannot be empty.
6. Author name cannot be empty.
7. Member name cannot be empty.
8. Fine amount cannot be negative.
9. A book cannot be issued if unavailable.
10. Inactive members cannot borrow books.
11. A book cannot be returned without an active issue record.
12. A book with an active loan cannot be deleted.

**Example:**

```python
def validate_name(name: str) -> bool:
    """Validate a name."""

    if not name.strip():
        return False

    return True
```

Input validation improves data accuracy and prevents invalid operations.

---

## 10. SOLID Principles

SOLID principles help developers build maintainable, reusable, and scalable applications.

### S – Single Responsibility Principle (SRP)

A class should have only one main responsibility.

**Example:**
- Book handles book information.
- Member handles member information.
- Issue handles borrowing and returning.
- Reports handles report generation.
- Storage handles JSON operations.

Each module has a separate responsibility.

### O – Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification.

**Example:**

New report types can be added by creating additional report classes without modifying existing report implementations.

### L – Liskov Substitution Principle (LSP)

Child classes should be usable wherever their parent classes are expected without breaking functionality.

**Example:**

Different report classes should implement the same report interface and behave correctly when used in place of the base report type.

### I – Interface Segregation Principle (ISP)

A class should not be forced to implement methods it does not need.

**Example:**

Use separate interfaces for storage operations, report generation, and other independent operations instead of creating one large interface.

### D – Dependency Inversion Principle (DIP)

High-level modules should depend on abstractions rather than concrete implementations.

**Example:**

Book and member services should use a storage abstraction rather than directly depending on JSON file operations.

---

## 11. Application Workflow

The general application workflow is:

1. Start the application.
2. Load existing data from JSON files.
3. Display the library management menu.
4. Accept user input.
5. Validate the selected operation.
6. Execute the requested operation.
7. Handle exceptions if an error occurs.
8. Save successful changes to JSON.
9. Display the result.
10. Continue until the user exits.

### Main Menu Example

```text
========================================
        LIBRARY MANAGEMENT SYSTEM
========================================

1. Add Book
2. Update Book
3. Delete Book
4. Search Book
5. Display All Books

6. Register Member
7. Update Member
8. Delete Member
9. Display All Members

10. Issue Book
11. Return Book

12. Available Books Report
13. Borrowed Books Report
14. Top Borrowers Report
15. Fine Report

16. Exit

Enter your choice:
```

---

## 12. Installation and Setup

### Prerequisites

- Python 3.10 or above.
- Visual Studio Code or another Python IDE.
- Git.
- GitHub account.

### Step 1: Create the Project Folder

```bash
mkdir library_management
cd library_management
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

### Step 4: Create the Project Files

Create these Python files:

```text
app.py
book.py
member.py
issue.py
reports.py
storage.py
exceptions.py
validator.py
```

Create a data folder containing:

```text
books.json
members.json
issues.json
```

The JSON files can initially contain empty arrays:

```json
[]
```

### Step 5: Run the Application

```bash
python app.py
```

No external packages are required for the basic application because it uses Python standard library modules.

---

## 13. Testing

Testing ensures that the application works correctly.

The project can use Python's built-in unittest framework.

### Test Cases

| Test Case | Expected Result |
|---|---|
| Add a book | Book added successfully |
| Add duplicate book | Duplicate book error |
| Search a book | Book details displayed |
| Update a book | Book information updated |
| Delete a book | Book deleted |
| Register member | Member registered |
| Register duplicate member | Duplicate member error |
| Validate membership | Membership status checked |
| Issue available book | Book issued successfully |
| Issue unavailable book | Error displayed |
| Issue to inactive member | Issuing rejected |
| Return book | Book returned successfully |
| Return late book | Fine calculated |
| Save JSON | Data saved successfully |
| Load JSON | Existing data retrieved |
| Generate reports | Correct reports displayed |

### Run Tests

If a tests folder is added later, run:

```bash
python -m unittest discover -s tests -v
```

### Manual Verification

The following steps can also verify core functionality:

1. Add a book.
2. Close the application.
3. Restart the application.
4. Search for the previously added book.
5. Register a member.
6. Issue an available book.
7. Try issuing the same book again.
8. Return the book.
9. Check the availability status.
10. Generate the reports.

The saved information should remain available after restarting the application.

---

## 14. Code Quality Standards

The project follows Python coding standards.

### PEP 8

PEP 8 is the official Python style guide.

The project should follow these practices:

- Use meaningful variable names.
- Use lowercase names with underscores for functions and variables.
- Use PascalCase for class names.
- Use four spaces for indentation.
- Keep lines reasonably short.
- Avoid unnecessary duplicate code.
- Use proper spacing.

### Type Hints

Type hints describe the expected data types of variables and functions.

Example:

```python
def calculate_fine(
    late_days: int,
    fine_per_day: float
) -> float:

    return late_days * fine_per_day
```

### Docstrings

Docstrings explain the purpose of classes and methods.

Example:

```python
class Book:
    """Represent a library book."""

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str
    ) -> None:
        """Initialize book information."""

        self.book_id = book_id
        self.title = title
        self.author = author
```

### Code Quality Verification

Install pycodestyle:

```bash
python -m pip install pycodestyle
```

Run:

```bash
pycodestyle .
```

---

## 15. Git and GitHub Submission

Git is used to track project changes, while GitHub is used to host the source code.

### Step 1: Initialize Git

```bash
git init
```

### Step 2: Add Project Files

```bash
git add .
```

### Step 3: Commit Project Structure

```bash
git commit -m "Create library management project structure"
```

### Step 4: Implement and Commit Modules

Use meaningful commit messages:

```bash
git add .
git commit -m "Implement book management operations"

git add .
git commit -m "Implement member registration and validation"

git add .
git commit -m "Implement book issue and return functionality"

git add .
git commit -m "Add fine calculation and report generation"

git add .
git commit -m "Implement JSON data storage"

git add .
git commit -m "Add custom exceptions and input validation"

git add .
git commit -m "Add project documentation"
```

### Step 5: Push to GitHub

```bash
git branch -M main

git remote add origin <your-repository-url>

git push -u origin main
```

---

## 16. Project Evaluation Checklist

Before submitting the project, verify the following requirements.

### OOP Concepts

- [ ] Classes and objects implemented.
- [ ] Encapsulation implemented.
- [ ] Inheritance implemented.
- [ ] Multiple inheritance demonstrated.
- [ ] Multilevel inheritance demonstrated.
- [ ] Hierarchical inheritance demonstrated.
- [ ] Polymorphism implemented.
- [ ] Method overriding implemented.
- [ ] Abstraction implemented.
- [ ] Composition implemented.

### Functional Requirements

- [ ] Add books.
- [ ] Update books.
- [ ] Delete books.
- [ ] Search books.
- [ ] Track book availability.
- [ ] Register members.
- [ ] Update members.
- [ ] Delete members.
- [ ] Validate membership.
- [ ] Issue books.
- [ ] Return books.
- [ ] Calculate late returns.
- [ ] Calculate fines.
- [ ] Generate available books report.
- [ ] Generate borrowed books report.
- [ ] Identify top borrowers.
- [ ] Generate fine reports.

### Technical Requirements

- [ ] Modular architecture.
- [ ] JSON-based storage.
- [ ] JSON data retrieval.
- [ ] Custom exception handling.
- [ ] Input validation.
- [ ] Type hints.
- [ ] Docstrings.
- [ ] PEP 8 standards.
- [ ] SOLID principles.
- [ ] Testing or repeatable verification steps.
- [ ] GitHub repository updated.

---

## 17. Future Enhancements

The project can be extended with additional features:

- Admin login and authentication.
- Member login.
- Book reservation functionality.
- Search books by category.
- Email notifications for due dates.
- Graphical user interface using Tkinter.
- Database integration using SQLite or MySQL.
- Export reports to CSV or PDF.
- Automatic membership expiry notifications.

---

## 18. Expected Project Outcome

After completing this project, the application should be able to:

- Manage books and members.
- Track book availability.
- Issue and return books.
- Calculate late return fines.
- Generate library reports.
- Store information permanently using JSON.
- Handle errors using exception handling.
- Validate user input.
- Demonstrate practical OOP concepts.
- Follow SOLID principles.
- Maintain clean and reusable Python code.

---

## 19. Conclusion

The Library Management System is a practical Python OOP mini project that demonstrates how real-world applications can be developed using classes, objects, inheritance, encapsulation, polymorphism, abstraction, and composition.

It also provides practical experience with JSON file handling, exception handling, input validation, type hints, docstrings, modular architecture, and SOLID principles.

This project improves Python programming skills and provides a foundation for developing larger software applications.

### Project Information

| Detail | Description |
|---|---|
| Project Name | Library Management System |
| Story | Story 4 – Mini Project |
| Programming Language | Python |
| Storage | JSON |
| Architecture | Modular OOP |
| Coding Standard | PEP 8 |
| Testing | unittest |
| Purpose | Educational Mini Project |

**End of Documentation**