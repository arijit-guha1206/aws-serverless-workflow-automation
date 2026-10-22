
import json
from pathlib import Path

from processor import validate_employees, summarize_by_department


def main():
    project_dir = Path(__file__).resolve().parent
    data_dir = project_dir / "data"

    input_file = data_dir / "employees.json"
    output_file = data_dir / "department_summary.json"

    # Load employee records
    with input_file.open("r", encoding="utf-8") as file:
        employees = json.load(file)

    # Validate and process the records
    validate_employees(employees)
    summary = summarize_by_department(employees)

    # Save the processed results
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print(f"Processed {len(employees)} employee records.")
    print(f"Department summary saved to: {output_file}")


if __name__ == "__main__":
    main()
