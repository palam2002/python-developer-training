from dataclasses import asdict, dataclass
from datetime import date, timedelta

from book import BookService
from exceptions import NotFoundError, OperationError, ValidationError
from member import MemberService
from storage import JsonStorage


@dataclass
class IssueRecord:

    issue_id: int
    book_id: int
    member_id: int
    issue_date: str
    due_date: str
    return_date: str | None = None
    fine: float = 0.0

    def to_dict(self):
        return asdict(self)


class IssueService:

    def __init__(
        self,
        storage: JsonStorage,
        books: BookService,
        members: MemberService,
        loan_days: int = 14,
        fine_per_day: float = 5.0,
    ) -> None:
        if loan_days <= 0 or fine_per_day < 0:
            raise ValidationError("Invalid loan or fine settings.")

        self.storage = storage
        self.books = books
        self.members = members
        self.loan_days = loan_days
        self.fine_per_day = fine_per_day

        self.records = {
            item["issue_id"]: IssueRecord(**item)
            for item in storage.load("issues.json")
        }

        self.next_id = max(self.records, default=0) + 1

        for record in self.active_loans():
            if record.book_id in self.books.books:
                self.books.books[record.book_id].available = False

        self.books._save()

    def _save(self) -> None:
        self.storage.save(
            "issues.json",
            [record.to_dict() for record in self.records.values()],
        )

    def active_loans(self):
        return [
            record for record in self.records.values()
            if record.return_date is None
        ]

    def issue_book(self, book_id: int, member_id: int):
        book = self.books.get_book(book_id)
        self.members.validate_membership(member_id)

        if not book.available:
            raise OperationError("Book is already borrowed.")

        today = date.today()
        record = IssueRecord(
            self.next_id,
            book_id,
            member_id,
            today.isoformat(),
            (today + timedelta(days=self.loan_days)).isoformat(),
        )

        self.records[record.issue_id] = record
        self.next_id += 1
        book.available = False

        self.books._save()
        self._save()

        return record

    def return_book(self, book_id: int):
        record = next(
            (
                item for item in self.active_loans()
                if item.book_id == book_id
            ),
            None,
        )

        if record is None:
            raise NotFoundError("No active loan found for this book.")

        today = date.today()
        due_date = date.fromisoformat(record.due_date)
        late_days = max((today - due_date).days, 0)

        record.return_date = today.isoformat()
        record.fine = round(late_days * self.fine_per_day, 2)

        self.books.get_book(book_id).available = True
        self.books._save()
        self._save()

        return record

    def current_fine(self, record: IssueRecord):
        end_date = (
            date.fromisoformat(record.return_date)
            if record.return_date
            else date.today()
        )
        due_date = date.fromisoformat(record.due_date)
        late_days = max((end_date - due_date).days, 0)

        return round(late_days * self.fine_per_day, 2)

    def fine_report(self):
        today = date.today()

        return [
            record for record in self.records.values()
            if record.fine > 0
            or (
                record.return_date is None
                and today > date.fromisoformat(record.due_date)
            )
        ]