# ⚡ Energy Pipeline Project

A scalable AWS-based energy data pipeline that simulates real-time energy readings, processes them using AWS Lambda, stores them in DynamoDB, and exposes analytics via a FastAPI interface.

---

## 🚀 Project Overview

This project is part of a Data Engineering assignment and includes the following:

- 🔁 **Data Simulation**: Python script to generate JSON data for multiple energy sites.
- ☁️ **Data Ingestion**: Upload data to S3 with event triggers.
- 🧠 **Real-Time Processing**: AWS Lambda parses JSON and writes to DynamoDB.
- 📊 **Analytics & Visualization**: Python script to visualize trends and anomalies using Matplotlib.
- 🌐 **REST API**: FastAPI app to expose data endpoints from DynamoDB.

---

## 🧰 Tech Stack

- **AWS S3, Lambda, DynamoDB**
- **Python, Boto3**
- **FastAPI, Uvicorn**
- **Pandas, Matplotlib**

---

## 🔧 How to Run Locally

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn boto3 pandas matplotlib
   ```

2. Run the API:
   ```bash
   uvicorn energy_api:app --reload
   ```

3. Use Postman or browser to call:
   - `http://127.0.0.1:8000/energy-data`
   - `http://127.0.0.1:8000/anomalies`

---

## 📂 Project Structure

```
energy_pipeline_project/
├── simulate_energy_upload.py       # Generates and uploads JSON data to S3
├── energy_api.py                   # FastAPI app for data access
├── visualize_energy_data.py        # Visualization of trends/anomalies
└── README.md
```

---

## 👨‍💻 Author

- GitHub: [nguru-dev](https://github.com/nguru-dev)
