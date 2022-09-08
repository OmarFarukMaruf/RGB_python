from email.mime import image
import cv2
import numpy as np

img = cv2.imread('64.jpg')
#img = cv2.resize(img, (1000,1000))

b, g, r = cv2.split(img)
y, x = g.shape

bit_8 = np.zeros((y, x), dtype='uint8')
for i in range(1, y):
    for j in range(1,x):
        if bit_8[y][x] >= 0 and bit_8[y][x] < 32:
            bit_8[y][x] = 32
        if bit_8[y][x] > 32 and bit_8[y][x] < 64:
            bit_8[y][x] = 64
        if bit_8[y][x] > 64 and bit_8[y][x] < 96:
            bit_8[y][x] = 96
        if bit_8[y][x] > 96 and bit_8[y][x] < 128:
            bit_8[y][x] = 128
        if bit_8[y][x] > 128 and bit_8[y][x] < 160:
            bit_8[y][x] = 160
        if bit_8[y][x] > 160 and bit_8[y][x] < 192:
            bit_8[y][x] = 192
        if bit_8[y][x] > 192 and bit_8[y][x] < 224:
            bit_8[y][x] = 224
        else:
            bit_8[y][x] = 256
cv2.imshow("8-Bit", bit_8)
cv2.waitKey()



# Output Error:
'''
IndexError: index 427 is out of bounds for axis 0 with size 427
'''

