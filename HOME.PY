import streamlit as st
from PIL import Image
from matplotlib import image
import os

#Title 
st.header(":red[Laptop Price Prediction Data App]")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resourses")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)
