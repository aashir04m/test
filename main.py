import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np

from util import classify, set_background


set_background('./bgs/Untitled design.png')

# set title
st.title('Skin Cancer Detection')

# set header
st.header('Please upload a sample image')

# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/Skin_Cancer.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# class_names = []

# with open('./model/labels1.txt', 'r') as f:
#     for line in f.readlines():
#         label = line.strip()
#         class_names.append(label)
#         f.close()

print(class_names)


# display image
if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name = classify(image, model)

    # write classification
    st.write("## {}".format(class_name))
    # st.write("### score: {}%".format(int(conf_score * 1000) / 10))
