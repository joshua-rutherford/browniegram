import camera
import click
import detector
import json

@click.group()
def cli():
    pass

@click.command()
@click.argument('config')
def create(config):
    image = camera.capture()
    with open(config) as file:
        detector = detector.Detector(json.load(file)["detector"])
    results = detector.detect(image)
    click.echo(results)

@click.command()
def delete(name):
    click.echo("Delete...")

@click.command()
def list():
    click.echo("Listing...")

cli.add_command(create)
cli.add_command(delete)
cli.add_command(list)

if __name__ == '__main__':
    cli()
