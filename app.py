import streamlit as st
import json

st.set_page_config(page_title="رباعیات خیام", layout="centered")

# خواندن فایل اشعار
with open("poems.json", "r", encoding="utf-8") as f:
    poems = json.load(f)

st.title("رباعیات خیام")

# گرفتن لیست دسته‌ها
categories = sorted(list(set([p["category"] for p in poems])))

selected_category = st.selectbox("یک دسته‌بندی انتخاب کن:", categories)

# فیلتر اشعار بر اساس دسته
filtered_poems = [p for p in poems if p["category"] == selected_category]

# مدیریت شعر فعلی
if "index" not in st.session_state:
    st.session_state.index = 0

current_poem = filtered_poems[st.session_state.index]

# نمایش شعر
st.subheader("رباعی")
st.text(current_poem["text"])

# دکمه شعر بعدی
if st.button("شعر بعدی"):
    st.session_state.index += 1
    if st.session_state.index >= len(filtered_poems):
        st.session_state.index = 0
    st.rerun()

# دکمه تفسیر
if st.button("تفسیر رباعی"):

    st.info(current_poem["interpretation"])
