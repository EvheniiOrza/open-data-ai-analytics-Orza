import os
import pandas as pd
from sqlalchemy import create_engine

DB_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DB_URL)


def load_data():
    print("Завантаження даних...")
    # Твій CSV лежить у папці /app/data (ми її прокинемо через compose)
    # Зверни увагу на сепаратор ';' який ми бачили раніше
    df = pd.read_csv('/app/data/reestrtz28.02.2026.csv', sep=';', low_memory=False)

    # Записуємо в БД. Змінено на append для масштабованості.
    df.to_sql('dataset', engine, if_exists='append', index=False)
    print(f"Успішно завантажено {len(df)} записів в БД!")


if __name__ == "__main__":
    load_data()