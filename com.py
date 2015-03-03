import RPi.GPIO as GPIO
import time
import binascii
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(24,GPIO.OUT)


string1 = ""
count = 1
listen = 0

try:

    while True:
        input_value22 = GPIO.input(22)
        if(input_value22 == 1):
            if(listen == 0):
                listen = 1
                print('Now listening')
                string1 = ""
            else:
                listen = 0
                print('\nStop listening')
                print('Message:'),string1
                text = ''.join(chr(int(string1[i:i+8], 2))
                for i in xrange(0, len(string1), 8))
                print('Message:'),text
        if(listen == 1):
            input_value4 = GPIO.input(4)
            input_value17 = GPIO.input(17)
            if(input_value4 == 1):
                GPIO.output(24,GPIO.HIGH)
                sys.stdout.write("1")
                string1 = string1 + '1'
            if(input_value17 == 1):
                GPIO.output(24,GPIO.HIGH)
                sys.stdout.write("0")
                string1 = string1 + '0'
            time.sleep(.5)
            GPIO.output(24,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
