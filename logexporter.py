import boto3
from datetime import datetime, timedelta
import math
import time


def lambda_handler(event, context):
    log_file = boto3.client("logs")
    window_in_days_from_today = event['window_length']
    start_window = datetime.now()
    end_window = datetime.now() - timedelta(days=window_in_days_from_today)
    print("Starting from: ", start_window)
    print("Ending at: ", end_window)
    startOf_start_window_Day = start_window.replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    endOf_end_window_Day = end_window.replace(
        hour=23, minute=59, second=59, microsecond=999999
    )
    group_name = event['log_group_name']
    
    response = log_file.create_export_task(
        taskName='export_task_{}'.format(time.time()),
        logGroupName=group_name,
        fromTime=math.floor(endOf_end_window_Day.timestamp() * 1000),
        to=math.floor(startOf_start_window_Day.timestamp() * 1000),
        destination=event['bucket_name'],
        destinationPrefix=event['folder_name'],
    )
    return response
