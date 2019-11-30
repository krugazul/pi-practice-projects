from gpiozero import DigitalOutputDevice
from time import sleep

pinAred = DigitalOutputDevice(17)
pinByellow = DigitalOutputDevice(27)
pinCgreen = DigitalOutputDevice(22)
pinDblack = DigitalOutputDevice(23)

pinEred = DigitalOutputDevice(13)
pinFyellow = DigitalOutputDevice(6)
pinGgreen = DigitalOutputDevice(5)
pinHblack = DigitalOutputDevice(12)

pinAred.off()
pinByellow.on()
pinCgreen.on()
pinDblack.off()
pinEred.off()
pinFyellow.off()
pinGgreen.on()
pinHblack.on()
sleep(1)

pinAred.close()
pinByellow.close()
pinCgreen.close()
pinDblack.close()
pinEred.close()
pinFyellow.close()
pinGgreen.close()
pinHblack.close()