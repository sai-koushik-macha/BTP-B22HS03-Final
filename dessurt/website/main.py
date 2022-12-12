import torch
import numpy as np
import pandas as pd
import streamlit as st
from run import main
from PIL import Image
import gdown
from os import path

st.set_page_config(
    page_title="DocVQA",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_output_mask = False #@param {type:"boolean"}
checkpoint = 'dessurt_docvqa_best.pth'

@st.cache
def download_weights(url):
    if path.exists(checkpoint) == False:
        gdown.download(url, checkpoint, quiet=False)


url = "https://drive.google.com/uc?export=download&id=1Lj6xMvQcF9dSCxVQS2nia4SiEoPXbtCv"
download_weights(url)





st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png"])

st.markdown("## Ask questions")
st.write("Query: ")
query = st.text_input('Write the query here')
#   st.markdown(f'{query}', unsafe_allow_html=True)
submit = st.button('Predicted Answer')

if submit:
    st.markdown(f"{main(checkpoint,None,image_file,None,False,default_task_token='natural_q~',dont_output_mask=not show_output_mask,question=query)}",unsafe_allow_html=True)

    
      

