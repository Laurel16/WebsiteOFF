import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
import PIL
from PIL import Image

#%%writefile score.py
#import streamlit as st
import easyocr
#from googletrans import Translator
#from gtts import gTTS
#from PIL import Image
#import numpy as np


st.write('hello 👋')






# st.title("Upload + Classification Example")

# uploaded_file = st.file_uploader("Choose an image...", type="jpg")
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='Uploaded Image.', use_column_width=True)
#     st.write("")
#     st.write("Classifying...")
    #label = predict(uploaded_file)
    #st.write('%s (%.2f%%)' % (label[1], label[2]*100))

    # Using PIL
    #image = Image.open(uploaded_file)
    #st.image(image, caption='Uploaded Image.')

# CSS = """
# h1 {
#     color: red;
# }

# .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf,#2e7bcf); color: white; }

# }
# """
# st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#translator = Translator()

def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text


st.sidebar.title('Language Selection Menu')
st.sidebar.subheader('Select...')
src = st.sidebar.selectbox("From Language",['French', 'English'])


# st.sidebar.subheader('Select...')
# destination = st.sidebar.selectbox("To Language",['English', 'French'])

# st.sidebar.subheader("Enter Text")
# area = st.sidebar.text_area("Auto Detection Enabled","")

# helper = {'English':'en', 'French': 'fr'}
# dst = helper[destination]
# source = helper[src]

# if st.sidebar.button("Translate!"):
#     if len(area)!=0:
#         sour = translator.detect(area).lang
#         answer = translator.translate(area, src=f'{sour}', dest=f'{dst}').text
#         #st.sidebar.text('Answer')
#         st.sidebar.text_area("Answer",answer)
#         st.balloons()
#     else:
#         st.sidebar.subheader('Enter Text!')


st.set_option('deprecation.showfileUploaderEncoding',False)
st.title('Open Food Facts categories predictions')
st.subheader('Ingredients photo recognition')
st.text('Select source Language from the Sidebar and upload your photo.')

image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg','JPG'])


if st.button("Convert"):

    if image_file is not None:
        img = Image.open(image_file)
        img = np.array(img)

        st.subheader('Image you Uploaded...')
        st.image(image_file,width=450)

        if src=='English':
            with st.spinner('Extracting Text from given Image'):
                eng_reader = easyocr.Reader(['en'])
                detected_text = eng_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)

        elif src=='French':
            with st.spinner('Extracting Text from given Image'):
                swahili_reader = easyocr.Reader(['fr'])
                detected_text = swahili_reader.readtext(img)
            st.subheader('Extracted text is ...')
            text = display_text(detected_text)
            st.write(text)



        # st.write('')
        # ta_tts = gTTS(text,lang=f'{source}')
        # ta_tts.save('trans.mp3')
        # st.audio('trans.mp3',format='audio/mp3')


        # with st.spinner('Translating Text...'):
        #     result = translator.translate(text, src=f'{source}', dest=f'{dst}').text
        # st.subheader("Translated Text is ...")
        # st.write(result)

        # st.write('')
        # st.header('Generated Audio')

        # with st.spinner('Generating Audio ...'):
        #     ta_tts2 = gTTS(result,lang=f'{dst}')
        #     ta_tts2.save('trans2.mp3')
        # st.audio('trans2.mp3',format='audio/mp3')
        # st.balloons()


    else:
        st.subheader('Image not found! Please Upload an Image.')

st.subheader('Categorie prediction')
st.text('''Your product's categorie should be...''')

#!nohup streamlit run score.py &



#from pyngrok import ngrok

#url = ngrok.connect(port=8501)
#url
