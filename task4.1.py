import cv2
import numpy

ph=numpy.zeros((400,400))
ph[200:]=1

for i in range(150,200):
    for j in range(100,301):
        ph[i][j]=1
        
for i in range(200,250):
    for j in range(100,301):
        ph[i][j]=0
        
        
cv2.imshow('Created Image',ph)
cv2.waitKey()
cv2.destroyAllWindows()
