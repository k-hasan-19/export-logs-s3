# Export logs to S3

Export cloudwatch log stream from log group to S3 bucket using this lambda function

## Sample payload:

```
{
  "window_length": 2,
  "log_group_name": "<log group namespace>",
  "bucket_name": "<S3 bucket name>",
  "folder_name": "<S3 prefix/folder-name>"
}
```
