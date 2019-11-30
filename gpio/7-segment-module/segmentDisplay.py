from gpiozero import DigitalOutputDevice
from time import sleep

class Segment():

    letterTime = 1
    pins = {}

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

    def __init__(self,a,b,c,d,e,f,g,h):
        self.pins['A'] = DigitalOutputDevice(a)
        self.pins['B'] = DigitalOutputDevice(b)
        self.pins['C'] = DigitalOutputDevice(c)
        self.pins['D'] = DigitalOutputDevice(d)
        self.pins['E'] = DigitalOutputDevice(e)
        self.pins['F'] = DigitalOutputDevice(f)
        self.pins['G'] = DigitalOutputDevice(g)
        self.pins['H'] = DigitalOutputDevice(h)

    def setLetterTime(self,time):
        self.letterTime = time

    def display(self,letter):
        if 'a' == letter: self.A()

        sleep(self.letterTime)

    def A(self):
        self.pins['A'].off()
        self.pins['B'].off()
        self.pins['C'].off()
        self.pins['D'].on()
        self.pins['E'].off()
        self.pins['F'].off()
        self.pins['G'].off()
        self.pins['H'].on()

