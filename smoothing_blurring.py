import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2nd arg: desired depth of the output image. If it is negative, it will be the same as that of the input image.
# mask = kernel = template = window
kernel = np.ones((5, 5), dtype=np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

blur = cv2.blur(img, (5, 5))

# The weight/coefficient at center is maximum.
# The weight is decreasing gradually while moving from center to boundary.
# Assume the image as matrix.
# Now the value at center is maximum.
# It gradually decrease while moving away from center.
# [
#    [1, 2, 1],
#    [1, 7, 1],
#    [1, 1 ,3]
# ]
# Gaussian Blur removes High Frequency Noise.
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# median blur removes salt & pepper noise.
# pixel[i] = average(neigbouring pixels)
# 2nd arg : kernelSize must be odd.
median = cv2.medianBlur(img, 5)

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', "2D Convolution", "Blur", "Gaussian Blur", "Median", "Bilateral"]
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)

# 2nd arg of imshow() : cmap
# cmap means color map.
# cmap works when we have image in 2D.
# It means that the image consist of only single channel.
# Basically, we have three channel Red, Green & Blue.
# We represent these channel via 0, 1, 2 (Sorry, I don't know the correct order. Means I don't know whether 0 is belong to red or green or blue.)
# To get any image in a single channel, we have following:
# img[:, :, 0] OR img[:, :, 1] OR img[:, :, 2]
# First two ':' represent the (x, y) coordinates
# After that either 0 or 1 or 2 represent the color intensity of either R or G or B at that point.
# Note: For image in 3D i.e, image where two or more channel present.
#       i.e, img[:] or img[:, :] <--- Both same don't get confuse.
#       The cmap don't show any change.
# For clear understanding check cmap_imshow.py file
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()