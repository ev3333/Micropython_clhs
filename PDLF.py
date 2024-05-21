from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
sensor1 = ColorSensor(Port.A)
sensor2 = ColorSensor(Port.B)
black_intensity = 

def callibration(max_intensity, min_intensity):
    callibrated = 



##Brake as boolean

def PDLF_CheckT(speed, kp, kd, black_intensity, stop):
    while sensor1.reflection() > black_intensity and sensor2.reflection() > black_intensity:
        derivative = error - last_error 
        error = sensor1 - sensor2
        correction = error*kp + derivative*kd
        speed + correction
        speed - correction
    
    if stop == True:
        ##Brake
    else 
        ##None
        


    
    

