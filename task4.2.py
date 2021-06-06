import cv2

#Image-1
ph1=cv2.imread("cp.jpeg")

cv2.imshow("Image-1",ph1)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop the Image-1 
cp1=ph1[20:210,150:310]

cv2.imshow("Cropped Image-1",cp1)
cv2.waitKey()
cv2.destroyAllWindows()

#Image-2
ph2=cv2.imread("h.png")

cv2.imshow("Image-2",ph2)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop the Image-2
cp2=ph2[0:190,120:280]

cv2.imshow("Cropped Image-2",cp2)
cv2.waitKey()
cv2.destroyAllWindows()

#Swapping of both crop images which result change in original image
img1=cv2.imread("cp.jpeg")

img1[20:210,150:310]=cp2

cv2.imshow("Image-1",img1)
cv2.waitKey()
cv2.destroyAllWindows()

img2=cv2.imread("h.png")

img2[0:190,120:280]=cp1

cv2.imshow("Image-1",img2)
cv2.waitKey()
cv2.destroyAllWindows()
