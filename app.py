import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

st.set_page_config(page_title="LeafCure 🌱", layout="centered")
st.title("LeafCure 🌱 - Leaf Disease Detection App")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf Image', use_column_width=True)

    # Dummy prediction simulation
    st.subheader("Prediction Result:")
    st.write("Tomato Leaf Curl Virus (Confidence: 97.5%)")

    st.subheader("Cure and Prevention Tips:")
    st.write("• Remove infected plants
• Use virus-free seeds
• Apply neem oil")

st.markdown("---")
st.subheader("Feedback")
name = st.text_input("Your Name")
comment = st.text_area("Your Feedback")
if st.button("Submit"):
    st.success("Thank you for your feedback!")
