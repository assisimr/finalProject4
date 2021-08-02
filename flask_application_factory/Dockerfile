FROM python:3.9

EXPOSE 5005

WORKDIR /flask_application_factory

COPY requirements.txt /flask_application_factory
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask_application_factory

CMD python app.py