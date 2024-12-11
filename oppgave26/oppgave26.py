from machine import Pin
import time

sensorPin = Pin(19,Pin.IN)
ledPin = Pin(15,Pin.OUT)

try:
    while True:
        if sensorPin.value(): #gjorde om slik at den ikke lyser når den detekterer bevegelser, og lyser når den detekterer. enklere å vise frem
            ledPin.value(1)
        else:
            ledPin.value(0)
            
except:
    pass