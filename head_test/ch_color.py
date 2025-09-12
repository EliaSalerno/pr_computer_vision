import cv2 as cv
import numpy as np


image=cv.imread('./images/folla.jpg')

image_hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("Image",image_hsv)
cv.waitKey(0)
cv.destroyAllWindows()
#226,112,12
lower_pink=np.array([0,0,0])
upper_pink=np.array([40,255,255])

mask=cv.inRange(image_hsv,lower_pink,upper_pink)
result=cv.bitwise_and(image,image,mask=mask)
gray_image=cv.cvtColor(result,cv.COLOR_BGR2GRAY)

_, thrash = cv.threshold(gray_image, 235, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thrash, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
c=0
for contour in contours:
	shape=cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True),True)
	x_cor=shape.ravel()[0]
	y_cor=shape.ravel()[1]-15
	if len(shape) > 12:
		cv.drawContours(image,[shape],0,(0,0,255),4)
		c+=1
print(c)
cv.imshow("Image",gray_image)
cv.waitKey(0)
cv.destroyAllWindows()
