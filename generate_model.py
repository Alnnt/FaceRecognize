import os
import cv2 as cv
import numpy as np

# face_cascade = cv.CascadeClassifier(r'.\models\haarcascade_frontalface_alt2.xml')
face_cascade = cv.CascadeClassifier(r'.\models\lbpcascade_animeface.xml')


def getSamplesAndIds(path):
    faces_samples = []
    ids = []
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    print(image_paths)
    for imagePath in image_paths:
        img = cv.imread(imagePath)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img_numpy = np.array(img, 'uint8')
        faces = face_cascade.detectMultiScale(img)
        id = int(os.path.split(imagePath)[1].split('.')[0])
        for x, y, w, h in faces:
            ids.append(id)
            faces_samples.append(img_numpy[y:y + h, x:x + w])

    print('id: ', ids)
    print('faceSamples:', faces_samples)
    return faces_samples, ids


path = './images/'
faces, ids = getSamplesAndIds(path)
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))
recognizer.write('./trainer.xml')
cv.waitKey(0)
