import json
from pathlib import Path

from processor import validate_employees, summarize_by_department


def main():
    project_dir = Path(__file__).resolve().parent
    data_dir = project_dir / "data"

    input_file = data_dir / "employees.json"
    output_file = data_dir / "department_summary.json"

    with input_file.open("r", encoding="utf-8") as file:
        employees = json.load(file)

    validate_employees(employees)
    summary = summarize_by_department(employees)

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)

    print(f"Processed {len(employees)} employee records.")
    print(f"Department summary saved to: {output_file}")


if __name__ == "__main__":
    main()
