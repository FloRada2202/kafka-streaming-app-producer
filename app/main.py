import logging
import random
import json
import time
import os

from kafka import KafkaProducer

logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    try:
        logging.info(os.getenv('KAFKA_SERVICE_INTERNAL_HOST'))
        kafka_producer = KafkaProducer(
                bootstrap_servers=f"{os.getenv('KAFKA_SERVICE_INTERNAL_HOST')}:{os.getenv('KAFKA_SERVICE_INTERNAL_PORT')}",
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        for i in range(1, 10):
            time.sleep(3)
            logging.info('producing message to topic')
            message = {
                "uid": f"{i}",
                "ts": time.time()
            }
            kafka_producer.send(os.getenv('KAFKA_SERVICE_OUTPUT_TOPIC'), value=message)
            kafka_producer.flush(timeout=5)
        kafka_producer.close()
    except Exception as e:
        logging.info(str(e))