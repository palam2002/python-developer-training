from book import BookService
from issue import IssueService
from member import MemberService
from reports import ReportService
from storage import JsonStorage


class Library:

    def __init__(self, data_dir: str = "data"):
        self.storage = JsonStorage(data_dir)
        self.books = BookService(self.storage)
        self.members = MemberService(self.storage)
        self.issues = IssueService(
            self.storage,
            self.books,
            self.members,
        )
        self.reports = ReportService(
            self.books,
            self.members,
            self.issues,
        )