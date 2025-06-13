# ⚡ Energy Pipeline Project

A real-time, cloud-native energy data pipeline built on **AWS**, featuring live ingestion, anomaly detection, API access, and interactive visualization — all orchestrated and deployed via **Terraform** and Python.

---

## 🚀 Overview

This project simulates energy meter data flowing through an automated AWS pipeline. As data lands in S3, a **Lambda function** processes and stores it into **DynamoDB**, where it can be queried through a **FastAPI** service and visualized using **Matplotlib** and **Plotly Dash** (HTML).

You can simulate energy records, detect anomalies, analyze trends, and view it all through APIs and a browser dashboard.

---

## 🧱 Architecture

```
Data Simulator (Python) ───► S3 (Trigger) ───► Lambda ───► DynamoDB
                                          │
                                          ▼
                                  FastAPI (GET/summary, GET/site)
                                          │
                                          ▼
                                 Frontend Dashboard (Plotly HTML)
```

---

## ⚙️ Technologies Used

- **AWS S3** – Stores incoming `.json` energy files  
- **AWS Lambda** – Parses, flags, and saves to DynamoDB  
- **AWS DynamoDB** – NoSQL store for processed data  
- **Terraform** – Infrastructure as Code (S3, Lambda, IAM, Trigger)  
- **FastAPI** – REST APIs to expose metrics  
- **Python** – Core logic, ingestion scripts, visualization  
- **Matplotlib / Plotly** – Trend graphs & anomaly charts  
- **GitHub Actions** – CI/CD (Optional)  
- **SNS Alerts** – Notifies for negative energy records (Extra Credit)  

---

## 📦 Features

- ✅ Simulated energy data generated every 5 minutes
- ✅ Lambda calculates net energy, flags anomalies
- ✅ DynamoDB stores structured readings with metadata
- ✅ FastAPI exposes endpoints:
  - `/site/{site_id}` – raw data  
  - `/summary/{site_id}` – record count, avg, anomaly count  
- ✅ Frontend dashboard visualizes trends
- ✅ Terraform manages entire stack

---

## 📁 Project Structure

```
├── simulate_energy_upload.py         # Pushes simulated data to S3
├── lambda_function.py                # Triggered by S3 uploads
├── energy_api.py                     # FastAPI app
├── visualize_energy_data.py          # Local plotter
├── terraform/
│   ├── main.tf                       # Infra resources
├── frontend.html                     # Dashboard UI
├── .gitignore
├── README.md
```

---

## 🛠 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/nguru-dev/energy-pipeline-project.git
   ```

2. Deploy AWS Infra:
   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

3. Simulate data to S3:
   ```bash
   python simulate_energy_upload.py
   ```

4. Run API server:
   ```bash
   uvicorn energy_api:app --reload
   ```

5. Open dashboard:
   ```
   frontend.html → open in browser
   ```

---

## 📈 Sample Output

> 🟢 `Uploaded energy_...json with 10 records to s3://energy-data-bucket-guru/raw/`  
> 🛑 Detected anomaly: Net energy = -2.41 kWh  
> ✅ API GET `/summary/site-1`: 50 records | 3 anomalies | Avg: 1.02 kWh

---

## 🎯 Extra Credit Done

- ✅ SNS alert for negative energy  
- ✅ Terraform-managed infra  
- ✅ Hosted frontend dashboard (S3 static site)  
- ✅ CI/CD via GitHub Actions (Optional pipeline available)  

---

## 👤 Author

**Nguru Sai**  
AWS | Data Engineering | Python | FastAPI | Terraform  
[GitHub: @nguru-dev](https://github.com/nguru-dev)

---

## 📌 License

MIT License – use freely with credit!