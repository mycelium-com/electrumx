FROM python:3.7-alpine

ADD . /electrumx

RUN apk add --no-cache build-base openssl && \
    apk add --no-cache --repository http://nl.alpinelinux.org/alpine/latest-stable/community leveldb-dev && \
    pip install uvloop

RUN cd /electrumx && \
    python setup.py install

RUN apk del build-base && \
    rm -rf /tmp/*

ENV HOME /data
ENV DB_DIRECTORY /data
ENV HOST ""
ENV ALLOW_ROOT 1
ENV SERVICES tcp://:50001,rpc://127.0.0.1

WORKDIR /data
VOLUME /data
EXPOSE 50001

CMD ["/electrumx/electrumx_server"]
