import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("xray_disease_detection_model.h5")

class_names = ["NORMAL", "PNEUMONIA", "COVID"]

st.title("🩺 Chest X-ray Disease Detection")
st.write("Upload a chest X-ray image to detect disease")

uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded X-ray", use_column_width=True)

    img = image.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    result = class_names[np.argmax(prediction)]

    st.success(f"🧾 Prediction: **{result}**")
