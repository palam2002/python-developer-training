
from employee import Employee


class EmployeeService:

    def __init__(self):
        self._employees: dict[int, Employee] = {}

    def add_employee(self, employee: Employee):
        if employee.employee_id in self._employees:
            raise ValueError("Employee ID already exists.")

        self._employees[employee.employee_id] = employee

    def get_all_employees(self) -> list[Employee]:
        #Return all employees.
        return list(self._employees.values())

    def get_employee(self, employee_id: int):
        return self._employees.get(employee_id)

    def delete_employee(self, employee_id: int):
        return self._employees.pop(employee_id, None)




