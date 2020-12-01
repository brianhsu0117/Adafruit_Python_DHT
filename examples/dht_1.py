#!/usr/bin/python3
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)

GPIO_PIN = 4
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        h0, t0 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, GPIO_PIN)
        if h0 is not None and t0 is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(t0, h0))
        else:
            print('Failed to get reading. Try again!')
        time.sleep(1)
except KeyboardInterrupt:
    print('關閉程式')
