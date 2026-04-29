import pandas as pd
df = pd.read_csv('../data/reestrtz28.02.2026.csv', sep=';', encoding='utf-8')

# Топ-5 марок за кількістю реєстрацій
top_brands = df['BRAND'].value_counts().head(5)
print(top_brands)