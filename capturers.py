import cv2
import io
import numpy
import picamera

def camera():
    def function():
        buffer = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.capture(buffer, format='jpeg')
        buffer = numpy.fromstring(buffer.getvalue(), dtype=numpy.uint8)
        return cv2.imdecode(buffer, 1)
    return function
