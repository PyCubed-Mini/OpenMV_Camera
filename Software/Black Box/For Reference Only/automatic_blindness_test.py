'''
### Automatic Blindness Test (DEPRECATED)
## Allan Shtofenmakher
# Spacecraft Design Lab

# DEPRECATED: For some reason, only the first photo in the sequence
# can be subject to "blinding," so it's not useful to take photos
# in sequence.  Also, the code is rather unstable.  
# Recommended alternative is manual_blindness_test.py.

# Uses the camera to take several photos in sequence, shutting
# the camera eye between snapshots, rendering the camera "blind."
# The time between snapshots continuously decreases until the
# camera is unable to take the image in time.  Saves all photos
# to the SD card.

# The blue LED is used to signal camera activation;
# the green LED signals successful code execution;
# a flashing red LED signals an error.

# The variable being tested here is the BLINDNESS TIME, 
# or the time allotted to the camera for setup after reset.

# This code loops through blindness times automatically.
# There is no need to change blindness_time between tests
# manually in the code.  However, it may be necessary to remove
# some of the smaller blindness_time values from blindness_array
# to prevent the camera from throwing errors.

# Note: Do NOT run this code without an SD card attached.
# Note: Do NOT run this code from the OpenMV IDE.

# Project Start Date: 27 October 2019
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

# define a list of blindness times
blindness_array = [10, 50, 100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 5000, 9999]
blindness_array.reverse()  # go largest to smallest

# loop through all blindness times
for blindness_time in blindness_array:
    
    # flash light to signal camera activation
    pyb.LED(BLUE_LED_PIN).on()

    # print message to serial monitor
    print("Testing blindness for: %4d ms" % blindness_time)
    
    # instantaneously make the computer shut its eye
    sensor.sleep(True)
    sensor.sleep(False)

    # initialize camera and define camera settings
    sensor.reset() # initialize the camera sensor
    sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
    sensor.set_framesize(sensor.VGA) # or sensor.QVGA (or others)
    sensor.skip_frames(time = blindness_time) # let new settings take effect ("be blind")
    
    # print snapshot start message to serial monitor
    print("Taking photo . . . ")
    
    # actually take photo and save to SD card
    sensor.snapshot().compressed(quality=50).save("blindness_%04d_ms.jpg" % blindness_time)
    
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