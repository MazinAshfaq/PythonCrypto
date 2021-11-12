FROM python:3.7-slim 
MAINTAINER You "ashfaq@pdx.edu"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
