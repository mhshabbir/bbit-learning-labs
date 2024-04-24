import pika
import os
from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        self.setupRMQConnection()
    
    def setupRMQConnection(self):
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters = self.con_params)

        self.channel = self.connection.channel()

        self.exchange = self.channel.exchange_declare(exchange="buy_stock")

    def publishOrder(self, message: str) -> None:
        self.channel.basic_publish(
            exchange= self.exchange_name,
            routing_key= self.routing_key,
            body=" This is message from Muhammad",
        )

        self.channel.close()
        self.connection.close()