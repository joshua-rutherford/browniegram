import cv2
import images
import os
import numpy

def opencv(model, directory):
    def train():
        faces = []
        labels = []
        names = {}
        i = 0
        directories = os.listdir(directory)
        for label in directories:
            i = i + 1
            names[i] = label
            print("Index: {0}, Label: {1}".format(i, label))
            files = os.listdir(os.path.join(directory, label))
            for file in files:
                face = images.resize(cv2.imread(os.path.join(directory, label, file), cv2.IMREAD_GRAYSCALE), 92, 112, cv2.INTER_LANCZOS4)
                faces.append(face)
                labels.append(i)
        model.train(numpy.asarray(faces), numpy.asarray(labels))
        return names
    return train