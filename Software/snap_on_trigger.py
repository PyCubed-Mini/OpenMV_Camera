'''
### Snap on Trigger
## Allan Shtofenmakher
# Spacecraft Design Lab

# Take a photo with the camera and communicate data over SPI to microcontroller with the intention
# of saving it to the SD card

# Note: Do NOT run this code without an SD card attached.

# Project Start Date: 10 October 2019
# Last Updated: 22 October 2019

'''


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
# spi = SPI(2, SPI.MASTER, baudrate = 115200, polarity=1, phase=0)  # use in case MASTER is needed
spi = SPI(2, SPI.SLAVE, polarity=0, phase=0)

# define chip-select switch (P3) as pull-up
pyb.Pin("P3", pyb.Pin.IN, pull=pyb.Pin.PULL_UP)

# prepare buffer
buf = bytearray(5)

# print for troubleshooting:
# print(buf)

# some experimental code:
# spi.send(b'heyyy')  # send five-byte string
# spi.send('hello')  # doesn't work because of lack of preceding 'b'
# spi.recv(buf)  # for receiving only
# print(buf)  # for troubleshooting

# send AND receive five-byte string
spi.send_recv(b'heyyy', buf)

print(''.join(chr(b) for b in buf))

# for troubleshooting, print out the individual bytes of the buffer one at a time
# for i in range(5):
#     print(buf[i])

# turn SPI indicator off
pyb.LED(RED_LED_PIN).off()

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 2500) # let new settings take effect

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# print start message to serial monitor
print("Taking photo . . . ")

# actually take photo
sensor.snapshot()#.compress(90).save("example90.jpg") # or "example90.bmp" (or others)

# print completion message to serial monitor
print("Done!")

# turn camera indicator off
pyb.LED(BLUE_LED_PIN).off()
