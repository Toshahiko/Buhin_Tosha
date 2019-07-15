import random
import math


def GenerateRandomValue() :
    ran_val = random.random()
    return ran_val


def Distance( x, y ) :
    dist =  x*x + y*y
    return dist


sum = 0
num_of_times = 10000

for i in range( num_of_times ) :
    point_x = GenerateRandomValue()
    point_y = GenerateRandomValue()

    distance = Distance( point_x, point_y )
    if distance < 1.0 :
        sum += 1
        
print( 4*sum/num_of_times )