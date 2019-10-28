MOTIVATION:

- Focusing the lens enables the Qube to take pictures of faraway objects, like the Earth, with clarity
- The quality trade study helps us determine what image compression level is best for ensuring that the images the Qube takes are of sufficient quality without being too large
- The time delay trade studies help us understand how much time we need for certain operations and how this translates into power consumption

INSTRUCTIONS FOR USE:

How to focus the lens:
0) Ensure an SD card is connected to the OpenMV device
1) Connect the OpenMV device to a computer via USB cable
2) Open the OpenMV IDE on your computer and open coarse_video_calibration.py from the IDE
3) Run coarse_video_calibration.py directly from the OpenMV IDE via the green "play" button
4) Point the camera at a faraway object.  Use the IDE's frame buffer (nominally in the top right corner of the IDE) to see what the camera sees.  
5) Continue watching the frame buffer as you slowly twist the camera lens until the faraway object comes into focus.
6) Stop running coarse_video_calibration.py (red "X" button)
7) Open fine_snapshot_calibration.py from the IDE
8) At the top of the IDE window, click on "Tools" > "Save open script to OpenMV cam" to save the current code to the SD card
9) Safely remove hardware and disconnect OpenMV device from computer
10) Take a picture of the same faraway object by supplying power to the OpenMV device.  One way to do this is to reconnect the OpenMV device to the computer via USB cable.  It is important not to use the IDE to run the program---if you do, the image won't save to the SD card.
11) Safely disconnect OpenMV device from power (e.g., safely remove hardware and disconnect)
12) Remove microSD card from OpenMV device
13) Connect microSD card to computer (e.g., via microSD adapter)
14) Rename "example.jpg" (or whatever your file is) as needed and move the file from microSD card to computer
15) Safely remove microSD card from computer
16) Reattach microSD card to camera
17) Rotate the camera lens slightly in a direction you feel will improve the focus.  Use past images to guide your way.
18) Repeat steps 10-17 until the faraway object is in the best focus possible.

How to trade image quality vs. size:
0) Ensure an SD card is connected to the OpenMV device
1) Connect the OpenMV device to a computer via USB cable
2) Open the OpenMV IDE on your computer
3) Open automatic_quality_test.py from the IDE
4) At the top of the IDE window, click on "Tools" > "Save open script to OpenMV cam" to save the current code to the SD card
5) Safely remove hardware and disconnect OpenMV device from computer
6) Point at an object of interest and supply power to the OpenMV device to take several pictures of it in sequence.  One way to do this is to reconnect the OpenMV device to the computer via USB cable.  It is important not to use the IDE to run the program---if you do, the images won't save to the SD card.
7) Safely disconnect OpenMV device from power (e.g., safely remove hardware and disconnect)
8) Remove microSD card from OpenMV device
9) Connect microSD card to computer (e.g., via microSD adapter)
10) Move "quality_XX.jpg" files to computer
11) Analyze the image quality by inspecting the images visually.  Trade image quality vs. size, either by inspection or by plotting this information somehow.
12) Safely remove microSD card from computer
13) Reattach microSD card to camera

How to run a manual time delay test:
0) Ensure an SD card is connected to the OpenMV device
1) Connect the OpenMV device to a computer via USB cable
2) Open the OpenMV IDE on your computer
3) Open the relevant PY file (either manual_blindness_test.py or manual_process_delay_test.py) from the IDE
4) From the IDE, manually change the variable of interest (either blindness_time or process_time) to be one of values in the corresponding array of interest (either blindness_array or process_delay_array)
5) At the top of the IDE window, click on "Tools" > "Save open script to OpenMV cam" to save the current code to the SD card
6) Safely remove hardware and disconnect OpenMV device from computer
7) Point at an object of interest and supply power to the OpenMV device to take a picture of it.  One way to do this is to reconnect the OpenMV device to the computer via USB cable.  It is important not to use the IDE to run the program---if you do, the images won't save to the SD card.
8) Safely disconnect OpenMV device from power (e.g., safely remove hardware and disconnect)
9) Remove microSD card from OpenMV device
10) Connect microSD card to computer (e.g., via microSD adapter)
11) Repeat steps 3-5, using a value from the array of interest that you haven't used before
12) Safely remove microSD card from computer
13) Reattach microSD card to camera
14) Repeat steps 7-13 until all values in the array of interest have been considered
15) Repeat steps 9-10
16) Move relevant files ("blindness_XXXX_ms.jpg" or "process_XXXX_ms.jpg") from microSD card to computer
17) Repeat steps 12-13
