'''
### Automatic Process Delay Test (DEPRECATED)
## Allan Shtofenmakher
# Spacecraft Design Lab

# DEPRECATED: For some reason, only the last photo in the sequence
# can be subject to the effects of processing delay, so it's not 
# useful to take photos in sequence.  It is currently believed
# corruption of saved images during the processing phase occurs
# due to the camera shutting off before processing is complete.
# Recommended alternative is manual_process_delay_test.py.

# Uses the camera to take several photos in sequence, decreasing
# the time allotted to image processing each time until, 
# ultimately, the camera is unable to process the image in time.
# Saves all photos to the SD card.

# The blue LED is used to signal camera activation;
# the green LED signals successful code execution;
# a flashing red LED signals an error.

# The variable being tested here is the PROCESSING TIME, 
# or the time allotted to the camera for processing images after
# they are taken.

# This code loops through processing times automatically.
# There is no need to change process_time between tests
# manually in the code.  However, it may be necessary to remove
# some of the smaller process_time values from
# process_delay_array to prevent the camera from throwing errors.

# Note: Do NOT run this code without an SD card attached.
# Note: Do NOT run this code from the OpenMV IDE.

# Project Start Date: 20 October 2019
# Last Updated: 28 October 2019
# DEPRECATED AS OF: 28 October 2019
# Provided for reference only

'''


# import relevant libraries
import sensor, image, pyb

# use colors to annoy people during testing
RED_LED_PIN = 1
GREEN_LED_PIN = 2
BLUE_LED_PIN = 3

# initialize camera and define camera settings
sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 2500) # let new settings take effect

# define a list of process times
process_delay_array = [10, 50, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 9999]
process_delay_array.reverse()  # go largest to smallest

# loop through all process times
for process_time in process_delay_array:
    
    # flash light to signal camera activation
    pyb.LED(BLUE_LED_PIN).on()

    # print message to serial monitor
    print("Testing process time: %4d ms" % process_time)
    
    # print snapshot start message to serial monitor
    print("Taking photo . . . ")
    
    # actually take photo and save to SD card
    sensor.snapshot().compressed(quality=50).save("process_%04d_ms.jpg" % process_time)
    
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
sensor.skip_frames(time = 500)
pyb.LED(GREEN_LED_PIN).off()
