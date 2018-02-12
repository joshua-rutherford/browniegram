import cv2
import time

def scan(interval, capture, detect, callback):
    while True:
        image = cv2.cvtColor(capture, cv2.COLOR_RGB2GRAY)
        detections = detect(image)
        if len(detections) == 1:
            left, top, width, height = detections[0]
            print("{0}, {1}, {2}, {3}".format(left, top, width, height))
            callback(crop(image[0], left, top, 92, 112))
        else:
            time.sleep(interval)

def crop(image, left, top, width, height):
    right = left + width
    bottom = top + height
    return image[top:bottom, left:right]

def resize(image, width, height, interpolation):
    return cv2.resize(image, (width, height), interpolation = interpolation)
