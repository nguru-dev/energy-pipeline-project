from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://127.0.0.1:5500"] for local HTML
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EnergyReadings')

@app.get("/records")
def get_records(site_id: str, start: str, end: str):
    start_dt = datetime.fromisoformat(start)
    end_dt = datetime.fromisoformat(end)

    response = table.query(
        KeyConditionExpression=Key('site_id').eq(site_id) & Key('timestamp').between(start, end)
    )
    return response['Items']

@app.get("/anomalies")
def get_anomalies(site_id: str):
    response = table.query(
        KeyConditionExpression=Key('site_id').eq(site_id),
        FilterExpression=Attr('anomaly').eq(True)
    )
    return response['Items']
