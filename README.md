# Customer Churn Prediction using API-Driven Cloud Native Architecture

## Course

**AIMLCZG549 – API-Driven Cloud Native Solutions**

---

# Project Overview

This project implements an end-to-end API-driven cloud native machine learning solution for predicting customer churn.

The application covers the complete machine learning lifecycle including:

- Business Understanding
- Data Ingestion
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning Model Development
- MLflow Experiment Tracking (MLOps)
- Prefect Data Pipeline Automation (DataOps)
- FastAPI REST API
- Swagger & OpenAPI Documentation
- Prefect Built-in API Access

---

# Business Problem

Customer churn is one of the major challenges faced by telecommunication companies. Losing existing customers directly impacts business revenue and increases customer acquisition costs.

This project predicts whether a customer is likely to churn based on customer demographic information, service subscriptions, and billing details.

---

# Dataset

**Source**

IBM Telco Customer Churn Dataset (Kaggle)

Dataset Location

```
data/raw/customer_churn.csv
```

Processed Dataset

```
data/processed/customer_churn_processed.csv
```

---

# Project Architecture

```
Customer Churn Dataset
           │
           ▼
Data Preprocessing
           │
           ▼
Exploratory Data Analysis
           │
           ▼
Machine Learning Models
(Logistic Regression,
Random Forest,
Gradient Boosting)
           │
           ▼
Best Model Selection
(Logistic Regression)
           │
     ┌──────────────┐
     ▼              ▼
MLflow         Prefect Pipeline
(MLOps)         (DataOps)
     │              │
     └──────┬───────┘
            ▼
FastAPI REST API
            │
            ▼
Swagger / OpenAPI
            │
            ▼
Prediction Response
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.11 |
| IDE | VS Code |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| DataOps | Prefect Cloud |
| MLOps | MLflow |
| API | FastAPI |
| API Server | Uvicorn |
| Version Control | Git & GitHub |

---

# Folder Structure

```
customer-churn-api-driven
│
├── api
├── data
│   ├── raw
│   └── processed
├── flows
├── logs
├── models
├── notebooks
├── reports
├── screenshots
├── src
├── tests
├── README.md
├── requirements.txt
├── prefect.yaml
├── .gitignore
└── LICENSE
```

---

# Data Pipeline

The automated data pipeline includes:

- Data Loading
- Missing Value Handling
- Duplicate Checking
- Data Type Conversion
- Feature Encoding
- Feature Scaling
- Exploratory Data Analysis
- Report Generation

The pipeline is automated using **Prefect Cloud** and scheduled to execute every **2 minutes**.

---

# Machine Learning Models

The following classification algorithms were evaluated:

- Logistic Regression
- Random Forest
- Gradient Boosting

### Selected Model

**Logistic Regression**

---

# Final Model Performance

| Metric | Value |
|---------|--------|
| Accuracy | 0.8088 |
| Precision | 0.6667 |
| Recall | 0.5597 |
| F1 Score | 0.6085 |

---

# MLOps (MLflow)

MLflow is used for:

- Experiment Tracking
- Metric Logging
- Model Logging
- Model Comparison

Logged Metrics

- Accuracy
- Precision
- Recall
- F1 Score

Start MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

---

# DataOps (Prefect)

Prefect Cloud automates the complete data pipeline.

Pipeline includes:

- Preprocessing
- EDA
- Automated Execution
- Cloud Scheduling
- Logging
- Monitoring

Run Flow

```bash
python flows/data_pipeline_flow.py
```

Deploy Flow

```bash
prefect deploy --all
```

Run Deployment

```bash
prefect deployment run "Customer Churn Data Pipeline/customer-churn-data-pipeline"
```

---

# Built-in Prefect API

The project retrieves application details using Prefect's built-in Client API.

Retrieved Details include:

- Deployment
- Work Pool
- Flow Runs
- Flow Status

Generated Reports

```
reports/prefect_api_application_details.csv
```

```
reports/prefect_api_application_details.png
```

---

# FastAPI

Start API

```bash
uvicorn api.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

OpenAPI

```
http://127.0.0.1:8000/openapi.json
```

---

# API Endpoints

| Method | Endpoint | Description |
|----------|-----------|-------------|
| GET | / | Application Home |
| GET | /health | Health Check |
| POST | /predict | Customer Churn Prediction |

---

# Sample Prediction Response

```json
{
    "prediction": 0,
    "prediction_label": "No Churn",
    "churn_probability": 0.4882
}
```

---

# Assignment Objectives Covered

## Sub-Objective 1

- Business Understanding
- Data Ingestion
- Data Preprocessing
- Exploratory Data Analysis
- DataOps Automation using Prefect Cloud

## Sub-Objective 2

- Model Preparation
- Model Training
- Model Evaluation
- MLflow Experiment Tracking

## Sub-Objective 3

- Built-in API Access using Prefect Client API
- Display Application Details

---

# Screenshots

The project includes screenshots for:

- MLflow Experiment Tracking
- Prefect Cloud Deployment
- Prefect Cloud Completed Pipeline
- Swagger API Documentation
- Swagger Prediction Response
- OpenAPI Specification

---