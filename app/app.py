
import streamlit as st
import numpy as np
import joblib
import pandas as pd
import datetime
import requests
import time
import PIL
from PIL import Image
import pytesseract as pt
custom_config = r'--oem 3 --psm 4'


pt.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

from helpers import cat_emoij, list_categories

CSS = """
 h1 {
    color: #00917c;
 }

 h2 {
 color: #b34180
 }

"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#control + cmd + espace pour les smileys

#st.write('Hello 👋')
st.image('app/image/off.png', width=300)
x = 'sweets'
emoij = '😋'




st.set_option('deprecation.showfileUploaderEncoding', False)
st.title('Devine ma catégorie')
#st.header('Ingredients photo recognition')
#st.subheader('Upload your photo')

image_file = st.file_uploader("", type=['jpg','png','jpeg','JPG'])


#if st.button("Convert"):
#start = time.time()
if image_file is not None:
    img = Image.open(image_file)
    img = np.array(img)
    st.subheader('''Voici votre étiquette''')
    st.image(image_file,width=450)
    st.subheader('''J'examine le texte...''')
    #st.balloons()


    #with st.spinner('''J'examine votre photo...'''):
    text = pt.image_to_string(img, config=custom_config, lang="fra")
    st.subheader('Voici le texte de votre étiquette ...')
    #end = time.time()
    #st.write(end - start)


            #text = display_text(text)
    st.write(text)

    url = 'https://apioff-kdwmcasooa-ew.a.run.app/predict_probabilities?'
    params={'text': text}
    result = requests.get(url, params=params)
            #st.write(result.headers)
            #predict = result[0]
    json = result.json()
    x = json['result']
    emoij = cat_emoij(x, list_categories)
    st.write(f"<h1 style='color: #00917c; font-size: 25px;'>{x} {emoij}</h1>", unsafe_allow_html=True)
    st.balloons()

else:
        st.subheader('''J'attends la photo de vos ingrédients''')

#st.write(f'<style>{CSS}</style>', unsafe_allow_html=True, 'breakfast cereals', '', emoij)


# def display_text(bounds):
#     text = []
#     for x in bounds:
#         t = x[1]
#         text.append(t)
#     text = ' '.join(text)
#     return text

