def opencv(model, threshold):
    def recognize(image):
        label, confidence = model.predict(image)
        return label if confidence < threshold else None
    return recognize

