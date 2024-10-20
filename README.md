

### 🎨 Artistic Style Transfer Web App

This web application allows users to transform their photos into stunning artwork by applying styles from other images, such as famous paintings. The app uses a neural style transfer model powered by TensorFlow and TensorFlow Hub, providing an intuitive interface for uploading images and seeing the results instantly.

### Features
Image Upload: Upload a content image (the image you want to transform) and a style image (the source of the artistic style) easily.


Style Transfer: Apply the artistic style from the style image to the content image with a single click.


Real-Time Display: See the transformed image in real-time once the style transfer is complete.


Simple and Attractive UI: The app has an easy-to-navigate interface, with a clean layout and colorful emojis for better engagement.

## Tech Stack
Frontend: Streamlit for building the web interface and user interaction.


Backend: TensorFlow and TensorFlow Hub for the neural style transfer model.


Image Processing: PIL (Python Imaging Library) for handling image uploads and preprocessing.


# How It Works
Load the Model: The application loads a pre-trained style transfer model from TensorFlow Hub.


Upload Images: Users can upload two images:


Content Image: The image to which the style will be applied.


Style Image: The image that serves as the source of the artistic style.


Apply Style Transfer: Once both images are uploaded, the user clicks the "✨ Apply Style Transfer" button to transform the content image using the selected style.


View Result: The transformed image is displayed for the user to view.

![Alt text](https://github.com/Zurinlakdawala91/Style-tranfer/blob/main/Screenshot%202024-10-20%20192616.png)





![Alt text](https://github.com/Zurinlakdawala91/Style-tranfer/blob/main/Screenshot%202024-10-20%20192721.png)
