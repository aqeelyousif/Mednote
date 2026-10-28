import streamlit as st

st.title("🩺 منصتي الطبية (Mednote)")
st.write("أهلاً بك! هذا التطبيق تم بناؤه من الصفر.")

name = st.text_input("ما هو اسمك؟")
if name:
    st.success(f"أهلاً بك يا {name}! التطبيق يعمل بنجاح.")
    
