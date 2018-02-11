import capturers
import detectors
import images

def callback(images):
    print len(images)

if __name__ == '__main__':   
    capture = capturers.camera()
    detect = detectors.facial('./frontal.xml', 1.3, 4, 30, 30)
    images.scan(5, cature, detect, callback)