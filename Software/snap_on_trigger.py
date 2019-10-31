'''
### Snap on Trigger
## Allan Shtofenmakher
# Spacecraft Design Lab

# Take a photo with the camera and communicate data over SPI to microcontroller with the intention
# of saving it to the SD card

# Note: Do NOT run this code without an SD card attached.

# Project Start Date: 10 October 2019
# Last Updated: 31 October 2019

'''


## Setup

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



## Snapshot

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 2500) # let new settings take effect

# print snapshot start message to serial monitor
print("Taking photo . . . ")

# actually take photo  # currently doesn't save
img = sensor.snapshot().compressed(30)#.save("example90.jpg") # or "example90.bmp" (or others)

# print snapshot end message to serial monitor
print("Photo complete!")

# turn camera indicator off
pyb.LED(BLUE_LED_PIN).off()



# Image Processing

# print image properties
print(img)  # most important properties
print("number of bytes: " + str(img.size()))  # img.size() = len(img[:]), but works better


# write image to file
with open('picture_out.png', 'wb') as f:
    f.write(img)

# print message to indicate completion
print('Save Checkpoint 1!')


# read image from file
with open('picture_out.png', 'rb') as f:
    img_data = f.read()

# print message to indicate completion
print('Save Checkpoint 2!')


'''
### Run this to verify that the data from Checkpoint 2 makes the same image as in Checkpoint 1
with open('picture_out_out.png', 'wb') as f:
    f.write(img_data)

print('Save Checkpoint 3!')
'''


# print img_data for troubleshooting (should see bytes, 'JFIF', and weird stuff like P7<F<2PFAFZUP_)
# print(img_data)



### Communication

# flash light to indicate waiting for SPI signal
pyb.LED(RED_LED_PIN).on()

# prepare hello_buffer
hello_buffer = bytearray(5)
spi.send_recv(b'ready', hello_buffer)

# print message received from MCU
print(''.join(chr(b) for b in hello_buffer))

# determine size of image
# image_size = img.size()  # if img is being sent to MCU
image_size = len(img_data)  # if img_data is being sent to MCU

# create new size_buffer based on image_size
size_buffer = bytearray(len(str(image_size)))  # str() converts num 2 str, len() produces numeric input

# send that size to the MCU in a robust way
# print(str(image_size))  # print for troubleshooting
spi.send_recv(bytearray(str(image_size)), size_buffer)

# print message received from MCU
print(''.join(chr(b) for b in size_buffer))

# send image
# spi.send_recv(img, bytearray(image_size))
# spi.send(img)  # a straight send works
# spi.send_recv(img_data, bytearray(image_size))
spi.send(img_data)  # straight send SHOULD work and is the best because it's not limited by camera RAM

# print completion message to serial monitor
print("Done!")

# turn SPI indicator off
pyb.LED(RED_LED_PIN).off()



## Optional Code Blocks


'''
### Original "hello" communication code block
# prepare buffer
buf = bytearray(5)

# print for troubleshooting:
# print(buf)

# send AND receive five-byte string
spi.send_recv(b'heyyy', buf)

print(''.join(chr(b) for b in buf))

# for troubleshooting, print out the individual bytes of the buffer one at a time
# for i in range(5):
#     print(buf[i])
'''


'''
### Image print options for troubleshooting
# print(img[:])
# print(len(img[:]))
# print(img)
'''


'''
### Use this block of code to print out the RGB values of the image ###
fh = open('test.txt', 'w')  # 'rb' = 'read binary'
fh.write('(')
for i in range(img.size()):
    if i != 0:
        fh.write(', ')
    # print(i)
    fh.write(str(img[i]))

fh.write(')')
fh.close()
'''
