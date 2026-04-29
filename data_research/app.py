import os
import pandas as pd
from sqlalchemy import create_engine
import json

DB_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DB_URL)


def research_data():
    print("Дослідження даних...")
    df = pd.read_sql('dataset', engine)

    # ТУТ ТВІЙ КОД З 02_research.ipynb.py
    stats = df.describe().to_dict()

    os.makedirs('/app/reports', exist_ok=True)
    with open('/app/reports/research_report.json', 'w') as f:
        json.dump(stats, f)
    print("Результати дослідження збережено!")


if __name__ == "__main__":
    research_data()