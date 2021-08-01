FROM python:3.9

EXPOSE 5003

WORKDIR /flask-routing

COPY requirements.txt /flask-routing
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-routing

CMD python app.py