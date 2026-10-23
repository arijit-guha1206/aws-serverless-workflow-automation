
# AWS Serverless Workflow Architecture

This diagram represents the workflow documented in the original team project.

```mermaid
flowchart TD
    A["Amazon S3: Input employee JSON"] --> B["AWS Step Functions: Orchestration"]
    B --> C["AWS Lambda: Process records"]
    C --> D[("DynamoDB: Employees")]
    D --> E["DynamoDB Streams"]
    E --> F["AWS Lambda: Generate credentials"]
    F --> G[("DynamoDB: Credentials")]
    B --> H["Amazon SNS: Notifications"]
    F --> H
    D --> I["AWS Glue / PySpark: Batch processing"]
    G --> I
    I --> J["Power BI: Visualization"]
```

**Note:** This illustrates the architecture described in the original team project documentation. The AWS workflow is not deployed by this local demo.
