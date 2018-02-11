import cv2
import time

def scan(interval, capture, detect, callback):
    while True:
        image = capture()
        detections = detect(image)
        if len(detections) == 0:
            time.sleep(interval)
        else:
            def cropper(vertices):
                left, top, width, height = vertices
                return crop(image, left, top, width, height)
            images = map(cropper, detections)
            callback(images)

def crop(image, left, top, width, height):
    right = left + width
    bottom = top + height
    return image[top:bottom, left:right]

def resize(image, width, height, interpolation):
    return cv2.resize(image, (width, height), interpolation)
