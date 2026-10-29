from dataclasses import asdict, dataclass

from exceptions import NotFoundError, ValidationError
from storage import JsonStorage


@dataclass
class Person:

    name: str
    email: str

    def validate_person(self):
        if not self.name.strip():
            raise ValidationError("Name cannot be empty.")

        if "@" not in self.email or "." not in self.email.split("@")[-1]:
            raise ValidationError("Invalid email address.")


@dataclass
class Member(Person):

    member_id: int
    active: bool = True

    def __post_init__(self):
        self.validate_person()

        if self.member_id <= 0:
            raise ValidationError("Member ID must be positive.")

    def to_dict(self):
        return asdict(self)


class MemberService:

    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage
        self.members = {
            item["member_id"]: Member(**item)
            for item in storage.load("members.json")
        }

    def _save(self):
        self.storage.save(
            [member.to_dict() for member in self.members.values()],
        )

    def register_member(self, member: Member):
        if member.member_id in self.members:
            raise ValidationError("Member ID already exists.")

        self.members[member.member_id] = member
        self._save()

    def get_member(self, member_id: int):
        if member_id not in self.members:
            raise NotFoundError("Member not found.")

        return self.members[member_id]

    def validate_membership(self, member_id: int):
        member = self.get_member(member_id)

        if not member.active:
            raise ValidationError("Membership is inactive.")

        return member

    def update_member(
        self, member_id: int, name: str, email: str
    ):
        old_member = self.get_member(member_id)
        updated = Member(name, email, member_id, old_member.active)
        self.members[member_id] = updated
        self._save()

    def delete_member(self, member_id: int):
        self.get_member(member_id)
        del self.members[member_id]
        self._save()