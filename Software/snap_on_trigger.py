# Snap on Trigger
#
# Take a photo with the camera and communicate data over SPI to microcontroller with the intention
# of saving in to the SD card
#
# Note: Do NOT run this code without an SD card attached.
#
# Project Start Date: 10 October 2019

# import relevant libraries
import sensor, image, pyb
from pyb import SPI

# use colors to annoy people during testing
RED_LED_PIN = 1
GREEN_LED_PIN = 2
BLUE_LED_PIN = 3

# flash light to indicate waiting for SPI signal
pyb.LED(RED_LED_PIN).on()

# set up digital SPI interface, with camera as slave and MCU as master
spi = SPI(2, SPI.SLAVE, polarity=0, phase=0)
# spi = SPI(2, SPI.MASTER, baudrate = 115200, polarity=1, phase=0)
pyb.Pin("P3", pyb.Pin.IN, pull=pyb.Pin.PULL_UP)

# spi.send(b'heyyy')  # respond
# spi.send('hello')
buf = bytearray(5)
# print(buf)

# spi.recv(buf)  # for receive only
spi.send_recv(b'heyyy', buf)

# print(buf)
print(''.join(chr(b) for b in buf))
# for i in range(5):
#     print(buf[i])

# turn SPI indicator off
pyb.LED(RED_LED_PIN).off()

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 500) # let new settings take effect

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# print start message to serial monitor
print("Taking photo . . . ")

# actually take photo
sensor.snapshot()#.save("example.jpg") # or "example.bmp" (or others)

# print completion message to serial monitor
print("Done!")

# turn camera indicator off
pyb.LED(BLUE_LED_PIN).off()
