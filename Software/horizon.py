# Edge detection with Canny:
#
# This example demonstrates the Canny edge detector.
import sensor, image, pyb, math
# from pyb import SPI

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.RGB565
sensor.set_framesize(sensor.QVGA) # or sensor.QVGA (or others)
sensor.skip_frames(time = 4500) # Let new settings take affect.
sensor.set_gainceiling(8)

img = sensor.snapshot() # Take a picture and return the image.
img.save("edges.jpg")

#load in image
#with open('earth3.jpg', 'rb') as f:
#    img_data = f.read()

#img = image.Image(1920,758, sensor.GRAYSCALE)
#n=0
#for i in range(0,1920):
#    for j in range(0,758):
#        img[n] = img_data[n]
#        n = n+1

# Determine threshold
hist = img.get_histogram()
upperthresh = hist.get_threshold()
upperthresh = math.floor(1.2*upperthresh.value())
lowerthresh = math.floor(0.8*upperthresh)
# Use Canny edge detector
img.find_edges(image.EDGE_CANNY, threshold=(lowerthresh, upperthresh))
#img.save("edges.jpg")
print('success!')
# Faster simpler edge detection
#img.find_edges(image.EDGE_SIMPLE, threshold=(100, 255))
#img.save('edges.jpg')

# find indices for horizon pixels
xval = []
yval = []
n = 0

for i in range(0,img.width()):
    for j in range(0,img.height()):
        if img.get_pixel(i,j) == 255:
            xval.append(i)
            yval.append(j)
            n = n + 1

xsum = sum(xval)
ysum = sum(yval)
xmean = xsum/n
ymean = ysum/n

# least squares linear fit y = ax + b
xysum = 0
x2sum = 0
for i in range(0,n):
    xysum = xysum + xval[i]*yval[i]
    x2sum = x2sum + xval[i]**2

a = (n*xysum - xsum*ysum)/(n*x2sum - xsum**2)
b = (x2sum*ysum - xsum*xysum)/(n*x2sum - xsum**2)
b = ymean - a*xmean

print(a)
print(b)

# determine attitude

Re = 6378
h = 400
d = ((Re+h)**2-Re**2)**(1/2)
alpha0 = math.degrees(math.atan(Re/(Re+h)))

# pitch
alpha1 = (img.height()/2 - ymean)/img.height()*14
alpha = alpha1 + alpha0

# yaw
psi = math.degrees(math.atan(a))

print(alpha)
print(psi)
