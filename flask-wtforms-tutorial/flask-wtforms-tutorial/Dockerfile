FROM python:3.9

EXPOSE 5002

WORKDIR /flask_wtforms_tutorial

COPY requirements.txt /flask_wtforms_tutorial
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask_wtforms_tutorial

CMD python routes.py