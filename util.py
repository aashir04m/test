import base64

import streamlit as st
from PIL import ImageOps, Image
import numpy as np
# import cv2

def set_background(image_file):
    """
    This function sets the background of a Streamlit app to an image specified by the given image file.

    Parameters:
        image_file (str): The path to the image file to be used as the background.

    Returns:
        None
    """
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


def classify(image, model):
    """
    This function takes an image, a model, and a list of class names and returns the predicted class and confidence
    score of the image.

    Parameters:
        image (PIL.Image.Image): An image to be classified.
        model (tensorflow.keras.Model): A trained machine learning model for image classification.
        class_names (list): A list of class names corresponding to the classes that the model can predict.

    Returns:
        A tuple of the predicted class name and the confidence score for that prediction.
    """
    # convert image to (224, 224)
    image = ImageOps.fit(image, (28, 28), Image.Resampling.LANCZOS)

    # # convert image to numpy array
    image_array = np.asarray(image)

    # # normalize image
    normalized_image_array = (image_array.astype(np.float32) / 255.0) - 1

    # # set model input
    data = np.ndarray(shape=(1, 28, 28, 3), dtype=np.float32)
    # print("data", data)
    data[0] = normalized_image_array

    classes = {4: ('nv', ' melanocytic nevi'),
           6: ('mel', 'melanoma'),
           2 :('bkl', 'benign keratosis-like lesions'),
           1:('bcc' , ' basal cell carcinoma'),
           5: ('vasc', ' pyogenic granulomas and hemorrhage'),
           0: ('akiec', 'Actinic keratoses and intraepithelial carcinomae'),
           3: ('df', 'dermatofibroma')}
    
    # # make prediction
    # prediction = model.predict(data)
    # print("prediction", prediction)
    # # index = np.argmax(prediction)
    # max_prob = max(prediction[0])
    # print("max_prob", max_prob)
    # class_ind = list(prediction[0]).index(max_prob)
    # print("class_ind", class_ind)
    # class_name = classes[class_ind]
    # print("class_name", class_name)
    # # index = 0 if prediction[0][0] > 0.95 else 1
    # # class_name = class_names[index]
    # # confidence_score = prediction[0][class_ind]

    # img = cv2.imread(image)
    # cv2.imwrite(img)
    # cv2_imshow(img)
    # img = cv2.resize(img, (28, 28))
    result = model.predict(data)
    print(result)
    max_prob = max(result[0])
    print("max_prob", max_prob)
    class_ind = list(result[0]).index(max_prob)
    print("class_ind", class_ind)
    class_name = classes[0]
    print(class_name)

    return class_name
