import click
import mtgPriceCan.facetoface
import mtgPriceCan.settings


@click.command()
@click.argument('cards')
def cli(cards):
    mtgPriceCan.facetoface.face_to_face(cards, mtgPriceCan.settings.url)


if __name__ == '__main__':
    cli()