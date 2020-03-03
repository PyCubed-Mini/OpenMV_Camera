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

# determine orientation
lt = img.get_pixel(0,0) #top left
rt = img.get_pixel(img.width()-1,0) #top right
lb = img.get_pixel(0,img.height()-1) #bottom left
rb = img.get_pixel(img.width()-1,img.height()-1) #bottom right
pix = [lt,rt,lb,rb]

max1 = max(pix)
pix.remove(max1)
max2 = max(pix)

if (max1 == lb and max2 == rb) or (max2 == lb and max1 == rb):
    orient = 0 #horizontal, earth on bottom
elif (max1 == lb and max2 == lt) or (max2 == lb and max1 == lt):
    orient = 1 #vertical, earth to left
elif (max1 == rb and max2 == rt) or (max2 == rb and max1 == rt):
    orient = 2 #vertical, earth to right
else:
    orient = 3 #horizontal, earth on top

# Determine threshold
upperthresh = img.get_histogram().get_threshold().value()
#upperthresh = hist.get_threshold()
upperthresh = math.floor(upperthresh)
lowerthresh = math.floor(0.6*upperthresh)
# Use Canny edge detector
img.find_edges(image.EDGE_CANNY, threshold=(lowerthresh, upperthresh))

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

if n<100:
    print("not enough edges")
    exit()

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

if orient == 0:
    alpha1 = (ymean - img.height()/2)/img.height()*14
    alpha = alpha1 + alpha0 #pitch
    psi = math.degrees(math.atan(a)) #yaw
elif orient == 1:
    alpha1 = (img.width()/2 + xmean)/img.width()*18.8
    alpha = alpha1 + alpha0 #pitch
    if a>0:
        psi = math.degrees(math.atan(a)) #yaw
    else:
        psi = 180 + math.degrees(math.atan(a)) #yaw
elif orient == 2:
    alpha1 = (xmean - img.width()/2)/img.width()*18.8
    alpha = alpha1 + alpha0 #pitch
    if a>0:
        psi = 360 - math.degrees(math.atan(a)) #yaw
    else:
        psi = 180 - math.degrees(math.atan(a)) #yaw
else:
    alpha1 = (img.height()/2 - ymean)/img.height()*14
    alpha = alpha1 + alpha0 #pitch
    psi = 180 + math.degrees(math.atan(a)) #yaw

print(alpha)
print(psi)
