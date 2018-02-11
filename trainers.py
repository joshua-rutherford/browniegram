import cv2
import images
import os

def opencv(model, directory):
    def train():
        faces = []
        labels = []
        directories = os.listdir(directory)
        for label in directories:
            files = os.listdir(os.path.join(directory, label))
            for file in files:
                a = os.path.join(directory, label, file)
                print(a)
                b = cv2.imread(a, cv2.IMREAD_GRAYSCALE)
                face = images.resize(a, 92, 112, cv2.INTER_LANCZOS4)
                faces.append(face)
                labels.append(label)
        model.train(images, labels)
    return train