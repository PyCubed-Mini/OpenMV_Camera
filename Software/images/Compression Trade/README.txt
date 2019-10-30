Each of these trade studies trade file size against image compression quality.  The first two trades are rather informal; the third is intended to be the true study to be analyzed.

Conclusions:
- The default image quality is quality=50 at ~20 kB per photo
- quality=90 produces the best image quality results at ~100 kB per photo
- For unknown reasons, quality greater than 90 is not guaranteed to work and, in fact, almost always results in an error
- quality=90 images have infrequently resulted in heap memory issues, so it may be safe to proceed with quality=75 images, at ~50 kB per photo, in the future
