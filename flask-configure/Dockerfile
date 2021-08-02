FROM python:3.9

EXPOSE 5004

WORKDIR /configure_flask

COPY requirements.txt /configure_flask
RUN pip install  -r requirements.txt --upgrade pip

ENV SECRET_KEY=GDtfDCFYjD
ENV SESSION_COOKIE_NAME=cookies_are_love
ENV PROD_DATABASE_URI=my_prod_db
ENV DEV_DATABASE_URI=my_dev_db

COPY . /configure_flask

CMD python app.py