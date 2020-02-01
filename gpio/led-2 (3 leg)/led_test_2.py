from gpiozero import LED
from time import sleep

led_1 = LED(21)
led_2 = LED(6)

while True:
    led_1.on()
    led_2.on()
    sleep(1)
    led_1.off()
    led_2.off()
    sleep(1)