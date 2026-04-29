import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Використовуємо абсолютний шлях, щоб уникнути помилок FileNotFoundError
CSV_PATH = "/Users/mac/open-data-ai-analytics-Orza/data/reestrtz28.02.2026.csv"

# Налаштування сторінки
st.set_page_config(page_title="Аналітика ТЗ", layout="wide")

st.title("Аналітика реєстру транспортних засобів")

@st.cache_data
def load_data():
    # Додано sep=';' (розділювач) та on_bad_lines='skip' (пропуск пошкоджених рядків)
    return pd.read_csv(
        CSV_PATH,
        sep=';',
        low_memory=False,
        on_bad_lines='skip', # Ігнорує рядки з неправильною кількістю колонок
        encoding='utf-8'     # На всякий випадок фіксуємо кодування
    )

def visualize_data():
    st.write(f"Завантаження даних з `{CSV_PATH}`...")

    try:
        df = load_data()
        st.success("Дані успішно завантажено!")
    except FileNotFoundError:
        st.error(f"Помилка: Файл не знайдено за шляхом {CSV_PATH}")
        return
    except Exception as e:
        st.error(f"Помилка при читанні CSV: {e}")
        return

    if not df.empty:
        st.markdown("---")

        # Розміщуємо графіки у дві колонки для краси (за бажанням)
        col1, col2 = st.columns(2)

        # Графік 1: Розподіл за роком випуску (MAKE_YEAR)
        with col1:
            st.subheader("Розподіл за роком випуску")
            if 'MAKE_YEAR' in df.columns:
                fig1, ax1 = plt.subplots(figsize=(10, 5))
                year_data = pd.to_numeric(df['MAKE_YEAR'], errors='coerce').dropna()
                year_data = year_data[year_data > 1900]

                sns.histplot(year_data, bins=20, kde=True, color='skyblue', ax=ax1)
                ax1.set_xlabel('Рік випуску')
                ax1.set_ylabel('Кількість')
                st.pyplot(fig1)  # Виводимо графік на веб-сторінку
            else:
                st.warning("Колонка 'MAKE_YEAR' відсутня в даних.")

        # Графік 2: Розподіл за видом палива (FUEL)
        with col2:
            st.subheader("Топ-10 видів палива")
            if 'FUEL' in df.columns:
                fig2, ax2 = plt.subplots(figsize=(10, 5))
                fuel_counts = df['FUEL'].value_counts().head(10)
                fuel_counts.plot(kind='bar', color='salmon', ax=ax2)
                ax2.set_xlabel('Вид палива')
                ax2.set_ylabel('Кількість')
                ax2.tick_params(axis='x', rotation=45)
                st.pyplot(fig2)  # Виводимо графік на веб-сторінку
            else:
                st.warning("Колонка 'FUEL' відсутня в даних.")

        # Бонус: Виведення перших 5 рядків даних на сторінку
        st.markdown("---")
        st.subheader("Попередній перегляд даних")
        st.dataframe(df.head())

    else:
        st.warning("CSV файл порожній.")


if __name__ == "__main__":
    visualize_data()