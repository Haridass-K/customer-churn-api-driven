import os
import sys

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from prefect import flow, task

from src.preprocess import run_preprocessing
from src.eda import run_eda


@task
def preprocessing_task():
    return run_preprocessing()


@task
def eda_task(processed_data_path):
    return run_eda(processed_data_path=processed_data_path)


@flow(name="Customer Churn Data Pipeline")
def customer_churn_data_pipeline():
    processed_data_path = preprocessing_task()
    eda_task(processed_data_path)


if __name__ == "__main__":
    customer_churn_data_pipeline()