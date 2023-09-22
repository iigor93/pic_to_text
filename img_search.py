import numpy as np
import cv2

src = cv2.imread("./test.jpg")
Temp = cv2.imread("./mark.png")

src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
temp = cv2.cvtColor(Temp, cv2.COLOR_RGB2GRAY)

height, width = src.shape
print(height, width)

H, W = temp.shape
print(H, W)

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    src2 = src.copy()
    result = cv2.matchTemplate(src2, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    if method in [cv2.TM_SQDIFF, cv2.TM_CCORR]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + W, location[1] + H)
    cv2.rectangle(src2, location, bottom_right, (0, 128, 128), 5)
    cv2.imshow('name', src2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
