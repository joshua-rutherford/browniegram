import capturers
import click
import cv2
import db
import detectors
import images
import recognizers
import trainers

from espeak import espeak

model = cv2.createEigenFaceRecognizer()
recognize = recognizers.opencv(model, 4000)

@click.group()
def cli():
  pass

@click.command()
@click.argument('name')
def add(name):
    adder = db.adder(name)
    capturer = capturers.camera()
    detector = detectors.opencv('./.browniegram/frontal.xml', 1.3, 4, 30, 30)
    images.scan(1, 112 / 92, capturer, detector, adder)

@click.command()
@click.argument('name')
def remove(name):
    db.remove(name)

@click.command()
def run():
    train = trainers.opencv(model, './.browniegram/db')
    print('training...')
    names = train()
    print('trained...')
    capture = capturers.camera()
    detect = detectors.opencv('./.browniegram/frontal.xml', 1.3, 4, 30, 30)
    def callback(image):
        name = recognize(image)
        if name:
            print(names[name])
            espeak.synth("Delay. Hello %s. I was wondering where you have been."%names[name])
        else:
            print('unknown')
            espeak.synth("Delay. Hmm, have we met before.  I can't seem to recall your face.")
        while espeak.is_playing():
	        time.sleep(0.1)
    images.scan(5, 112 / 92, capture, detect, callback)

cli.add_command(add)
cli.add_command(run)

if __name__ == '__main__':
    cli()