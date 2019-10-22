# CircuitPython demo - NeoPixel
import time
import board
import busio
import neopixel
from digitalio import DigitalInOut, Direction, Pull
from adafruit_bus_device.spi_device import SPIDevice

pixel_pin = board.NEOPIXEL
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

# set up SPI communication
spi = busio.SPI(board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs_cam = DigitalInOut(board.D4)  # USE PIN 4
# cs.direction = Direction.OUTPUT
# cs.value = True
camera = SPIDevice(spi, cs_cam, baudrate=115200, polarity=0, phase=0)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

i = 0
while True:
    # pixels.fill(RED)
    # pixels.show()
    # # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
    # pixels.fill(GREEN)
    # pixels.show()
    # time.sleep(1)
    # pixels.fill(BLUE)
    # pixels.show()
    # time.sleep(1)

    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)
    
    i = (i+1) % 10  # run from 0 to 9
    
    if (i % 10) == 0:
    
      with camera:
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

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
    
    time.sleep(0.01) # make bigger to slow down
