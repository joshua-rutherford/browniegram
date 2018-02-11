import cv2

def scan(inteval, capture, detect, callback):
    while True:
        image = capture()
        detections = detect(image)
        if detections
            def cropper(vertices):
                left, top, width, height = vertices
                return crop(image, left, top, width, height)
            images = map(cropper, detections)
            callback(images)
        else:
            sleep(interval)

def crop(image, left, top, width, height, preserve):
    right = left + width
    bottom = top + height
    return image[top:bottom, left:right]

def resize(image, width, height, interpolation):
    return cv2.resize(image, (width, height), interpolation)
