import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), dtype=np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), dtype=np.uint8)
img2[0:250, 250:500] = cv2.bitwise_not(img2[0:250, 250:500])
bitwise_AND_Image = cv2.bitwise_and(img1, img2)
bitwise_OR_Image = cv2.bitwise_or(img1, img2)
bitwise_XOR_Image = cv2.bitwise_xor(img1, img2)
cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.imshow("Bitwise AND of Image1 & Image2", bitwise_AND_Image)
cv2.imshow("Bitwise OR of Image1 and Image2", bitwise_OR_Image)
cv2.imshow("Bitwise XOR of Image1 and Image2", bitwise_XOR_Image)
cv2.waitKey(0)
cv2.destroyAllWindows()


