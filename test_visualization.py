import cv2
import csv
import numpy as np
import math
from visualization import plot

image = cv2.imread('data/train_images/0002cc93b.jpg')
csvfile = open('data/train.csv')

plot(image, csvfile)

cv2.waitKey(0)