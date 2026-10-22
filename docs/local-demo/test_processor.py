import unittest

from processor import validate_employees, summarize_by_department


class TestEmployeeProcessor(unittest.TestCase):

    def setUp(self):
        # Small test dataset with fictional employees
        self.employees = [
            {
                "employee_id": "E101",
                "name": "Aarav Sharma",
                "department": "Engineering",
                "salary": 60000
            },
            {
                "employee_id": "E102",
                "name": "Priya Das",
                "department": "Analytics",
                "salary": 55000
            },
            {
                "employee_id": "E103",
                "name": "Rohan Sen",
                "department": "Engineering",
                "salary": 65000
            }
        ]

    def test_validation_accepts_valid_records(self):
        self.assertTrue(validate_employees(self.employees))

    def test_department_counts_and_averages(self):
        summary = summarize_by_department(self.employees)

        # Convert the list to a dictionary for easy comparison
        result = {
            item["department"]: item
            for item in summary
        }

        self.assertEqual(result["Engineering"]["employee_count"], 2)
        self.assertEqual(result["Engineering"]["average_salary"], 62500.0)

        self.assertEqual(result["Analytics"]["employee_count"], 1)
        self.assertEqual(result["Analytics"]["average_salary"], 55000.0)

    def test_missing_required_field_is_rejected(self):
        invalid_employees = [
            {
                "employee_id": "E104",
                "name": "Test User",
                "department": "Engineering"
                # Salary is intentionally missing
            }
        ]

        with self.assertRaises(ValueError):
            validate_employees(invalid_employees)


if __name__ == "__main__":
    unittest.main()
