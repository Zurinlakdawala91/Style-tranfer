import functools
import altair as alt
import numpy as np
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

def main():
    # Load the style transfer model from TensorFlow Hub
    hub_handle = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    hub_module = hub.load(hub_handle)

    print("TF Version: ", tf.__version__)
    print("TF-Hub version: ", hub.__version__)
    print("Eager mode enabled: ", tf.executing_eagerly())
    print("GPU available: ", tf.config.list_physical_devices('GPU'))

    # Function to crop the image to a square
    def crop_center(image):
        """Returns a cropped square image."""
        shape = image.shape
        new_shape = min(shape[0], shape[1])
        offset_y = max(shape[0] - shape[1], 0) // 2
        offset_x = max(shape[1] - shape[0], 0) // 2
        image = tf.image.crop_to_bounding_box(
            image, offset_y, offset_x, new_shape, new_shape)
        return image

    # Function to load and preprocess the image
    def load_image(uploaded_file, image_size=(256, 256), col=st):
        img = Image.open(uploaded_file)
        img = img.convert('RGB')  # Ensure the image is in RGB format
        img = tf.convert_to_tensor(np.array(img))
        img = crop_center(img)
        img = tf.image.resize(img, image_size)
        img = tf.cast(img, tf.float32) / 255.0
        img = tf.expand_dims(img, 0)  # Add a batch dimension
        col.image(np.array(img[0]))
        return img

    # Function to display images
    def show_n(images, col=st):
        for img in images:
            col.image(np.array(img[0]))

    # Basic setup and app layout
    st.set_page_config(page_title="Artistic Style Transfer", layout="wide")

    # Add custom background color
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set a title for the app
    st.title("🎨 Artistic Style Transfer Web App")
    st.markdown("Turn your photos into art by applying styles from famous paintings or any other images!")

    # Set up columns for user interface
    col1, col2 = st.columns(2)
    col1.markdown('### 🎨 Add image on which style is required')
    uploaded_file = col1.file_uploader("Choose content image")
    content_image = None

    if uploaded_file is not None:
        content_image = load_image(uploaded_file, (384, 384), col=col1)

    col2.markdown('### 🖼️ Add image from which style will be extracted')
    uploaded_file_style = col2.file_uploader("Choose style image")
    style_image = None

    if uploaded_file_style is not None:
        style_image = load_image(uploaded_file_style, (384, 384), col=col2)

    # Apply style transfer if both images are uploaded and button is clicked
    if content_image is not None and style_image is not None:
        if st.button("✨ Apply Style Transfer"):
            stylized_image = hub_module(content_image, style_image)[0]
            col3, col4, col5 = st.columns(3)
            col4.markdown('### 🖌️ Style applied on the image')
            show_n([stylized_image], col=col4)

if __name__ == "__main__":
    main()
