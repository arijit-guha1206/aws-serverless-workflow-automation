def validate_employees(employees):
    """Check that every employee has the required fields."""
    required_fields = {
        "employee_id",
        "name",
        "department",
        "salary"
    }

    if not isinstance(employees, list):
        raise ValueError("Employee data must be a list.")

    for employee in employees:
        if not isinstance(employee, dict):
            raise ValueError("Each employee record must be an object.")

        missing_fields = required_fields - employee.keys()

        if missing_fields:
            raise ValueError(
                f"Missing fields: {sorted(missing_fields)}"
            )

    return True


def summarize_by_department(employees):
    """Calculate employee counts and average salaries by department."""
    validate_employees(employees)

    departments = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if not isinstance(salary, (int, float)) or isinstance(salary, bool):
            raise ValueError("Employee salary must be numeric.")

        if department not in departments:
            departments[department] = []

        departments[department].append(salary)

    summary = []

    for department, salaries in departments.items():
        summary.append({
            "department": department,
            "employee_count": len(salaries),
            "average_salary": round(sum(salaries) / len(salaries), 2)
        })

    return summary
