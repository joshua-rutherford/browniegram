import cv2
import images

def opencv(model, threshold):
    def recognize(image):
        label, confidence = model.predict(image)
        print("I think it is {0} and I have a confidence of {0}", label, confidence)
        return label if confidence < threshold else None
    return recognize

