import logging

from confluent_kafka import Producer

from kafka_configuration import KafkaConfig

class KafkaProducerClient:
    def __init__(self):
        self.kafka_service_internal_host = KafkaConfig().kafka_service_host
        self.kafka_service_internal_port = KafkaConfig().kafka_service_port
        self.kafka_service_username = KafkaConfig().kafka_service_username
        self.kafka_service_password = KafkaConfig().kafka_service_password

    def get_producer(self):
        producer_configuration = {
            'bootstrap.servers': self.kafka_service_internal_host,
            'security.protocol': 'SASL_SSL',
            'sasl.mechanisms': 'PLAIN',
            'sasl.username': self.kafka_service_username,
            'sasl.password': self.kafka_service_password
        }

        return Producer(
                producer_configuration
            )
