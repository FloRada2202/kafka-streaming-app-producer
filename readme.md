# Kafka Producer Documentation
# Kafka Streaming Application

## Initial setup
### 1. Create docker network using following command if network is not previously created
'''docker network create kafka-streaming-app-network '''
### 2. Start single node apache kafka and zookeper using following command if apache kafka is not running
'''docker-compose -f docker-compose-apache-kafka.yml up --build'''
### 3. Start main service container using follogin command
'''docker-compose up --build'''


### Since this is demo application, environment variables will be included here:
```
KAFKA_SERVICE_INTERNAL_HOST='kafka-service'  kafka host
KAFKA_SERVICE_INTERNAL_PORT='9092'  kafka port
KAFKA_SERVICE_OUTPUT_TOPIC='kafka-produce-users-topic' kafka topic to produce data
```