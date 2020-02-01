import RPi.GPIO as GPIO
import time

BUTTON = 16
LED = 21
LED2 = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)#Button to GPIO16
GPIO.setup(LED, GPIO.OUT)  #LED to GPIO21
GPIO.setup(LED2, GPIO.OUT)  #LED to GPIO6

try:
    while True:
         button_state = GPIO.input(BUTTON)
         if button_state == True:
             GPIO.output(LED2, False)
             GPIO.output(LED, True)
             time.sleep(0.5)
         else:
             GPIO.output(LED, False)
             GPIO.output(LED2, True)
             time.sleep(0.5)
except:
    GPIO.cleanup()