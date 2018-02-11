import cv2

def facial(classifierFile, scaleFactor, minimumNeighbors, minimumWidth, minimumHeight):
    classifier = cv2.CascadeClassifier(classifierFile)
    def function(image):
        return classifier.detectMultiScale(image, 
            scaleFactor = scaleFactor, 
            minNeighbors = minimumNeighbors,
            minSize = (minimumWidth, minimumHeight),
            flags = cv2.CASCADE_SCALE_IMAGE)
    return function
