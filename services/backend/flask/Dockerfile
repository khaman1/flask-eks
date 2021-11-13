FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

WORKDIR /app
COPY app/ .

RUN pip3 install -r requirements.txt

ARG CURRENT_ENV=dev
ENV CURRENT_ENV $CURRENT_ENV

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]