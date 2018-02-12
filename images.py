import cv2
import time

def scan(interval, ratio, capture, detect, callback):
    while True:
        image = cv2.cvtColor(capture(), cv2.COLOR_RGB2GRAY)
        detections = detect(image)
        if len(detections) == 1:
            x, y, w, h = detections[0]
            r = h / w
            if r > ratio:
                h = (w * ratio)
            else:
                w = (h / ratio)
            callback(resize(crop(image, x, y, w, h), 92, 112, interpolation = cv2.INTER_LANCZOS4))
        else:
            time.sleep(interval)

def crop(image, left, top, width, height):
    right = left + width
    bottom = top + height
    return image[top:bottom, left:right]

def resize(image, width, height, interpolation):
    return cv2.resize(image, (width, height), interpolation = interpolation)
