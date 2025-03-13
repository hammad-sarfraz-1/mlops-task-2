import streamlit as st
import requests

BACKEND_URL = "http://backend:8000"

st.title("Login & Signup")

menu = st.sidebar.selectbox("Menu", ["Login", "Signup"])

if menu == "Signup":
    st.subheader("Create an Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        response = requests.post(f"{BACKEND_URL}/signup", json={"email": email, "password": password})
        st.success(response.json().get("message"))

elif menu == "Login":
    st.subheader("Login to Your Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(f"{BACKEND_URL}/login", json={"email": email, "password": password})
        if response.status_code == 200:
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
