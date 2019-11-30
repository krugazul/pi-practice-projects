
from segmentDisplay import Segment

pins = [17,27,22,23,13,6,5,12]
segment1 = Segment(pins)
segment1.setLetterTime(2)
segment1.printLetterTime()
segment1.display('a')
segment1.display('b')
segment1.display('c')
