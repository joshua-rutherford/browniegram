import cv2

class Detector:

    def __init__(self, config):
        self.config = config
        self.classifier = cv2.CascadeClassifier(config["classifier"])

    def detect(image):
        faces = self.classifier.detectMultiScale(image, 
            scaleFactor = config["scaleFactor"], 
            minNeighbors = config["minimumNeighbors"],
            minSize = config["minimumSize"],
            flags = cv2.CASCADE_SCALE_IMAGE)
        return None if len(faces) != 1 else faces[0]
