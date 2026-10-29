
from employee import Employee
from employee_service import EmployeeService


def main():
    service = EmployeeService()

    try:
        # Create employees
        employee1 = Employee(201, "Teja", 45000.0)
        employee2 = Employee(202, "Malli", 32000.0)

        # Add employees
        service.add_employee(employee1)
        service.add_employee(employee2)

        print("=== All Employees ===")
        for employee in service.get_all_employees():
            employee.display_details()
            print()

        # Search for an employee
        print("=== Search Employee ===")
        saved_employee = service.get_employee(201)

        if saved_employee is not None:
            saved_employee.display_details()
        else:
            print("Employee not found.")

        # Delete an employee
        print("\n=== Delete Employee ===")
        deleted = service.delete_employee(202)
        print("Employee deleted:", deleted)

        # Display remaining employees
        print("\n=== Remaining Employees ===")
        for employee in service.get_all_employees():
            employee.display_details()

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

