import boto3
import json
import time
import random
from datetime import datetime
import uuid

s3 = boto3.client('s3')
bucket_name = 'energy-data-bucket-guru'  
prefix = 'raw/'

def generate_energy_data():
    sites = ['site_A', 'site_B', 'site_C']
    records = []

    for site in sites:
        record = {
            "site_id": site,
            "timestamp": datetime.utcnow().isoformat(),
            "energy_generated_kwh": round(random.uniform(-5, 100), 2),
            "energy_consumed_kwh": round(random.uniform(-5, 100), 2)
        }
        records.append(record)
    
    return records

def upload_to_s3():
    data = generate_energy_data()
    filename = f"energy_{int(time.time())}.json"
    s3.put_object(
        Bucket=bucket_name,
        Key=prefix + filename,
        Body=json.dumps(data)
    )
    print(f"✅ Uploaded {filename} to s3://{bucket_name}/{prefix}")

if __name__ == "__main__":
    upload_to_s3()
