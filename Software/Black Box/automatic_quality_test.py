'''
### Automatic Quality Test
## Allan Shtofenmakher
# Spacecraft Design Lab

# Uses the camera to take several photos in sequence, rendering
# a different level of JPEG compression each time.  Saves all
# photos to the SD card.

# The blue LED is used to signal camera activation;
# the green LED signals successful code execution;
# a flashing red LED signals an error.

# The variable being tested here is the QUALITY of JPEG compression. 

# This code loops through quality values automatically, so there is
# no need to change quality_value between tests manually in the code.

# Note: Do NOT run this code without an SD card attached.
# Note: Do NOT run this code from the OpenMV IDE.

# Project Start Date: 21 October 2019
# Last Updated: 28 October 2019

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

# define a list of quality values
quality_array = [1, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90]  # unstable for quality>90

# loop through all quality values
for quality_value in quality_array:
    
    # flash light to signal camera activation
    pyb.LED(BLUE_LED_PIN).on()

    # print message to serial monitor
    print("Testing quality=%d" % quality_value)
    
    # print snapshot start message to serial monitor
    print("Taking photo . . . ")
    
    # actually take photo and save to SD card
    sensor.snapshot().compressed(quality=quality_value).save("quality_%02d.jpg" % quality_value)
    
    # print snapshot end message to serial monitor
    print("Photo complete!")
    
    # turn camera indicator off
    pyb.LED(BLUE_LED_PIN).off()

    # pause to allow time for processing
    sensor.skip_frames(time = 3000)

# print completion message to serial monitor
print("Done!")

# flash light to indicate successful execution of code
pyb.LED(GREEN_LED_PIN).on()
sensor.skip_frames(time = 500)
pyb.LED(GREEN_LED_PIN).off()