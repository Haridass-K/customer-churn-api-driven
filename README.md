# Customer Churn Prediction using API-Driven Cloud Native Architecture

## Course

**AIMLCZG549 – API-Driven Cloud Native Solutions**

---

# Project Overview

This project implements an end-to-end API-driven cloud native machine learning solution for predicting customer churn.

The solution includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Machine Learning model development
- MLflow experiment tracking
- Prefect data pipeline orchestration
- FastAPI REST API
- Swagger/OpenAPI documentation

---

# Project Architecture

```
Raw Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Machine Learning Model
(Logistic Regression)
      │
      ▼
MLflow Experiment Tracking
      │
      ▼
Prefect Pipeline
      │
      ▼
FastAPI REST API
      │
      ▼
Swagger / OpenAPI
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.11 |
| IDE | VS Code |
| ML Library | Scikit-learn |
| API | FastAPI |
| API Server | Uvicorn |
| MLOps | MLflow |
| DataOps | Prefect |
| Version Control | Git & GitHub |

---

# Project Structure

```
customer-churn-api-driven/
│
├── api/
├── data/
│   ├── raw/
│   └── processed/
├── flows/
├── logs/
├── models/
├── notebooks/
├── reports/
├── screenshots/
├── src/
├── tests/
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# Dataset

Customer Churn Dataset

Raw Dataset

```
data/raw/customer_churn.csv
```

Processed Dataset

```
data/processed/customer_churn_processed.csv
```

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
|---------|---------|
| Accuracy | 0.8088 |
| Precision | 0.6667 |
| Recall | 0.5597 |
| F1 Score | 0.6085 |

---

# MLflow

Start MLflow

```bash
mlflow ui
```

Open

```
http://127.0.0.1:5000
```

---

# Prefect

Run Flow

```bash
python flows/data_pipeline_flow.py
```

Start Worker

```bash
prefect worker start --pool customer-churn-pool
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
| GET | / | Home |
| GET | /health | Health Check |
| POST | /predict | Predict Customer Churn |

---

# Prediction Response

Example

```json
{
  "prediction": 0,
  "prediction_label": "No Churn",
  "churn_probability": 0.4882
}
```

---

# Assignment Objectives Covered

- Business Understanding
- Data Preprocessing
- Exploratory Data Analysis
- Machine Learning
- Model Evaluation
- MLflow Experiment Tracking
- Prefect Pipeline
- FastAPI REST API
- Swagger Documentation
- OpenAPI Specification

---

