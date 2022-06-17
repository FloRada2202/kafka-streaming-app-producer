FROM python:3

WORKDIR /

COPY service-requirements.txt ./
RUN git clone https://github.com/edenhill/librdkafka.git
WORKDIR /librdkafka
RUN /librdkafka/configure --prefix /usr &&\ 
    make &&\
    make install

WORKDIR /
RUN curl -LJO https://tda-public.s3.eu-central-1.amazonaws.com/hire-challenge/stream.jsonl.gz &&\
    pip install --no-cache-dir -r service-requirements.txt

ENV KAFKA_SERVICE_INTERNAL_HOST ${KAFKA_SERVICE_INTERNAL_HOST}
ENV KAFKA_SERVICE_INTERNAL_PORT ${KAFKA_SERVICE_INTERNAL_PORT}
ENV KAFKA_SERVICE_OUTPUT_TOPIC ${KAFKA_TOPIC_SUBSCRIBE}
ENV KAFKA_SERVICE_PASSWORD ${KAFKA_SERVICE_PASSWORD}
ENV KAFKA_SERVICE_USERNAME ${KAFKA_SERVICE_USERNAME}

ADD app /app
