FROM python:3.7-slim-stretch
MAINTAINER You "ashfaq@pdx.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
CMD gunicorn --bind :$PORT --workers 1 --threads 8 app:app