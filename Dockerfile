FROM python:3.7
COPY . /ML_Drug_Presc_Web_App
WORKDIR /ML_Drug_Presc_Web_App
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:ML_Drug_Presc_Web_App