def opencv(model, threshold):
    def recognize(image):
        label, confidence = model.predict(images.resize(image, (92, 112), cv2.INTER_LANCZOS4))
        return label if confidence < threshold else None
    return recognize

