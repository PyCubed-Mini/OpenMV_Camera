'''
### Coarse Video Calibration
## Allan Shtofenmakher
# Spacecraft Design Lab

# MODIFIED FROM EXAMPLE SCRIPT: HELLOWORLD.PY

# Uses the camera to take VGA-style photos continuously, as if the
# camera was recording a video.  Video is not saved.

# The blue LED is used to signal that the camera is active.

# Run this code directly from the OpenMV IDE, and use what is
# displayed in the IDE frame buffer to focus the camera by hand.
# This is simply a coarse calibration to set up an "initial guess"
# prior to running fine_snapshot_calibration.py.

# Project Start Date: 15 October 2019
# Last Updated: 28 October 2019

'''


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
sensor.skip_frames(time = 2000)     # Wait for settings take effect.

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# take snapshots continuously to emulate video effect
while(True):

    img = sensor.snapshot()         # Take a picture and return the image.
