from dotenv import load_dotenv
import os
import boto3
import pandas as pd
from io import StringIO


def save_csvs_from_s3_to_folder(bucket, prefix, save_to_path):

    # Load environment variables from .env
    load_dotenv()

    # Read credentials from environment
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    region_name = os.getenv('AWS_DEFAULT_REGION')    

    # Initialize S3 client using loaded credentials
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

    csv_keys = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.csv')]

    # Choose one CSV file
    for csv_key in csv_keys:
        # Get the file from S3
        obj = s3.get_object(Bucket=bucket, Key=csv_key)
        body = obj['Body'].read().decode('utf-8')

        # Load into pandas
        df = pd.read_csv(StringIO(body))
        df.to_csv(f'{save_to_path}/{csv_key.replace(prefix, '')}', index = False)