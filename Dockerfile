FROM python:3.8-buster

COPY app/ app


RUN pip install --upgrade pip
RUN pip install -r app/requirements.txt

RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y tesseract-ocr-fra \
    && apt-get clean \
    && apt-get autoremove

RUN mkdir -p ~/.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml'


EXPOSE $PORT


#RUN tesseract --version
#RUN find -iname *tesseract*

CMD streamlit run app/app.py
