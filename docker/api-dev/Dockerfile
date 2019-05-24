FROM python:3.7.2
MAINTAINER hide <sharehead@gmail.com>

COPY Pipfile ./home
COPY Pipfile.lock ./home
WORKDIR /home
RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.6.1
ENV IS_DOCKER true
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN pip install pipenv
RUN pipenv install --system
CMD ./docker/api-dev/run.sh