import cv2
import numpy as np

img = cv2.imread("ss.jpg")
img = cv2.resize(img, (500, 300))

cv2.imshow("main", img)

red, green, blue = cv2.split(img)

y, x = red.shape
r = np.zeros((y, x), dtype='uint8')
g = np.zeros((y, x), dtype='uint8')
b = np.zeros((y, x), dtype='uint8')

for i in range(0, y-1):
    for j in range(0, x-1):
        if red[i][j] < 32:
           r[i][j] = 32
        if red[i][j] < 64:
           r[i][j] = 64
        if red[i][j] < 96:
           r[i][j] = 96
        if red[i][j] < 128:
           r[i][j] = 128
        if red[i][j] < 160:
           r[i][j] = 160
        if red[i][j] < 192:
           r[i][j] = 192
        if red[i][j] < 224:
           r[i][j] = 226
        else:
            r[i][j] = 256


        if green[i][j] < 32:
           g[i][j] = 32
        if green[i][j] < 64:
           g[i][j] = 64
        if green[i][j] < 96:
           g[i][j] = 96
        if green[i][j] < 128:
           g[i][j] = 128
        if green[i][j] < 160:
           g[i][j] = 160
        if green[i][j] < 192:
           g[i][j] = 192
        if green[i][j] < 224:
           g[i][j] = 226
        else:
            g[i][j] = 256

        if blue[i][j] < 64:
           b[i][j] = 64
        if blue[i][j] < 128:
           b[i][j] = 128
        if blue[i][j] < 192:
           b[i][j] = 192
        else:
            b[i][j] = 256

bit_8 = cv2.merge((r, g, b))
#print(bit_8)

cv2.imshow("8bit color", bit_8)
cv2.waitKey()
