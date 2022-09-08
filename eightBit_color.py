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


def check_red_green(value):
    if value < 32:
        return 32
    elif value < 64:
        return 64
    elif value < 96:
        return 96
    elif value < 128:
        return 128
    elif value < 160:
        return 160
    elif value < 192:
        return 192
    elif value < 224:
        return 224
    else:
        return 256


def check_blue(value):
    if value < 64:
        return 64
    elif value < 128:
        return 128
    elif value < 192:
        return 192
    else:
        return 256


for i in range(0, y-1):
    for j in range(0, x-1):
        r[i][j] = check_red_green(red[i][j])
        g[i][j] = check_red_green(green[i][j])
        b[i][j] = check_blue(blue[i][j])


bit_8 = cv2.merge((r, g, b))
#print(bit_8)

cv2.imshow("8bit color", bit_8)
cv2.waitKey()
