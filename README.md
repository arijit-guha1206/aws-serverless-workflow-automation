# AWS Serverless Workflow Automation & Data Processing
![Python Tests](https://github.com/arijit-guha1206/aws-serverless-workflow-automation/actions/workflows/python-tests.yml/badge.svg)

A team project exploring serverless employee-data processing using AWS services, complemented by a runnable local Python demonstration and automated tests.

## Project Overview

The original team project documents an event-driven workflow for processing employee data, generating user credentials, sending notifications, performing batch transformations, and visualizing results.

This repository also contains a **local Python demo** that validates sample employee records, summarizes employee data by department, and runs automated unit tests through GitHub Actions.

## Architecture Documented in the Original Team Project

The project documentation describes the following workflow:

1. **Amazon S3** — Stores the input JSON file containing employee data.
2. **AWS Step Functions** — Orchestrates the workflow and coordinates processing steps.
3. **AWS Lambda** — Reads employee data from S3 and writes records to Amazon DynamoDB.
4. **Amazon DynamoDB** — Stores employee records and generated user-credential records in separate tables.
5. **DynamoDB Streams and Lambda** — Trigger follow-up processing when employee records change.
6. **Amazon SNS** — Sends workflow success or failure notifications.
7. **AWS Glue and PySpark** — Perform batch processing by joining employee and credential datasets.
8. **Power BI** — Visualizes employee data and processed results.

## Local Python Demo

The `local-demo/` directory contains a runnable Python implementation of a small employee-data processing workflow.

### Features

- Loads employee records from a JSON file.
- Validates required employee fields.
- Groups employee records by department.
- Calculates department-level employee counts and average salaries.
- Writes the generated summary to a JSON file.
- Includes automated unit tests for validation and aggregation.
- Runs the demo and tests automatically through GitHub Actions.

### Technologies

- Python
- JSON
- `unittest`
- GitHub Actions

### Project Structure

```text
aws-serverless-workflow-automation/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── docs/
│   └── README.md
├── local-demo/
│   ├── data/
│   │   ├── employees.json
│   │   └── department_summary.json
│   ├── main.py
│   ├── processor.py
│   ├── test_processor.py
│   └── README.md
├── .gitignore
├── README.md
└── project_document_AWS_serverless.pdf
```

## Run the Local Demo

**Requirements:** Python 3.9 or later.

Open a terminal in the repository directory and run:

```bash
cd local-demo
python main.py
```

To run the automated tests:

```bash
python -m unittest -v test_processor
```

The demo reads `data/employees.json` and generates `data/department_summary.json`.

## Continuous Integration

A GitHub Actions workflow runs when changes are pushed to the `main` branch or a pull request targets `main`. It:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Runs the employee-processing demo.
4. Executes the automated unit tests.

The workflow has been run successfully in GitHub Actions.

## Scope and Limitations

The AWS architecture above reflects the original team project's documentation. The runnable implementation currently provided in this repository is a **local Python demo**; it does not deploy or connect to AWS services.

The local demo uses fictional sample employee data. AWS integrations, credential generation, notifications, Glue processing, and Power BI dashboards are not implemented by the local demo.

## Key Learning Areas

- Serverless architecture and workflow orchestration
- Event-driven processing concepts
- JSON data validation and transformation
- Department-level data aggregation
- Unit testing
- Continuous integration with GitHub Actions


**Architecture diagram:** [View the workflow diagram](docs/architecture.md)
