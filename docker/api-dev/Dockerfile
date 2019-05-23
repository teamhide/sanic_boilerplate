FROM python:3.7.2
MAINTAINER hide <sharehead@gmail.com>

COPY . /home
WORKDIR /home
RUN pip install pipenv
RUN pipenv install --system
CMD ["python3", "/home/main.py"]