'''
### Feather M4 Express Main Module
## Allan Shtofenmakher
# Spacecraft Design Lab

# AKA main.py
# Reads SD card file names and communicates with OpenMV camera 
# and SD card breakout board over SPI
# Features NeoPixel rainbow_cycle to indicate proper operation

# Project Start Date: 21 October 2019
# Last Updated: 31 October 2019

'''


# import relevant libraries
import os
import sys
import time
import board
import busio
import storage
import neopixel
import adafruit_sdcard
from digitalio import DigitalInOut, Direction, Pull
from adafruit_bus_device.spi_device import SPIDevice

# set up NeoPixel rainbow_cycle
pixel_pin = board.NEOPIXEL
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

# set up SPI communication
spi = busio.SPI(board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs_cam = DigitalInOut(board.D4)  # use pin 4 for camera
cs_sd = DigitalInOut(board.D5)  # use pin 5 for SD card
camera = SPIDevice(spi, cs_cam, baudrate=115200, polarity=0, phase=0)
sdcard = adafruit_sdcard.SDCard(spi, cs_sd)

# Use the filesystem as normal! Our files are under /sd
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
sys.path.append("/sd")


# define helper function wheel() to improve NeoPixel performance
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


# define helper function color_chase() to improve NeoPixel performance
def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


# define helper function rainbow_cycle() to improve NeoPixel performance
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


# define helper function to print the contents of the SD
def print_directory(path, tabs=0):
    for file in os.listdir(path):
        try:
            stats = os.stat(path + "/" + file)  # changed from statvfs()
            filesize = stats[6]
            isdir = stats[0] & 0x4000
            
            if filesize < 1000:
                sizestr = str(filesize) + " by"
            elif filesize < 1000000:
                sizestr = "%0.1f KB" % (filesize / 1000)
            else:
                sizestr = "%0.1f MB" % (filesize / 1000000)
            
            prettyprintname = ""
            for _ in range(tabs):
                prettyprintname += "   "
            prettyprintname += file
            if isdir:
                prettyprintname += "/"
            print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
            
            #recursively print directory contents
            if isdir:
                print_directory(path + "/" + file, tabs + 1)
        except:
            print('error')
            pass
 

# print SD card file names and stats
print('Files on filesystem:')
print('--------------------')
print_directory("/sd")
print('')

# enable this to see more lights:
# RED = (255, 0, 0)
# YELLOW = (255, 150, 0)
# GREEN = (0, 255, 0)
# CYAN = (0, 255, 255)
# BLUE = (0, 0, 255)
# PURPLE = (180, 0, 255)

# initialize loop index i
i = 0

while True:
    
    # enable this to see more lights:
    # pixels.fill(RED)
    # pixels.show()
    # # Increase or decrease to change the speed of the solid color change.
    # time.sleep(1)
    # pixels.fill(GREEN)
    # pixels.show()
    # time.sleep(1)
    # pixels.fill(BLUE)
    # pixels.show()
    # time.sleep(1)

    # enable this to see more lights:
    # color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    # color_chase(YELLOW, 0.1)
    # color_chase(GREEN, 0.1)
    # color_chase(CYAN, 0.1)
    # color_chase(BLUE, 0.1)
    # color_chase(PURPLE, 0.1)
    
    # increment loop_index, divide by 10, and redefine loop index as remainder
    i = (i+1) % 10  # run from 0 to 9
    
    # run SPI communication once every ten loops  # CHANGED TO 2
    if (i % 2) == 0:
    
      # initialize/reset save_to_SD_flag to disable saving
      save_to_SD_flag = 0
      
      # communicate with camera over SPI
      with camera as spi:
          
          # prepare hello_buffer
          hello_buffer = bytearray(5)
          spi.write_readinto(b'hello', hello_buffer)
          # spi.write(b'hello')  # for writing only
          # spi.readinto(hello_buffer)  # for reading only
          
          # convert hello_buffer into string using strange workaround
          hello_buffer_string = ''.join(chr(b) for b in hello_buffer)
              
          # print message received from camera
          print('buffer string: ' + hello_buffer_string)
          
          # continue if the proper hello_buffer_string has been received
          if hello_buffer_string == 'ready':
              
              # prepare new size_buffer
              size_buffer = bytearray(5)
              
              # receive image size from camera
              spi.write_readinto(b'<OwO>', size_buffer)
              
              # convert bytearray to string
              image_size_string = ''.join(chr(b) for b in size_buffer)
              
              # try to convert image_size_string to integer and continue onwards
              try:
              
                  # convert string to number
                  image_size = int(image_size_string)
              
                  # print size of image to terminal
                  print('number of bytes in photo: ' + image_size_string)
                  
                  # prepare buffer to receive image from camera
                  image_buffer = bytearray(image_size)
                  
                  # indicate start of image transmission
                  print("Receiving image . . . ")
                  
                  # send dummy bytearray; receive image
                  spi.write_readinto(image_buffer, image_buffer)
                  
                  if image_buffer:
                  
                      # indicate completion of image transmission
                      print("Image received!")
                      
                      # print converted image for troubleshooting
                      # print(image_buffer)
                  
                      # change save_to_SD_flag to save image at end of loop
                      save_to_SD_flag = 1
                      
                  else:
                      
                      # indicate failure of image transmission
                      print('')
                      print('Failed to receive message.  File not saved to SD card.')
                      print('')
                  
              # if not possible, print error message
              except:
              
                  # print error message if image_size_string is not numeric
                  print('')
                  print("Message received from camera: " + image_size_string)
                  print("cannot be converted to integer.")
                  print('')
          
          # strange workaround to enable printing bytearray buf (for troubleshooting)
          # print(''.join(chr(b) for b in hello_buffer))
          
          # slow down the process
          time.sleep(0.1)
      
      # if image was received, save image to SD
      if save_to_SD_flag:
      
          # indicate start of save
          print("Saving data . . . ")
          
          # write image to file
          with open('/sd/picture1.jpg', 'wb') as f:
              f.write(image_buffer)
          
          '''
          ### Uncomment this section to test SD card's read/write abilities
          # read image from file
          with open('/sd/picture1.jpg', 'rb') as f:
              image_data = f.read()
              
          # save image under different name
          with open('/sd/picture2.jpg', 'wb') as f:
              f.write(image_data)
          '''
          
          # print success message
          print('Save completed!')
      
      
      # FOR REFERENCE ONLY: 
      # old-fashioned SPI code
      
      # while not spi.try_lock():
      #     pass
      #     
      # try:
      #     spi.configure(baudrate=1000000, phase=0, polarity=0)
      #     cs.value = False
      #     spi.write(b'hello')
      #     cs.value = True
      # finally:
      #     spi.unlock()

    rainbow_cycle(0)  # Increase the number to slow down the rainbow
    
    # time.sleep(0.01) # uncomment and make bigger to slow down
