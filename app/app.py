
import streamlit as st
import numpy as np
import joblib
import pandas as pd
import datetime
import requests
import time
import PIL
from PIL import Image

#%%writefile score.py
#import streamlit as st
#import easyocr
#from googletrans import Translator
#from gtts import gTTS
#from PIL import Image
#import numpy as np
#import cv2
import pytesseract as pt
custom_config = r'--oem 3 --psm 4'
#mport tesserocr
#api = tesserocr.PyTessBaseAPI()


pt.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
#image = Image.open(path)
#t = pytesseract.image_to_string(image)
#line_bot_api.reply_message(event.reply_token,TextSendMessage(text=t))


#control + cmd + espace pour les smileys

st.write('Hello 👋')
#image = Image.open('test.jpeg')
#st.image(image, caption='Le Wagon', use_column_width=True)
st.image('app/image/off.png', width=300)
#if st.button('Predict'):
    #st.balloons()


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

CSS = """
 h1 {
    color: #822659;
 }

 h2 {
 color: #b34180
 }



"""
# .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf,#2e7bcf); color: white; }


st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


#translator = Translator()

#### récupérer à partir d'ici

def display_text(bounds):
    text = []
    for x in bounds:
        t = x[1]
        text.append(t)
    text = ' '.join(text)
    return text


#st.sidebar.title('Language Selection Menu')
#st.sidebar.subheader('Select...')
#src = st.sidebar.selectbox("From Language",['French', 'English'])


#////// comnenté

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


#// fin du comment

st.set_option('deprecation.showfileUploaderEncoding',False)
st.title('Open Food Facts categories predictions')
st.header('Ingredients photo recognition')
#st.subheader('Upload your photo')

image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg','JPG'])


if st.button("Convert"):
    start = time.time()
    if image_file is not None:
        img = Image.open(image_file)
        img = np.array(img)

        st.subheader('Image you uploaded...')
        st.image(image_file,width=450)
        #st.balloons()

        # if src=='English':
        #     with st.spinner('Extracting Text from given Image'):
        #         eng_reader = easyocr.Reader(['en'])
        #         detected_text = eng_reader.readtext(img)
        #     st.subheader('Extracted text is ...')
        #     text = display_text(detected_text)
        #     st.write(text)

        #if src=='French':
        with st.spinner('Extracting Text from given Image'):
                #swahili_reader = easyocr.Reader(['fra'])
                #detected_text = swahili_reader.readtext(img)

                #api.SetImage(img)
                #text = api.GetUTF8Text()
            text = pt.image_to_string(img, config=custom_config, lang="fra")
            st.subheader('Extracted text is ...')
            end = time.time()
            st.write(end - start)

            #text = display_text(text)
            st.write(text)
            st.subheader('Categorie prediction')
            st.text('''Your product's categorie should be...''')


            url = 'https://apioff-kdwmcasooa-ew.a.run.app/predict_probabilities?'
            params={'text': text}
            result = requests.get(url, params=params)
            #st.write(result.headers)
            #predict = result[0]
            json = result.json()
            st.write(json['result'])


            # model = joblib.load('NB_pipeline_pnns_2.joblib')
            # prediction = model.predict([text])
            # st.write(prediction[0])


#// tout ça commenté

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

#// fin du comment

    else:
        st.subheader('Image not found! Please Upload an Image.')




#// tout le reste commenté

#!nohup streamlit run score.py &



#from pyngrok import ngrok

#url = ngrok.connect(port=8501)
#url
