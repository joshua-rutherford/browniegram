import capturers
import cv2
import detectors
import images
import recognizers
import trainers

capture = capturers.camera()
detect = detectors.opencv('./frontal.xml', 1.3, 4, 30, 30)
model = cv2.createEigenFaceRecognizer()
train = trainers.opencv(model, './db')
recognize = recognizers.opencv(model, 1000)

def callback(image):
    name = recognize(image)
    if name:
        print(name)
    else:
        print('unknown')

if __name__ == '__main__':
    train()
    capture = capturers.camera()
    detect = detectors.opencv('./frontal.xml', 1.3, 4, 30, 30)
    images.scan(5, capture, detect, callback)