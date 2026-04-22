import streamlit as st

st.set_page_config(page_title="Цифровий Тетіїв", page_icon="🏛️")

st.title("🏛️ Тетіїв у смартфоні")
st.subheader("Офіційний сервіс громади")

menu = ["🏠 Головна", "📋 Документи", "🏥 Запис до лікаря", "🛠️ Комунальна варта"]
choice = st.sidebar.selectbox("Меню", menu)

if choice == "🏠 Головна":
    st.write("Ласкаво просимо! Оберіть послугу в меню зліва.")
    st.info("📌 ЦНАП працює: Пн-Пт 08:00 - 17:00")

elif choice == "📋 Документи":
    st.header("Замовлення довідок")
    name = st.text_input("Ваше ПІБ")
    doc = st.selectbox("Тип документа", ["Довідка про склад сім'ї", "Витяг про місце проживання"])
    if st.button("Надіслати запит"):
        st.success(f"Запит надіслано! Очікуйте відповіді.")

elif choice == "🏥 Запис до лікаря":
    st.header("Запис на прийом")
    doctor = st.selectbox("Лікар", ["Терапевт", "Педіатр", "Стоматолог"])
    date = st.date_input("Дата")
    if st.button("Записатися"):
        st.success("Ви записані!")

elif choice == "🛠️ Комунальна варта":
    st.header("Повідомити про проблему")
    prob = st.text_area("Опишіть проблему")
    if st.button("Відправити"):
        st.warning("Повідомлення прийнято.")
      
