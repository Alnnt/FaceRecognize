import cv2 as cv

img = cv.imread(r'face_rgb.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_equalizeHist = cv.equalizeHist(img_gray)  # 直方图均衡

cv.imwrite(r'face_gray.jpg', img_gray)
cv.imwrite(r'face_equalizeHist.jpg', img_equalizeHist)

cv.imshow('RGB', img)
cv.imshow('GRAY', img_gray)
cv.imshow('equalizeHist', img_equalizeHist)
cv.waitKey(0)
