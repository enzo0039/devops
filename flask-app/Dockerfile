FROM python:3.7

COPY . /flask-ap
WORKDIR /flask-ap
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENV FLASK_flask-ap /flask-ap/server.py

CMD gunicorn --bind 0.0.0.0:5000 wsgi:flaskapp

EXPOSE 5000
