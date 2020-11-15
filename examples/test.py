try:
    import RPi.GPIO as GPIO    
except:
    import Mock.GPIO as GPIO

import time

def cb():
    print("Callback called")

print("set mode")
GPIO.setmode(GPIO.BCM)
print("set warning false")
GPIO.setwarnings(False)
GPIO.setup(15,GPIO.OUT)
GPIO.output(15,GPIO.HIGH)
GPIO.input(15)
time.sleep(1)
GPIO.add_event_detect(15,GPIO.BOTH,cb,0)
GPIO.output(15,GPIO.LOW)
GPIO.input(15)
GPIO.wait_for_edge(15,GPIO.BOTH, 0, 0)
GPIO.wait_for_edge(15,GPIO.BOTH, 0, 10)
GPIO.gpio_function(15)