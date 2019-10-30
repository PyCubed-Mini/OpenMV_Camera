'''
### Fine Snapshot Calibration
## Allan Shtofenmakher
# Spacecraft Design Lab

# MODIFIED FROM EXAMPLE SCRIPT: SNAPSHOT.PY

# Uses the camera to take one VGA-style photo of high quality,
# then saves it to the SD card under filename chosen by user.

# The blue LED is used to signal camera activation;
# the green LED signals successful code execution;
# a flashing red LED signals an error.

# The user is expected to use the SD card to run this code,
# remove the SD card after each use, read the SD card on a 
# computer, and rename the file directly on the SD card or
# move the file to the computer and rename it there.  At each
# stage, the most focused photos should be compared to one 
# another, and the user should tweak the camera focus slightly
# in a direction expected to improve focus.  Repeat until the 
# focus level is adequate.

# DEFINE FILE NAME BELOW.

# Note: Do NOT run this code without an SD card attached.
# Note: Do NOT run this code from the OpenMV IDE.

# Project Start Date: 15 October 2019
# Last Updated: 28 October 2019

'''


# NAME YOUR FILE HERE (use '.jpg' format only):
# example: filename = "my_image.jpg"
filename = "example"

# manipulate filename as needed
if filename[-4:] == '.jpg':
    
    # print encouraging message if format of filename is '.jpg'
    print('')
    print('Thanks for putting \'.jpg\' at the end of your file name!')
    print('')
    
elif '.' not in filename:

    # print neutral message if no format specified
    print('Your file name has been updated!')
    
    # append '.jpg' to filename
    filename = filename + '.jpg'
    
    # print updated filename
    print('')
    print('Updated filename: %s' % filename)
    print('')

else:

    # print discouraging message otherwise
    print('')
    print('This camera can only save VGA images as JPG files.')
    print('Consider changing your file name accordingly.')
    print('')

    # append '.jpg' to filename
    filename = filename + '.jpg'
    
    # print updated filename
    print('Updated filename: %s' % filename)
    print('')

# import relevant libraries
import sensor, image, pyb

# use colors to annoy people during testing
RED_LED_PIN = 1
GREEN_LED_PIN = 2
BLUE_LED_PIN = 3

# initialize camera and define camera settings
sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.VGA)    # Set frame size to VGA (640x480)
sensor.skip_frames(time = 2500)     # Wait for settings take effect.

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# print snapshot start message to serial monitor
print("Taking photo . . . ")

# actually take photo and save to SD card
sensor.snapshot().compressed(quality=75).save("%s" % filename)

# print snapshot end message to serial monitor
print("Photo complete!")

# turn camera indicator off
pyb.LED(BLUE_LED_PIN).off()

# pause to allow time for processing
sensor.skip_frames(time = 500)

# flash light to indicate successful execution of code
pyb.LED(GREEN_LED_PIN).on()
sensor.skip_frames(time = 500)
pyb.LED(GREEN_LED_PIN).off()
