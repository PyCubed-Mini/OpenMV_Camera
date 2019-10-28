This blindness trade completes the series of trade studies for the first OpenMV camera.

"Blindness" is defined as the time required for the camera to "open its eye"—that is, how much time is alloted for new settings to take place after the camera resets.  With insufficient "blindness" time, the images may become dark or corrupted.  With too much "blindness" time, the Qube wastes power.  An optimum must be found to trade security of image saving and power consumption.

Findings:
- Below 1000 ms of "blindness," the image files corrupt and cannot save properly
- Below 3000 ms of "blindness," the camera has insufficient heap memory to take quality=90 JPEG images, so quality must be reduced to quality=75 or quality=80
- Between 3000 ms and 4000 ms of "blindness," quality=90 images may fail to save
- No substantial benefits for "blindness" times greater than 4000 ms

Conclusions:
- A minimum of 1000 ms of "blindness" is required to save photos (though more is safer)
- For quality=75 images, a "blindness" time of 2000 ms should be sufficient
- For quality=90 images, a "blindness" time of 3000 ms may be enough, but 4000 ms is recommended

Note that images with "blindness" times below 3000 ms are saved as quality=75, while images with "blindness" times at or above 3000 ms are saved as quality=90.
