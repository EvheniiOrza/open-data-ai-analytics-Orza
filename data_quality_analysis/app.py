import os
import pandas as pd
from sqlalchemy import create_engine
import json

DB_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DB_URL)


def analyze_quality():
    print("Аналіз якості даних...")
    df = pd.read_sql('dataset', engine)

    # ТУТ ТВІЙ КОД З 01_quality_check.ipynb
    missing_values = df.isnull().sum().to_dict()
    duplicates = int(df.duplicated().sum())

    report = {
        "missing_values": missing_values,
        "duplicates": duplicates
    }

    # Зберігаємо звіт у спільну папку
    os.makedirs('/app/reports', exist_ok=True)
    with open('/app/reports/quality_report.json', 'w') as f:
        json.dump(report, f)
    print("Звіт якості збережено!")


if __name__ == "__main__":
    analyze_quality()