# app.py
import streamlit as st

def main():
    st.title("Hello, Streamlit!")
    st.write("Ini adalah aplikasi Streamlit pertama saya.")
    
    # Contoh input dan output
    name = st.text_input("Masukkan nama Anda:")
    if st.button("Submit"):
        st.write(f"Hello, {name}!")

if __name__ == "__main__":
    main()