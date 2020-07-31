FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x ./docker/*


CMD ./docker/run.sh