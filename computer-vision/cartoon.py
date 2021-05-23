import argparse
import cv2
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())


image = cv2.imread(args.get("image"))
cv2.imshow("Original", image)

#Converting to RGB
img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Detecting edges of the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


#Cartoonifying the image
color = cv2.bilateralFilter(img, 10, 250, 250)
# bitwise operations with masks
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
