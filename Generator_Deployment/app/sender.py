import threading
from random import random
#from time import sleep


def send_tcp_values_with_freq(s, generator):
    threading.Timer(1/1000, send_tcp_values_with_freq, args=(s, generator)).start()
    #       there shold be sensor Generator By Artem 
    num = next(generator)
    message = num.to_bytes(4, byteorder='big', signed=True)
    s.send(message)
    
    
def send_values_db (s, generator, num_vals):
	for i in range(int(num_vals)):
		num = next(generator)
		message = num.to_bytes(4, byteorder='big', signed=True)
		s.send(message)
#		sleep(0.00003)
		
	print('db_done')
	
	
#def send_tcp_values_with_high_freq(s, generator, limit=7200000, n=1, time=1/50000):
#	n+=1
#	if not n>limit:
#	    threading.Timer(1/50000, send_tcp_values_with_freq, args=(s, generator, limit, n, )).start()
    #       there shold be sensor Generator By Artem 
 #   	num = next(generator)
  #  	message = num.to_bytes(4, byteorder='big', signed=True)
   # 	s.send(message)


def freq(s, generator, limit=7200000, time=1/50000, n=1, ):
    n+=1 
    if not n>limit:
        threading.Timer(time, freq, args=( s, generator, limit, time, n, )).start()
        num = next(generator)
        message = num.to_bytes(4, byteorder='big', signed=True)
        s.send(message)
    else:
        print('db_done')
