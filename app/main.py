import logging
import ujson
import gzip
import time

from kafka_producer import KafkaProducerClient
from kafka_configuration import KafkaConfig

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    try:
        kafka_producer_instance = KafkaProducerClient().get_producer()

        with gzip.open('stream.jsonl.gz', 'rt') as data:
            for record in data:
                try:
                    kafka_producer_instance.produce(
                        KafkaConfig().kafka_service_output_topic,
                        ujson.dumps(record)
                    )
                    kafka_producer_instance.poll(0)
                except BufferError as e:
                    logging.info("Queue is full. Waiting for the free space!")
                    kafka_producer_instance.poll(20)
                    kafka_producer_instance.produce(
                        KafkaConfig().kafka_service_output_topic,
                        ujson.dumps(record)
                    )
        kafka_producer_instance.flush()
    except Exception as e:
        logging.info(str(e))
