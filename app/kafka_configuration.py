import os
import logging

logging.basicConfig(level=logging.INFO)


class KafkaConfig(object):
    @property 
    def kafka_service_host(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_HOST')
    
    @property 
    def kafka_service_port(self):
        return os.getenv('KAFKA_SERVICE_INTERNAL_PORT')
    
    @property 
    def kafka_service_output_topic(self):
        return os.getenv('KAFKA_SERVICE_OUTPUT_TOPIC')

    @property
    def kafka_service_username(self):
        return os.getenv('KAFKA_SERVICE_USERNAME')

    @property
    def kafka_service_password(self):
        return os.getenv('KAFKA_SERVICE_PASSWORD')