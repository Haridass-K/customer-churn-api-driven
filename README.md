# Customer Churn Prediction using API-Driven Cloud Native Architecture

## Course

**AIMLCZG549 – API-Driven Cloud Native Solutions**

---

# Project Overview

This project presents an end-to-end API-driven cloud-native machine learning solution for predicting customer churn in the telecommunications domain.

The application implements the complete machine learning lifecycle, including data preprocessing, exploratory data analysis, model development, experiment tracking, workflow orchestration, REST API development, and cloud deployment.

The project integrates DataOps, MLOps, and API-driven cloud-native technologies using Prefect Cloud, MLflow, FastAPI, and Render.

---

# Business Problem

Customer churn is one of the major challenges faced by telecommunication companies. Losing existing customers directly impacts business revenue and increases customer acquisition costs.

This project predicts whether a customer is likely to churn based on customer demographics, subscribed services, contract information, and billing details, enabling organizations to take proactive customer retention measures.

---

# Dataset

**Dataset:** IBM Telco Customer Churn Dataset

**Source:** Kaggle

Raw Dataset

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
 MLflow      Prefect Pipeline
 (MLOps)         (DataOps)
     │              │
     └──────┬───────┘
            ▼
      FastAPI REST API
            │
            ▼
      Render Cloud
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
| IDE | Visual Studio Code |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| DataOps | Prefect Cloud |
| MLOps | MLflow |
| REST API | FastAPI |
| API Server | Uvicorn |
| Cloud Deployment | Render |
| API Documentation | Swagger UI & OpenAPI |
| Version Control | Git & GitHub |

---

# Project Folder Structure

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

The automated data pipeline performs:

- Data Loading
- Missing Value Analysis
- Duplicate Detection
- Data Type Conversion
- Feature Encoding
- Feature Scaling
- Exploratory Data Analysis
- Report Generation

The workflow is automated using **Prefect Cloud** and scheduled to execute every **2 minutes**.

---

# Machine Learning Models

The following classification models were evaluated:

- Logistic Regression
- Random Forest
- Gradient Boosting

### Selected Model

**Logistic Regression**

### Final Performance

| Metric | Value |
|---------|-------|
| Accuracy | 0.8088 |
| Precision | 0.6667 |
| Recall | 0.5597 |
| F1 Score | 0.6085 |

---

# MLOps (MLflow)

MLflow is used for:

- Experiment Tracking
- Parameter Logging
- Metric Logging
- Model Comparison
- Model Artifact Management

Logged Metrics

- Accuracy
- Precision
- Recall
- F1 Score

Run MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

---

# DataOps (Prefect Cloud)

The Prefect workflow automates:

- Data Preprocessing
- Exploratory Data Analysis
- Scheduled Execution
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

The application retrieves deployment information using Prefect's built-in Client API.

Retrieved Information includes:

- Deployment Details
- Work Pool Details
- Flow Run Details
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

Run the API locally

```bash
uvicorn api.main:app --reload
```

Local Swagger

```
http://127.0.0.1:8000/docs
```

Local OpenAPI

```
http://127.0.0.1:8000/openapi.json
```

---

# Cloud Deployment (Render)

The FastAPI application has been successfully deployed on **Render Cloud** as a Python Web Service.

### Live Application

https://customer-churn-api-driven.onrender.com

### Swagger UI

https://customer-churn-api-driven.onrender.com/docs

### OpenAPI Specification

https://customer-churn-api-driven.onrender.com/openapi.json

The cloud deployment allows users to access the application directly through a web browser without requiring local installation.

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

- FastAPI REST API
- Swagger & OpenAPI Documentation
- Built-in Prefect API Access
- Application Detail Retrieval

---

# Screenshots

The repository includes screenshots demonstrating:

- Overall Project Architecture
- Data Preprocessing
- Correlation Heatmap
- Feature Importance
- Prefect Cloud Deployment
- Prefect Completed Pipeline
- MLflow Experiment Tracking
- Swagger API Documentation
- Swagger Prediction Response
- OpenAPI Specification
- Prefect Built-in API Details
- Render Cloud Deployment
- Live Prediction using Render

---
# Reproducing the Project

If all project files cannot be uploaded to the Taxila portal due to upload size limitations, the complete project is available in this GitHub repository.

## Clone Repository

```bash
git clone https://github.com/Haridass-K/customer-churn-api-driven.git
```

Navigate to the project directory

```bash
cd customer-churn-api-driven
```

---

## Activate Environment

This project was developed using a Conda environment.

```bash
conda activate customer-churn
```

If the environment is not available, install the dependencies using:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## 1. Start FastAPI

```bash
uvicorn api.main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

Open OpenAPI Specification

```
http://127.0.0.1:8000/openapi.json
```

---

## 2. Start MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

MLflow provides:

- Experiment Tracking
- Model Comparison
- Metric Logging
- Model Artifact Management

---

## 3. Start Prefect Server

```bash
prefect server start
```

Open Prefect Dashboard

```
http://127.0.0.1:4200
```

For first-time local setup configure the API endpoint:

```bash
prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
```

---

## 4. Start Prefect Worker

```bash
prefect worker start --pool customer-churn-pool
```

The worker listens for scheduled deployments and executes workflow runs.

---

## 5. Execute Prefect Deployment

Run the deployed DataOps workflow

```bash
prefect deployment run "Customer Churn Data Pipeline/customer-churn-data-pipeline"
```

The workflow automatically performs:

- Data Loading
- Data Preprocessing
- Exploratory Data Analysis
- Workflow Logging
- Monitoring
- Scheduled Execution

The workflow can also be executed directly:

```bash
python flows/data_pipeline_flow.py
```

---

## 6. Built-in Prefect API

Run

```bash
python src/prefect_api_details.py
```

This retrieves:

- Deployment Details
- Work Pool Details
- Flow Run Details
- Flow Status

Generated reports

```
reports/prefect_api_application_details.csv
```

```
reports/prefect_api_application_details.png
```

---

# Cloud Deployment

The FastAPI application has been successfully deployed on **Render Cloud**.

Live Application

https://customer-churn-api-driven.onrender.com

Swagger UI

https://customer-churn-api-driven.onrender.com/docs

OpenAPI

https://customer-churn-api-driven.onrender.com/openapi.json

The deployed cloud application provides the same prediction API demonstrated locally and can be accessed directly through a web browser without requiring local installation.

---

# Screenshots

The repository includes screenshots demonstrating:

- Overall Project Architecture
- Data Preprocessing
- Correlation Heatmap
- Feature Importance
- Prefect Deployment Dashboard
- Prefect Work Pool
- Prefect Completed Flow Run
- Prefect Task Execution
- MLflow Experiment Tracking
- Swagger API Documentation
- Swagger Prediction Response
- OpenAPI Specification
- Prefect Built-in API Details
- Render Cloud Deployment
- Live Prediction using Render

---

# GitHub Repository

https://github.com/Haridass-K/customer-churn-api-driven

---

# Note

Due to file size limitations on the Taxila portal, the complete implementation is maintained in this GitHub repository.

The repository contains:

- Source Code
- Datasets
- Machine Learning Models
- Jupyter Notebooks
- Prefect Workflows
- MLflow Integration
- FastAPI Application
- Render Cloud Deployment
- Reports
- Screenshots
- Project Documentation

The project can be fully reproduced by following the steps provided in the **Reproducing the Project** section above.