import streamlit as st
import json
import os

st.set_page_config(page_title="Дашборд аналітики транспортних засобів", layout="wide")

st.title("📊 Аналітика відкритих даних МВС")
st.write("Цей дашборд відображає результати роботи мікросервісів аналізу даних.")

col1, col2 = st.columns(2)

with col1:
    st.header("🔍 Якість даних")
    if os.path.exists('/app/reports/quality_report.json'):
        with open('/app/reports/quality_report.json', 'r') as f:
            quality_data = json.load(f)
            st.json(quality_data)
    else:
        st.warning("Звіт про якість ще генерується...")

with col2:
    st.header("📈 Базова статистика")
    if os.path.exists('/app/reports/research_report.json'):
        with open('/app/reports/research_report.json', 'r') as f:
            research_data = json.load(f)
            st.write(research_data)
    else:
        st.warning("Звіт про дослідження ще генерується...")

st.divider()
st.header("🖼️ Візуалізація результатів")

vcol1, vcol2 = st.columns(2)

with vcol1:
    if os.path.exists('/app/reports/img_1.png'):
        st.image('/app/reports/img_1.png', caption='Розподіл за роком випуску')
    else:
        st.info("Перший графік ще генерується...")

with vcol2:
    if os.path.exists('/app/reports/img_2.png'):
        st.image('/app/reports/img_2.png', caption='Популярність видів палива')
    else:
        st.info("Другий графік ще генерується...")