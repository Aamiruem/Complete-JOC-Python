# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:12:12 2023

@author: Prathvish Shetty
"""
# Image Enhancement CLAHE-Contrast Limited Adaptive Histogram Equalization
import cv2

# Read the image
img = cv2.imread(r"C:\Users\aamir\Desktop\JOC Pythen\Complete-JOC-Python\Week2JOC\image.jpg")

# Preparation for CLAHE
clahe = cv2.createCLAHE()

# Convert to grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Enhancement process
enh_img = clahe.apply(gray_img)

# Save it to file
cv2.imwrite("enhanced.jpg", enh_img)
print("Done Enhancing")
