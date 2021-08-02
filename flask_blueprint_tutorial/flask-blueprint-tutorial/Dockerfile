FROM python:3.9

EXPOSE 5006

WORKDIR /flask-blueprint-tutorial

COPY requirements.txt /flask-blueprint-tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask-blueprint-tutorial

CMD . /app.py