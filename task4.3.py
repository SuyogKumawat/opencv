import cv2
import numpy

i1=cv2.imread("ironman.jpg")
i2=cv2.imread("marvel.jpg")

#adding 2 images horizantally
merge_image=numpy.hstack((i1,i2))

cv2.imshow("Merged Image",merge_image)
cv2.waitKey()
cv2.destroyAllWindows()
