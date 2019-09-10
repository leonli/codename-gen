import click
import random
from pyfiglet import Figlet
from termcolor import colored, cprint
import imagenet

@click.command()
@click.option("--count", default=10, help="Yield number of codenames.")
def codename_gen(count):
    """Enjoy the codenames 🍺"""
    imagenet_cls = imagenet.imagenet1000_labels()
    f = Figlet(font='slant')
    print(f.renderText('Codename Gen'))
    c_tag = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for _ in range(count):
        print(colored(random.choice(imagenet_cls), random.choice(c_tag)))
    cprint('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', 'green')
    cprint('Done! Enjoy the codenames 🍺', 'grey', 'on_green')

if __name__ == '__main__':
    codename_gen()

