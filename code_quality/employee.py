
class Employee:

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float
    ):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive.")

        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display_details(self) -> None:
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary:.2f}")

