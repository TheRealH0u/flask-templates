FROM alpine:3.18

RUN apk add --update --no-cache supervisor openssh python3 py3-pip zlib jpeg-dev zlib-dev gcc python3-dev vim nano
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

RUN adduser -D -u 1000 -g 1000 -s /bin/sh www

COPY config/supervisord.conf /etc/supervisord.conf
COPY --chown=www:www app/ /app

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN echo "FLAG{$(tr -dc A-Za-z0-9 </dev/urandom | head -c 20)}" > /flag.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
