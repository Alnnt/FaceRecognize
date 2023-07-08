import cv2 as cv


def detect_face(img, cascade):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.equalizeHist(img_gray)
    faces = cascade.detectMultiScale(img_gray)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
    cv.imshow('img', img)


# detector = cv.CascadeClassifier(r'.\models\haarcascade_frontalface_alt2.xml')  # 三次元人脸
detector = cv.CascadeClassifier(r'.\models\lbpcascade_animeface.xml')  # 二次元人脸

img = cv.imread(r"sample_group.jpg")
# img = cv.imread(r"sample_group_miku.jpg")

detect_face(img, detector)
cv.waitKey(0)
cv.destroyAllWindows()
