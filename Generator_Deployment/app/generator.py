from random import choice, random, uniform, gauss
from math import sin, pow

def gauss_arg():
 low_mu, high_mu =  uniform(0.01, 0.1),  uniform(0.1, 0.3)
 low_sigma, high_sigma = uniform(0.001, 0.02),  uniform(0.08, 0.12)
 return [low_mu, high_mu, low_sigma, high_sigma]

def gen1():
   type = choice(['sin', 'gauss', 'cubic','square'])
#     print(type)
   step = int( random() * choice ([ 100, 10000, 10000000])) + 1 
   scale = choice([10,50,250,1000,4000])
   noise_level = choice([0.1, 0.05, 0.01, 0.005, 0.001])
   if type == 'sin':
       period = choice ([1/100, 1/1000, 1/10000, 1/30000])
       f = lambda x, value: sin(x *period ) * random() * scale + random()*noise_level*scale 
   if type == 'gauss':
       f = lambda x, value: gauss( gauss(gauss_arg()[0] + x, gauss_arg()[1]+x), 
                                        uniform(gauss_arg()[2]+x,gauss_arg()[3]+x))
   if type == 'square':
       f = lambda x, value: 8* pow(x,2) - 4*x - random()
   
   if type == 'cubic':
       f = lambda x, value: 3* pow(x,3) - 3* pow(x,2) + 4*x + random()
   value = f(0,0)
   st = 0
   x =  random()  
   while True:       
     if st == step:
         x =  random()
         value = f (x, value)
         st = 0
     st +=1 
     yield round(value*1000)
        
