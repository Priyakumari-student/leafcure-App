import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd
import time
import io

# 1. Page Setup
st.set_page_config(page_title="LeafCure 🌱", layout="centered")
st.title("🌿 LeafCure - Leaf Disease Detection App")

# 2. Theme Toggle
theme = st.radio("Choose Theme", ["🌞 Light", "🌙 Dark"], horizontal=True)
if theme == "🌙 Dark":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: white; }
        .stApp { background-color: #0e1117; }
        </style>
    """, unsafe_allow_html=True)

# 3. Upload or Camera Input
st.subheader("📤 Upload or Capture a Leaf Image")
upload_option = st.radio("Choose Input Method", ["Upload", "Camera"])
uploaded_file = None
if upload_option == "Upload":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.camera_input("Take a picture")

# 4. Dummy Prediction & Display
if uploaded_file:
    with st.spinner("🔍 Analyzing image..."):
        time.sleep(1)
        image = Image.open(uploaded_file)
        st.image(image, caption='📷 Uploaded Leaf Image', use_column_width=True)

        # Dummy prediction values
        predicted_class = "Tomato Leaf Curl Virus"
        confidence = 97.5

        st.subheader("🧠 Prediction Result")
        st.write(f"*Disease Detected:* {predicted_class}")
        st.progress(int(confidence))

        st.subheader("💡 Cure & Prevention Tips")
        with st.expander("Click to view treatment guidance"):
            st.markdown("""
            *Tomato Leaf Curl Virus (TLCV)*

            *🦠 Cause:* Virus transmitted by whiteflies  
            *⚠️ Impact:* Curled leaves, stunted growth

            ### ✅ Prevention
            - Remove infected plants immediately
            - Use certified virus-free seeds
            - Apply neem oil or insecticidal soap
            - Use yellow sticky traps for whiteflies
            """)

# 5. Feedback Section
st.markdown("---")
st.subheader("📝 Feedback")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Your Name")
with col2:
    email = st.text_input("Email (optional)")

comment = st.text_area("Your Feedback")
submit = st.button("Submit")

if submit:
    if name and comment:
        feedback_entry = pd.DataFrame([[name, email, comment]], columns=["Name", "Email", "Comment"])
        try:
            existing_data = pd.read_csv("feedback.csv")
            feedback_entry = pd.concat([existing_data, feedback_entry], ignore_index=True)
        except FileNotFoundError:
            pass
        feedback_entry.to_csv("feedback.csv", index=False)
        st.success("✅ Thanks for your feedback!")
    else:
        st.warning("⚠️ Please fill in your name and feedback.")

# 6. Additional Features
st.sidebar.header("Additional Features")
st.sidebar.markdown("""
- *🌍 Multi-language Support:* Coming soon!
""")
# 7. Contact Information
st.sidebar.header("Contact Us")
st.sidebar.markdown("""
For inquiries, reach us at:
- *Email:* priyakumari020630@gmail.com
""")
# 8. Footer
st.markdown("---")
st.caption("🌱 Built with ❤️ using Streamlit | © 2025 LeafCure")
