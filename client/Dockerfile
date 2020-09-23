FROM python:3.7-buster

WORKDIR /usr/app

RUN python -m pip install grpcio grpcio-tools

COPY Makefile .
COPY remotetaskcall/ remotetaskcall/

RUN rm -r remotetaskcall/generated && make protocol


ENV CLIENT_COMMAND \
    SERVICE_HOST=localhost \
    SERVICE_PORT=9090

ENTRYPOINT [ "make", "start" ]
