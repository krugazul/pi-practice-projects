from gpiozero import DigitalOutputDevice

class Segment():

    pinA = ''
    pinB = ''
    pinC = ''
    pinD = ''
    pinE = ''
    pinF = ''
    pinG = ''
    pinH = ''

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
        self.pinA = DigitalOutputDevice(a)
        self.pinB = DigitalOutputDevice(b)
        self.pinC = DigitalOutputDevice(c)
        self.pinD = DigitalOutputDevice(d)
        self.pinE = DigitalOutputDevice(e)
        self.pinF = DigitalOutputDevice(f)
        self.pinG = DigitalOutputDevice(g)
        self.pinH = DigitalOutputDevice(h)

    def display(self,letter):
        if 'a' == letter: self.A()
        if 'b' == letter: self.B()
        if 'c' == letter: self.C()

    def A(self):
        self.pinA.off()
        self.pinB.off()
        self.pinC.off()
        self.pinD.on()
        self.pinE.off()
        self.pinF.off()
        self.pinG.off()
        self.pinH.on()   

    def B(self):
        self.pinA.on()
        self.pinB.on()
        self.pinC.off()
        self.pinD.off()
        self.pinE.off()
        self.pinF.off()
        self.pinG.off()
        self.pinH.on()

    def C(self):
        self.pinA.off()
        self.pinB.on()
        self.pinC.on()
        self.pinD.off()
        self.pinE.off()
        self.pinF.off()
        self.pinG.on()
        self.pinH.on()

