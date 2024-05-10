from machine import Pin, PWM, ADC
from servo import Servo 
import time

motor = Servo(Pin(22))

while True:
  motor.move(0)
  time.sleep(2)
  motor.move(45)
  time.sleep(2)
  motor.move(90)
  time.sleep(2)
  motor.move(180)
  time.sleep(2)
  
  
