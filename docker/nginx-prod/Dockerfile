FROM nginx:1.15.6
MAINTAINER hide <sharehead@gmail.com>

COPY . ./home
WORKDIR home
RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/nginx-prod/nginx-prod.conf /etc/nginx/conf.d/default.conf