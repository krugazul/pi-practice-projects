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

pinAred.on()
pinByellow.off()
pinCgreen.off()
pinDblack.off()
pinEred.off()
pinFyellow.on()
pinGgreen.off()
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