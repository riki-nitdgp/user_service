FROM python:3.9

WORKDIR /opt/user_service

COPY ./requirements.txt /opt/user_service/requirements.txt

COPY ./server.py /opt/user_service/server.py

COPY ./config.json /opt/user_service/config.json

RUN pip3 install -r /opt/user_service/requirements.txt

COPY ./app /opt/user_service/app

EXPOSE 8005

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8005"]