FROM node:14.6.0

COPY . /app
WORKDIR /app
RUN npm install -g @angular/cli
RUN npm install
RUN npm build

RUN chmod +x ./docker/run.sh


CMD ./docker/run.sh