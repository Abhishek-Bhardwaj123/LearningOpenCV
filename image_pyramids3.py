import cv2

img = cv2.imread("doraemon.jpg")

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

hr_of_lr2 = cv2.pyrUp(lr2)

cv2.imshow("Level 1 Pyramid up", lr1)
cv2.imshow("Going from level2 to level 1 pyramid down", hr_of_lr2)

# 1. You decrease resolution by level 1.
# 2. You decrease resolution again so you are now at level 2.
# 3. You increase resolution by using pyrUp. So, you are now at level 1.
# Technically image at step1 must be equal/same at step 3.
# The image at step1 and step3 are same in size but image at step3 is blur as compared with step1.
# This is because at while performing step 2 we lost some pixel information of step1 image.
# Now, when we want to go back to step 1 by pyrUp the image at step2 will result a blur image.
cv2.waitKey(0)
cv2.destroyAllWindows()