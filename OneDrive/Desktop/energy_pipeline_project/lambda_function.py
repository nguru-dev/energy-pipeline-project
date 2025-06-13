import json
import boto3
from decimal import Decimal

s3 = boto3.client('s3')
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EnergyReadings')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    records = json.loads(content)

    print(f"📦 Read {len(records)} records from {key}")

    for record in records:
        site_id = record.get('site_id')
        timestamp = record.get('timestamp')
        gen = Decimal(str(record.get('energy_generated_kwh', 0)))
        con = Decimal(str(record.get('energy_consumed_kwh', 0)))
        net = gen - con
        anomaly = gen < 0 or con < 0

        if anomaly:
            sns.publish(
                TopicArn="arn:aws:sns:us-east-2:919313849757:anomaly-alerts",
                Subject="🚨 Energy Anomaly Detected",
                Message=f"Site: {site_id}, Timestamp: {timestamp}, Net Energy: {net} kWh"
            )

        print(f"📤 Writing: {site_id} at {timestamp} | net={net} | anomaly={anomaly}")

        table.put_item(Item={
            'site_id': site_id,
            'timestamp': timestamp,
            'energy_generated_kwh': gen,
            'energy_consumed_kwh': con,
            'net_energy_kwh': net,
            'anomaly': anomaly
        })

    return {
        'statusCode': 200,
        'body': f'Processed {len(records)} records from {key}'
    }
