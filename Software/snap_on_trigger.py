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
spi = SPI(2, SPI.SLAVE) # (2, SPI.SLAVE, baudrate=1000000, polarity=1, phase=0)
# spi.send('hello')
spi.recv(5) # receive 5 bytes on the bus
print(spi.recv(5))
# spi.send_recv('hello') # send a receive 5 bytes


# turn SPI indicator off
pyb.LED(RED_LED_PIN).off()

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 2000) # let new settings take effect

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
