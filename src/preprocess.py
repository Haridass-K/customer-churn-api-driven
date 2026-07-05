import os

import pandas as pd
from sklearn.preprocessing import StandardScaler


def run_preprocessing(
    raw_data_path="data/raw/customer_churn.csv",
    processed_data_path="data/processed/customer_churn_processed.csv",
    reports_dir="reports"
):
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    os.makedirs(reports_dir, exist_ok=True)

    df = pd.read_csv(raw_data_path)

    duplicate_count = df.duplicated().sum()

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    missing_values_before = df.isnull().sum().sum()

    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )

    missing_values_after = df.isnull().sum().sum()

    df_encoded = pd.get_dummies(
        df,
        drop_first=True
    )

    numerical_columns = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    scaler = StandardScaler()

    df_encoded[numerical_columns] = scaler.fit_transform(
        df_encoded[numerical_columns]
    )

    df_encoded.to_csv(
        processed_data_path,
        index=False
    )

    preprocessing_summary = pd.DataFrame({
        "Item": [
            "Raw Data Path",
            "Processed Data Path",
            "Rows",
            "Columns",
            "Duplicate Records",
            "Missing Values Before Imputation",
            "Missing Values After Imputation"
        ],
        "Value": [
            raw_data_path,
            processed_data_path,
            df_encoded.shape[0],
            df_encoded.shape[1],
            duplicate_count,
            missing_values_before,
            missing_values_after
        ]
    })

    preprocessing_summary.to_csv(
        os.path.join(reports_dir, "prefect_preprocessing_summary.csv"),
        index=False
    )

    print("Preprocessing completed successfully.")
    print(f"Processed data saved to: {processed_data_path}")

    return processed_data_path


if __name__ == "__main__":
    run_preprocessing()