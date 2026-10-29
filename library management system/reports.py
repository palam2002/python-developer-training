from collections import Counter

from book import BookService
from issue import IssueService
from member import MemberService

class ReportService:

    def __init__(
        self,
        books: BookService,
        members: MemberService,
        issues: IssueService,
    ) -> None:
        self.books = books
        self.members = members
        self.issues = issues

    def list_available_books(self):
        return self.books.available_books()

    def list_borrowed_books(self):
        return [
            self.books.get_book(record.book_id)
            for record in self.issues.active_loans()
        ]

    def top_borrowers(self, limit: int = 5) -> list[tuple[int, int]]:
        if limit <= 0:
            return []

        counts = Counter(
            record.member_id
            for record in self.issues.records.values()
        )

        return counts.most_common(limit)

    def fine_report(self) -> list[tuple[int, int, float]]:
        return [
            (
                record.issue_id,
                record.member_id,
                self.issues.current_fine(record),
            )
            for record in self.issues.fine_report()
        ]