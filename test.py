import cv2
import csv
import numpy as np
import math


image = cv2.imread('data/train_images/0002cc93b.jpg')
imageHeight = np.size(image, 0)
imageWidth = np.size(image, 1)
overlay = image.copy()

with open('data/train.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for row in reader:
        encoded_pixels = row[1].split(" ")
        encoded_pixels = list((int(encoded_pixels[i]), int(encoded_pixels[i+1])) for i in range(0, len(encoded_pixels), 2))
        for element in encoded_pixels:
            y = element[0] % imageHeight
            x = math.floor(element[0] / imageHeight)
            w = element[1]
            cv2.line(overlay, (x, y), (x, y+w), (0,255,0, 50), 1)
        #print(row)
        break

alpha = 0.1
image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
cv2.imshow('image', image_new)

cv2.waitKey(0)