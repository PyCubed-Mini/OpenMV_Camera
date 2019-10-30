'''
### Manual Process Delay Test
## Allan Shtofenmakher
# Spacecraft Design Lab

# Take a photo with the camera and save it to the SD card.

# The blue LED is used to signal camera activation;
# the green LED signals successful code execution;
# a flashing red LED signals an error.

# The variable being tested here is the PROCESSING TIME, 
# or the time allotted to the camera for processing images after
# they are taken.

# This code does not loop through processing times automatically.
# You MUST change process_time between tests manually in the code.

# Note: Do NOT run this code without an SD card attached.
# Note: Do NOT run this code from the OpenMV IDE.

# Project Start Date: 20 October 2019
# Last Updated: 28 October 2019

'''


# import relevant libraries
import sensor, image, pyb

# use colors to annoy people during testing
RED_LED_PIN = 1
GREEN_LED_PIN = 2
BLUE_LED_PIN = 3

# define a list of process times
# use this as a reference only for manually changing the process_time
process_delay_array = [10, 50, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 9999]

# set process_time manually
process_time = 3000

# flash light to signal camera activation
pyb.LED(BLUE_LED_PIN).on()

# print message to serial monitor
print("Testing process time: %4d ms" % process_time)

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 2500) # let new settings take effect

# print snapshot start message to serial monitor
print("Taking photo . . . ")

# actually take photo and save to SD card
sensor.snapshot().compressed(quality=75).save("process_%04d_ms.jpg" % process_time)

# print snapshot end message to serial monitor
print("Photo complete!")

# turn camera indicator off
pyb.LED(BLUE_LED_PIN).off()

# pause to allow time for processing
sensor.skip_frames(time = process_time)

# print completion message to serial monitor
print("Done!")

# flash light to indicate successful execution of code
pyb.LED(GREEN_LED_PIN).on()
sensor.skip_frames(time = 10)  # shorter than usual
pyb.LED(GREEN_LED_PIN).off()
