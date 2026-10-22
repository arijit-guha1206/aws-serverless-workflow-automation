# Local Employee Data Processing Demo

A small Python demonstration inspired by the data-processing workflow described in the AWS Serverless Workflow Automation & Data Processing team-project documentation.

## Features

- Loads fictional employee records from JSON.
- Validates required employee fields.
- Groups employees by department.
- Calculates employee counts and average salaries.
- Writes processed summaries to JSON.
- Includes automated unit tests.

## Project Structure

```text
local-demo/
├── data/
│   ├── employees.json
│   └── department_summary.json
├── main.py
├── processor.py
├── test_processor.py
└── README.md
```

## Requirements

- Python 3.9 or later
- No third-party Python packages required

## Run the Demo

Open a terminal in the `local-demo` directory and run:

```bash
python main.py
```

The script reads `data/employees.json`, processes the records, and writes the results to `data/department_summary.json`.

## Run the Tests

```bash
python -m unittest -v test_processor
```

The tests check valid employee records, department summary calculations, and rejection of records with missing required fields.

## Scope and Limitations

This is a reconstructed local demonstration inspired by the original team project's documentation. It is not the original project source code and does not connect to AWS.

AWS services such as S3, Lambda, Step Functions, DynamoDB, SNS, and Glue, along with Power BI, are not implemented in this demo.

All employee records and salary values are fictional sample data.
