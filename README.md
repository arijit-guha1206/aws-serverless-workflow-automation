# AWS Serverless Workflow Automation & Data Processing

## Project Overview

This team project demonstrates a serverless workflow for processing employee data using AWS services, with Power BI for data visualization.

The workflow automates data ingestion, processing, notifications, and reporting by integrating multiple AWS services.

## Architecture & Workflow

1. **Amazon S3** — Stores the input JSON file containing employee data.
2. **AWS Step Functions** — Orchestrates the workflow and coordinates processing steps.
3. **AWS Lambda** — Reads JSON data from S3 and writes employee records to Amazon DynamoDB.
4. **Amazon DynamoDB** — Stores employee records and generated user credential records in separate tables.
5. **DynamoDB Streams & Lambda** — Triggers follow-up processing when employee records change.
6. **Amazon SNS** — Sends workflow success or failure notifications.
7. **AWS Glue (PySpark)** — Performs batch data processing by joining employee and user credential datasets.
8. **Power BI** — Presents employee data and processed results through visual reports.

## Technologies Used

- AWS Step Functions
- AWS Lambda
- Amazon S3
- Amazon DynamoDB and DynamoDB Streams
- Amazon SNS
- AWS Glue
- PySpark
- Power BI
- Python and Boto3

## Key Learning Areas

- Serverless workflow orchestration
- Event-driven processing
- Cloud storage and NoSQL data management
- Automated notifications
- Batch data transformation
- Data visualization and reporting

## Project Documentation

The project documentation is available here:

[View the project documentation](project_document_AWS_serverless.pdf)

## Project Type

Academic team project.

This repository currently contains the project documentation. Source code, deployment instructions, and infrastructure configuration are not included yet.

## Future Improvements

- Add organized source code and dependency documentation.
- Add sample input data with fictional employee records.
- Document setup and deployment steps.
- Add automated tests and error-handling examples.
- Improve credential handling and security practices.
- Document the data pipeline and Power BI reporting setup.

## Security Note

Do not commit AWS access keys, passwords, real employee information, or other sensitive data. Production systems should use secure credential management and appropriate access controls.
