import cv2
import images
import os
import numpy

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
                print(b)
                face = images.resize(b, 92, 112, cv2.INTER_LANCZOS4)
                faces.append(face)
                labels.append(label)
        model.train(numpy.asarray(faces), numpy.asarray(labels))
    return train