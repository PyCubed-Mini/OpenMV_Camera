# Trinket IO demo
# Welcome to CircuitPython 2.0.0 :)

import board
from digitalio import DigitalInOut, Direction, Pull
import busio
import touchio
from adafruit_bus_device.spi_device import SPIDevice
import adafruit_dotstar as dotstar
import time

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Analog input on D0
# analog1in = AnalogIn(board.D0)

# Analog output on D1
# aout = AnalogOut(board.D1)

# Digital input with pullup on D2
# button = DigitalInOut(board.D2)
# button.direction = Direction.INPUT
# button.pull = Pull.UP

# Capacitive touch on D3
# touch = touchio.TouchIn(board.D3)

# set up SPI communication
spi = busio.SPI(board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = DigitalInOut(board.D1)  # USE PIN 1
# cs.direction = Direction.OUTPUT
# cs.value = True
device = SPIDevice(spi, cs, baudrate=115200, polarity=0, phase=0)

######################### HELPERS ##############################

# Helper to convert analog input to voltage
def getVoltage(pin):
    return (pin.value * 3.3) / 65536

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  # Read analog voltage on D0
  # print("D0: %0.2f" % getVoltage(analog1in))

  # use D3 as capacitive touch to turn on internal LED
  # if touch.value:
  #     print("D3 touched!")
  # led.value = touch.value

  i = (i+1) % 256  # run from 0 to 255
  
  if (i % 10) == 0:
    
      with device:
          # spi.write(b'hello')
          buf = bytearray(5)
          # spi.write(b'hello')  # for writing only
		  # spi.readinto(buf)  # for reading only
          spi.write_readinto(b'hello', buf)
		  
		  # strange workaround to enable printing bytearray buf
          # print(buf)
          print(''.join(chr(b) for b in buf))
		  
		  # slow down the process
          time.sleep(0.1)
      
      # while not spi.try_lock():
      #     pass
      # 	
      # try:
      #     spi.configure(baudrate=1000000, phase=0, polarity=0)
      #     cs.value = False
      #     spi.write(b'hello')
      #     cs.value = True
      # finally:
      #     spi.unlock()
		  
  time.sleep(0.01) # make bigger to slow down
