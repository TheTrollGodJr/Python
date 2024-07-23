import cv2
import numpy as np

img = cv2.imread("cookieClicker/cookie.png")
t = 5
mask = cv2.inRange(img, np.array([96-t, 169-t, 196-t]), np.array([96+t, 169+t, 196+t]))
cv2.imwrite('cookieClicker/cookie-filtered.png', mask)
