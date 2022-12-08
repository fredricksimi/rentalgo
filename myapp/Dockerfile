FROM python:3.10-alpine
WORKDIR /usr/src/app/
COPY ./app ./
RUN pip install -r requirements.txt
RUN python manage.py migrate
EXPOSE 8000


