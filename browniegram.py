import capturers
import click
import db
import images
import trainers

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
    model = cv2.createEigenFaceRecognizer()
    train = trainers.opencv(model, './.browniegram/db')
    train()
    capture = capturers.camera()
    detect = detectors.opencv('./.browniegram/frontal.xml', 1.3, 4, 30, 30)
    images.scan(5, 112 / 92, capture, detect, callback)

cli.add_command(add)
cli.add_command(run)

if __name__ == '__main__':
    cli()