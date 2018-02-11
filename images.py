import cv2
import time

def scan(interval, capture, detect, callback):
    while True:
        image = capture()
        detections = detect(image)
        if len(detections) == 1:
            left, top, width, height = detections[0]
            callback(crop(image[0], left, top, width, height))
        else:
            time.sleep(interval)

def crop(image, left, top, width, height):
    right = left + width
    bottom = top + height
    return image[top:bottom, left:right]

def resize(image, width, height, interpolation):
    return cv2.resize(image, (width, height), interpoloation = interpolation)
