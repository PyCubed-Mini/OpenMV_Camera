'''
### SPI Troubleshooter
## Allan Shtofenmakher
# Spacecraft Design Lab

# Run this code to troubleshoot the SPI connection with the MCU.

# Camera is set up to communicate constantly with the microcontroller (MCU).  MCU is MASTER;
# camera is SLAVE.  Red LED flashes when message is received.  Check serial terminal to ensure that
# correct message is received.

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

# set up digital SPI interface, with camera as slave and MCU as master
# spi = SPI(2, SPI.MASTER, baudrate = 115200, polarity=1, phase=0)  # use in case MASTER is needed
spi = SPI(2, SPI.SLAVE, polarity=0, phase=0)

# define chip-select switch (P3) as pull-up
pyb.Pin("P3", pyb.Pin.IN, pull=pyb.Pin.PULL_UP)

# loop ad infinitum
while True:

    # flash light off to indicate waiting for SPI signal
    pyb.LED(RED_LED_PIN).off()

    # prepare/refresh buffer
    buf = bytearray(5)

    # for troubleshooting
    # print(buf)

    # send/receive message
    # spi.recv(buf)  # for receiving only
    spi.send_recv(b'heyyy', buf)

    # for troubleshooting
    # print(buf)

    # print received message
    print(''.join(chr(b) for b in buf))

    # flash light on to indicate reception of SPI signal
    pyb.LED(RED_LED_PIN).on()

    # pause briefly to indicate end of loop
    sensor.skip_frames(1)

