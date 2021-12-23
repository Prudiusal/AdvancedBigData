import socket 
from sender import send_tcp_values_with_freq, freq, send_values_db
from generator import gen1
import os
import time

HOST = '0.0.0.0'
PORT = 20207
gen_db  = os.getenv("GENERATE_DB")
history_number = int(os.getenv("HISTORY_NUMBER_DB"))
time = 1 / int(os.getenv("HIGH_FREQ"))

print('Sensor has started')
print(f'GENERATE_DB = {gen_db}')
print(f'HISTORY_NUMBER_DB = {history_number}')
print(f'HIGH_FREQ = {os.getenv("HIGH_FREQ")}')

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((HOST, PORT))
# become a server socket
serversocket.listen(1)

(clientsocket, address) = serversocket.accept()
# now do something with the clientsocket
print(f'Client with {address} has connected') 

sensor_values_generator = gen1()


if gen_db =="true":
	print('Generation of db has started') 
#	send_values_db(clientsocket, sensor_values_generator, history_number)
	freq(clientsocket, sensor_values_generator, history_number, time, )
	time.sleep(round(1.3*history_number*time))
	
		
 
print("Sensor is starting")
send_tcp_values_with_freq(clientsocket, sensor_values_generator)
 
