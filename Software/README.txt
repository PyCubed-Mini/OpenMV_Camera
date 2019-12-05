This folder holds all of the software "hacky" stuff from our attempts to figure out how to interface the OpenMV Cam software & hardware with the MCU.

Description of current contents:



- **Black Box** is probably what you're looking for.  It's a black box for testing new lenses for the OpenMV camera, should the need ever arise.  Just follow the instructions therein, and you should be fine.

- **feather_m4_express_backup** is a backup folder containing all of the original files present on a fresh Feather M4 Express MCU.  If you ever need to re-flash the MCU (e.g., it bricked, or it disconnected without "safely removing hardware"), copy and paste the files in this folder to the MCU's internal storage.

- **images** contains the photographic results of several trade studies.  Use these for inspiration for conducting additional trade studies or testing other lenses.

- **references** contains references that are vital for understanding the camera and MCU hardware.

- **trinket_m0_backup** is a backup folder containing all of the original files present on a fresh Trinket M0 MCU.  If you ever need to re-flash the MCU (e.g., it bricked, or it disconnected without "safely removing hardware"), copy and paste the files in this folder to the MCU's internal storage.



- **feather_m4_express_main.py** is the main.py file for the Feather M4 Express MCU.  The first set of comments in the file describe what the program does.  To use this program, simply download the file, rename it to main.py, and paste it to the MCU's internal storage.

- **snap_on_trigger.py** is the intended main.py file for the OpenMV camera.  The first set of comments in the file describe what the program does.  To use this program, simply download the file, rename it to main.py, and paste it to the camera's internal storage (if no SD card is attached) or to the camera's SD card (if an SD card *is* attached).  Please only use this program if the MCU and camera hardware are electrically configured to communicate over SPI.  Otherwise, the camera will return an error.

- **spi_troubleshooter.py** is a troubleshooter main.py file for the OpenMV camera.  Use this code if snap_on_trigger.py suggests that there is a bug in the SPI communication protocol between the MCU and the camera.  The intended use of this code is to communicate over SPI continuously, view the outputs using PuTTY (or some other TTY terminal), and tweak the electrical configuration until the system stops misbehaving.  You may literally have to hold down the jumper cables on the breadboard to get this to work.  Breadboards suck.  To use this program, simply download the file, rename it to main.py, and paste it to the camera's internal storage (if no SD card is attached) or to the camera's SD card (if an SD card *is* attached).  Please only use this program if the MCU and camera hardware are electrically configured to communicate over SPI.  Otherwise, the camera will return an error.

- **trinket_m0_main.py** is the main.py file for the Trinket M0 MCU.  Although the code still works, at this point, it is deprecated and only presented here for reference.

- **trinket_m0_original.py** is the original main.py file for the Trinket M0 MCU, provided for reference only.
