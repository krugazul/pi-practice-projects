from gpiozero import DigitalOutputDevice
from time import sleep

class Segment():
    letterTime = 1
    inputPins = []
    charMatrix = {
        'A':[0,0,0,1,0,0,0,1],
        'a':[0,0,0,0,0,1,0,1],
        'B':[0,0,0,0,0,0,0,1],
        'b':[1,1,0,0,0,0,0,1],
        'C':[0,1,1,0,0,0,1,1],
        'c':[1,1,1,0,0,1,0,1],
        'D':[0,0,0,0,0,0,1,1],
        'd':[1,0,0,0,0,1,0,1],
        'E':[0,1,1,0,0,0,0,1],
        'e':[0,1,1,0,0,0,0,1],
        'F':[0,1,1,1,0,0,0,1],
        'f':[0,1,1,1,0,0,0,1],
        '0':[0,0,0,0,0,0,1,1],
        '1':[1,0,0,1,1,1,1,1],
        '2':[0,0,1,0,0,1,0,1],
        '3':[0,0,0,0,1,1,0,1],
        '4':[1,0,0,1,1,0,0,1],
        '5':[0,1,0,0,1,0,0,1],
        '6':[0,1,0,0,0,0,0,1],
        '7':[0,0,0,1,1,1,1,1],
        '8':[0,0,0,0,0,0,0,1],
        '9':[0,0,0,0,1,0,0,1],
        '.':[1,1,1,1,1,1,1,0],
        '-':[1,1,1,1,1,1,0,1],
    }

    """
    Extends :class:`DigitalOutputDevice` and represents a 7 segment display
    (7SegmentDisplay).

	7 segment displays are among the simplest display units to display the numbers and characters.
	As shown in the above image of a 7-segment display, it consists of 8 LEDs, 
	each LED used to illuminate one segment of unit and the 8thLED used to illuminate DOT in 7 segment display. 
	
	We can refer each segment as a LINE, as we can see there are 7 lines in the unit,
	which are used to display a number/character.
	We can refer each segment "a,b,c,d,e,f,g" and for dot character we will use "h".
	There are 10 pins, in which 8 pins are used to refer a,b,c,d,e,f,g and h/dp, the two middle pins are common anode/cathode of all he LEDs.
	These common anode/cathode are internally shorted so we need to connect only one COM pin.

    :type pin: int or str
    :param pin:
        The GPIO pin which the LED is connected to. See :ref:`pin-numbering`
        for valid pin numbers. If this is :data:`None` a :exc:`GPIODeviceError`
        will be raised.

    :param bool active_high:
        If :data:`True` (the default), the LED will operate normally with the
        circuit described above. If :data:`False` you should wire the cathode
        to the GPIO pin, and the anode to a 3V3 pin (via a limiting resistor).

    :type initial_value: bool or None
    :param initial_value:
        If :data:`False` (the default), the LED will be off initially.  If
        :data:`None`, the LED will be left in whatever state the pin is found
        in when configured for output (warning: this can be on).  If
        :data:`True`, the LED will be switched on initially.

    :type pin_factory: Factory or None
    :param pin_factory:
        See :doc:`api_pins` for more information (this is an advanced feature
        which most users can ignore).
    """

    def __init__(self,inputPins):
        for inputPin in inputPins:
            self.inputPins.append(DigitalOutputDevice(inputPin))

    def setLetterTime(self,time):
        self.letterTime = time

    def printLetterTime(self):
        print(self.letterTime)

    def printPins(self):
        print(self.inputPins)

    def display(self,char):
        for count, value in enumerate(self.charMatrix[char]):
            if 0 == value:
                self.inputPins[count].off()
            else:
                self.inputPins[count].on()
        
        sleep(self.letterTime)

    def selfTest(self):
        self.setLetterTime(0.5)
        self.display('A')
        self.display('a')
        self.display('B')
        self.display('b')
        self.display('C')
        self.display('c')
        self.display('D')
        self.display('d')
        self.display('E')
        self.display('e')
        self.display('F')
        self.display('f')
        self.display('-')
        self.display('.')
        self.display('0')
        self.display('1')
        self.display('2')
        self.display('3')
        self.display('4')
        self.display('5')
        self.display('6')
        self.display('7')
        self.display('8')
        self.display('9')
