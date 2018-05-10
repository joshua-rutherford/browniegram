import cv2
import os
import shutil
import uuid

DATABASE_PATH = os.path.join('.browniegram', 'db')

def add(name, image):
    path = os.path.join(DATABASE_PATH, name)
    file = os.path.join(path, '{0}.pgm'.format(uuid.uuid4()))
    cv2.imwrite(file, image)

def adder(name):
    path = os.path.join(DATABASE_PATH, name)
    def function(image):
        file = os.path.join(path, '{0}.pgm'.format(uuid.uuid4()))
        cv2.imwrite(file, image)
    return function

def remove(name):
    path = os.path.join(DATABASE_PATH, name)
    shutil.rmtree(path)

def iterate(function):
    directories = os.listdir(DATABASE_PATH)
    for directory in directories:
        i = i + 1
        files = os.listdir(os.path.join(DATABASE_PATH, directory))
        for file in files:
            function(i, file)
