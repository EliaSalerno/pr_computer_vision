import cv2

image=cv2.imread('./images/robot.jpg')

image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.imshow("Image",image_rgb)
cv2.waitKey(0)
cv2.imshow("Image",image_gray)
cv2.waitKey(0)
cv2.imshow("Image",image_rgb)
cv2.waitKey(0)
cv2.imshow("Image",image_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()