"""
image_compression_tile.py - By: Keiko Nagami - Sat Feb 8 2020
- Takes an RGB image of size 320x240
- Breaks image up into 16x16 pixel blocks
- JPEG compress each block, and save each compressed block to SD card on camera board
- Run this with camera board WITH SD card plugged in
"""

# import relevant libraries
import sensor, image

sensor.reset() # initialize the camera sensor
sensor.set_pixformat(sensor.RGB565) # sensor.RGB565 takes RGB image
sensor.set_framesize(sensor.QVGA) # sensor.QVGA takes 320x240 image
sensor.skip_frames(time = 2500) # let new settings take effect

img = sensor.snapshot() # take an image
print(img)  # most important image properties
m = 16 # 16x16 pixel blocks
x_num_blocks = 320/m # number of 16x16 blocks in the x dimension (columns)
y_num_blocks = 240/m # number of 16x16 blocks in the y dimension (rows)
for i in range(x_num_blocks):
    for j in range(y_num_blocks):
        pixel_block = img.copy(roi=(i*m,j*m,m,m))
        pixel_block_jpeg = pixel_block.compressed(30)
        print(i,j,pixel_block_jpeg) # 16x16 tile properties
        with open('picture_out_' + str(i) + '_' + str(j) + '.png', 'wb') as f:
            f.write(pixel_block_jpeg)
