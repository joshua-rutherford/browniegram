import cv2
import images
import os

def opencv(model, directory):
    def train():
        images = []
        labels = []
        directories = os.listdir(directory)
        for label in directories:
            files = os.listdir(os.path.join(directory, label))
            for file in files:
                image = images.resize(cv2.imread(os.path.join(directory, label, file), cv2.IMREAD_GRAYSCALE), 92, 112, cv2.INTER_LANCZOS4)
                images.append(image)
                labels.append(label)
        model.train(images, labels)