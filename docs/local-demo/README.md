# Local Employee Data Processing Demo

A small Python demonstration inspired by the data-processing workflow
described in the AWS Serverless Workflow Automation & Data Processing
team project documentation.

## What it does

- Loads fictional employee records from JSON.
- Validates required employee fields.
- Groups employees by department.
- Calculates employee counts and average salaries.
- Saves processed results as JSON.
- Includes automated unit tests.

## Project structure

- `processor.py` - reusable validation and processing functions.
- `test_processor.py` - automated unit tests.
- `data/employees.json` - fictional sample employee records.
- `data/department_summary.json` - sample processed output.

## Requirements

- Python 3.9 or later
- No third-party packages required

## Run the tests

From this directory, run:

```bash
python -m unittest -v test_processor
```

## Important note

This is a reconstructed local demonstration, not the original
team project's source code. It does not connect to AWS or implement
S3, DynamoDB, Lambda, Step Functions, SNS, AWS Glue, or Power BI.

All employee records and salary values are fictional examples.
