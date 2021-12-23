from kafka import KafkaProducer, KafkaAdminClient

import os
import socket
from random import random
import time

print('Producer has started')
broker_host = os.getenv("BROKER_HOST")
topic = os.getenv("HOSTNAME")
bootstrap_server = broker_host + ":9092"

print(bootstrap_server)
print(f"topic is {topic}")

producer = KafkaProducer(bootstrap_servers=bootstrap_server)

#hello = 'Hello form prod!'
#producer.send('test', hello.encode('utf-8'))
time.sleep(3) 

host = '0.0.0.0'
port = 20207
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the  server on port
s.connect((host, port))
data = s.recv(16)

while True:
    message = s.recv(4)
    value = str(int.from_bytes(message, byteorder='big', signed=True))
    producer.send(topic ,value.encode('utf-8')) 

