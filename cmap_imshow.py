import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread("doraemon.jpg")
l = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r']
print(len(l))
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = img1[:, :, 2]
for i in range(len(l)):
    plt.subplot(4, 10, i+1)
    plt.imshow(img2, cmap=l[i])
    plt.xticks([])
    plt.yticks([])
plt.show()