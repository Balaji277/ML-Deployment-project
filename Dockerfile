FROM python:3.11.3-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN python3 main.py

CMD ["python3", "app.py"]
