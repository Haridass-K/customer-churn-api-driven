import os

import pandas as pd


def run_eda(
    processed_data_path="data/processed/customer_churn_processed.csv",
    reports_dir="reports"
):
    os.makedirs(reports_dir, exist_ok=True)

    df = pd.read_csv(processed_data_path)

    eda_summary = pd.DataFrame({
        "Metric": [
            "Number of Rows",
            "Number of Columns",
            "Missing Values",
            "Duplicate Records"
        ],
        "Value": [
            df.shape[0],
            df.shape[1],
            df.isnull().sum().sum(),
            df.duplicated().sum()
        ]
    })

    eda_summary.to_csv(
        os.path.join(reports_dir, "prefect_eda_summary.csv"),
        index=False
    )

    summary_statistics = df.describe().transpose()

    summary_statistics.to_csv(
        os.path.join(reports_dir, "prefect_summary_statistics.csv")
    )

    print("EDA completed successfully.")
    print(f"EDA summary saved to: {reports_dir}")

    return reports_dir


if __name__ == "__main__":
    run_eda()