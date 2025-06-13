import boto3
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EnergyReadings')

# Scan all records
response = table.scan()
items = response['Items']

# Load into DataFrame
df = pd.DataFrame(items)

# Convert numeric fields from Decimal to float
numeric_fields = ['energy_generated_kwh', 'energy_consumed_kwh', 'net_energy_kwh']
for field in numeric_fields:
    df[field] = df[field].astype(float)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort
df = df.sort_values(['site_id', 'timestamp'])

# Plot
for site in df['site_id'].unique():
    site_data = df[df['site_id'] == site]
    plt.plot(site_data['timestamp'], site_data['net_energy_kwh'], label=f'{site} Net Energy')

# Highlight anomalies
anomalies = df[df['anomaly'] == True]
plt.scatter(anomalies['timestamp'], anomalies['net_energy_kwh'], color='red', label='Anomalies', zorder=5)

plt.xlabel('Timestamp')
plt.ylabel('Net Energy (kWh)')
plt.title('Net Energy Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()